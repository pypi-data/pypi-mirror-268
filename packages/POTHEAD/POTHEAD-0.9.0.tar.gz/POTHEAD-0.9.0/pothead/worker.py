#!/usr/bin/env python3

from http import HTTPStatus
from logging import getLogger
from os import environ
from signal import SIGTERM, signal
from socket import (
    AF_INET,
    IPPROTO_TCP,
    SHUT_RDWR,
    SO_KEEPALIVE,
    SOCK_STREAM,
    SOL_SOCKET,
    TCP_KEEPCNT,
    TCP_KEEPIDLE,
    TCP_KEEPINTVL,
    getaddrinfo,
    socket,
)
from threading import Condition, Thread, Timer
from time import monotonic, sleep
from typing import Dict, Optional, Set
from uuid import uuid4
from wsgiref import simple_server

from werkzeug.serving import BaseWSGIServer, make_server

from .gating import wait_for_idle_cpus
from .oob_response import OutOfBandResponder
from .resource_balancer import ResourceBalancer, ResourceLoan
from .subprocess_middleware import SubprocessMiddleware
from .util import JobTracker, ObjectProxy, SocketCheckingWSGIHandler
from .wsgi_typing import (
    WsgiApplication,
)

LOGGER = getLogger("pothead.worker")
BROKER_CONNECT_RETRY_INTERVAL = 2


class DeferrableCleanup:
    def __init__(self, f):
        self.f = f

    def assume(self):
        f = self.f
        self.f = None
        return f

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if self.f:
            self.f()


class Flag:
    def __init__(self):
        self._set = False
        self._cond = Condition()

    def __bool__(self):
        return self._set

    def set(self):
        with self._cond:
            self._set = True
            self._cond.notify_all()

    def wait(self, timeout: float):
        with self._cond:
            self._cond.wait_for(lambda: self._set, timeout)


class Handler(SocketCheckingWSGIHandler):
    protocol_version = "HTTP/1.1"
    ph_server: "Server"
    request_received_at: Optional[float]
    request_id: Optional[str]

    def __init__(
        self, socket, address, server: "Server", cb_request_received, cb_processing_done
    ):
        self.cb_request_received = cb_request_received
        self.env = None
        self.request_id = None
        self.request_received_at = None
        self.ph_server = server

        with DeferrableCleanup(cb_processing_done) as c:
            if isinstance(server.app, OutOfBandResponder):
                server = ObjectProxy(server)  # type: ignore
                server.app = self._oob_wrapped_app(server.app, c.assume)

            super().__init__(socket, address, server)

    @staticmethod
    def _oob_wrapped_app(app, assume_cleanup) -> WsgiApplication:
        def application(environ, start_response):
            return app(environ, start_response, assume_cleanup)

        return application

    def handle_one_request(self):
        try:
            # Handler may be used for several requests, so we must reset
            # environment overrides each time
            self.env = None
            super().handle_one_request()
        finally:
            self.close_connection = True

    def run_wsgi(self) -> None:
        self.request_received_at = monotonic()
        self.request_id = str(self.headers.get("X-Request-Id", None) or uuid4())

        # This socket shall no longer be fast-closed on SIGTERM
        socket = self.request
        self.ph_server.sockets_waiting_for_request.remove(socket)

        with self.ph_server.worker_tracker.scope(self.request_id):
            super().run_wsgi()

    def make_environ(self):
        environ = super().make_environ()
        environ["REQUEST_ID"] = self.request_id

        if self.cb_request_received:
            self.cb_request_received(environ)

        return environ

    def log_message(self, format, *args):
        LOGGER.info("[%s] " + format, self.request_id, *args)

    def log_request(self, code="-", size="-"):
        if isinstance(code, HTTPStatus):
            code = code.value
        LOGGER.info(
            'Accepted request [%s] "%s" %s %s',
            self.request_id,
            self.requestline,
            str(code),
            str(size),
        )

    def connection_dropped(self, e, env):
        self.log_error("Cancelled by disconnected client")

    def log_error(self, format, *args):
        LOGGER.error("[%s] " + format, self.request_id, *args)

    def log_elapsed(self):
        LOGGER.info(
            "[%s] Elapsed: %.3f",
            self.request_id,
            monotonic() - self.request_received_at,
        )


class LoadBalancer:
    REFRESH_INTERVAL = 5
    DELAY_BASE = float(environ.get("LOAD_BALANCER_CONNECTION_DELAY_BASE", 1))
    DELAY_EXP = float(environ.get("LOAD_BALANCER_CONNECTION_DELAY_EXP", 1.5))

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._balancer = ResourceBalancer()
        self.refresh()

    def min_instance_connections(self):
        return self._balancer.usage_min()

    def wait_if_all_busy(self):
        """If all resources are already busy, wait for a while, longer if resources are more busy.
        If resources become more available while waiting, the wait-time will be reduced.
        """
        min_connections = self._balancer.usage_min()
        if min_connections > 0:
            # All endpoints already have
            start = monotonic()
            time_left = (
                start
                + (self.DELAY_BASE * (min_connections**self.DELAY_EXP))
                - monotonic()
            )
            while time_left > 0:
                min_connections = self._balancer.wait_for_change(
                    self._balancer.usage_min, min_connections, timeout=time_left
                )
                time_left = (
                    start
                    + (self.DELAY_BASE * (min_connections**self.DELAY_EXP))
                    - monotonic()
                )

    def acquire_addr(self) -> ResourceLoan:
        return self._balancer.acquire()

    def refresh(self):
        try:
            results = getaddrinfo(self.host, self.port, type=SOCK_STREAM)
            hosts = (sockaddr for _f, _t, _p, _c, sockaddr in results)
            self._balancer.provision(hosts)
        except BaseException:
            LOGGER.exception(
                "Failed to refresh endpoints for %s:%d", self.host, self.port
            )
        t = Timer(self.REFRESH_INTERVAL, self.refresh)
        t.daemon = True
        t.start()


class RequestCounter:
    def __init__(self, app):
        self._app = app
        self.started = 0
        self.completed = 0

    def __call__(self, environ, start_response):
        self.started += 1
        yield from self._app(environ, start_response)
        self.completed += 1


class Server:
    ssl_context = None
    multithread = False
    multiprocess = False
    passthrough_errors = False
    inspection_server: Optional[BaseWSGIServer] = None

    def __init__(
        self,
        addr,
        app,
        *,
        load_balancer=LoadBalancer,
        redirect_port: Optional[int] = None,
        inspection_port: Optional[int] = None,
        use_request_subprocess: bool = False,
        oob_cleanup_interval_seconds: Optional[float] = None,
        oob_item_expiry_seconds: Optional[float] = None,
    ):
        (host, port) = addr
        # Set up base environment
        env: Dict[str, str] = {}
        env["SERVER_NAME"] = host
        env["GATEWAY_INTERFACE"] = "HTTP/1.1"
        env["SERVER_PORT"] = port
        env["REMOTE_HOST"] = ""
        env["CONTENT_LENGTH"] = ""
        env["SCRIPT_NAME"] = ""
        self.base_environ = env

        self.broker_balancer = load_balancer(host, port)
        self.sockets_waiting_for_request: Set[socket] = set()
        self.worker_tracker = JobTracker()

        self.stopping = Flag()
        self.stopped = Flag()

        if inspection_port is not None:
            self.inspection_server = make_server(
                "", inspection_port, self.inspect, threaded=True
            )
            Thread(target=self.inspection_server.serve_forever, daemon=True).start()

        self.wait_for_slot = getattr(app, "wait_for_slot", None)
        if self.wait_for_slot:
            del app.wait_for_slot
        self.app = app
        self.app = (
            SubprocessMiddleware(LOGGER, self.app)
            if use_request_subprocess
            else self.app
        )
        self.app = self.request_counter = RequestCounter(self.app)
        self.app = (
            OutOfBandResponder(
                self.app,
                redirect_port,
                oob_cleanup_interval_seconds,
                oob_item_expiry_seconds,
            )
            if redirect_port is not None
            else self.app
        )

    def inspect(self, environ, start_response):
        if environ.get("REQUEST_METHOD", None) != "GET":
            start_response("405 Only GET supported", ())
            return
        path = environ.get("PATH_INFO", None)
        if path == "/inspect":
            start_response("200 OK", ())
            yield "requests pending:\n".encode()
            for request_id in self.worker_tracker.ongoing_requests():
                yield f"  {request_id}\n".encode()
            if hasattr(self.app, "inspect"):
                yield from self.app.inspect()
            yield f"{len(self.sockets_waiting_for_request)} blocked waiting for request\n".encode()
        elif path == "/apocalypse":
            start_response("200 OK", ())
            while not self.stopped.wait(5):
                yield b"Not yet\n"
            yield b"It's time\n"
        else:
            start_response("404 Not found", ())

    def worker(self):
        while not self.stopping:
            with self.broker_balancer.acquire_addr() as addr:
                self.broker_balancer.wait_if_all_busy()
                self._fetch_and_run_one_job(addr)

    def _fetch_and_run_one_job(
        self, addr, cb_request_received=None, cb_processing_done=lambda: None
    ):
        with socket(AF_INET, SOCK_STREAM) as s:
            self.sockets_waiting_for_request.add(s)
            try:
                s.connect(addr)
                self.server_address = s.getsockname()

                s.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
                s.setsockopt(IPPROTO_TCP, TCP_KEEPIDLE, 1)
                s.setsockopt(IPPROTO_TCP, TCP_KEEPINTVL, 2)
                s.setsockopt(IPPROTO_TCP, TCP_KEEPCNT, 3)
            except Exception as e:
                LOGGER.error("Couldn't connect to broker: %r", e)
                cb_processing_done()
                sleep(BROKER_CONNECT_RETRY_INTERVAL)
                return

            try:
                h = Handler(s, addr, self, cb_request_received, cb_processing_done)
            except BaseException:
                LOGGER.exception("In WSGI request handling")
                sleep(1)
                return

            try:
                s.shutdown(SHUT_RDWR)
            except OSError:
                # We shutdown to ensure flushing, and for courtesy, but we don't care about errors here
                pass

            if h.request_received_at:
                h.log_elapsed()

    def get_app(self):
        return self.app

    def shutdown(self):
        LOGGER.info("Shutting down workers...")
        self.stopping.set()
        for s in list(self.sockets_waiting_for_request):
            try:
                s.shutdown(SHUT_RDWR)
                s.close()
            except OSError:
                pass

        self.worker_tracker.drain(LOGGER)

        if isinstance(self.app, OutOfBandResponder):
            self.app.shutdown()
        LOGGER.info("Worker shutdown completed")
        self.stopped.set()
        if self.inspection_server is not None:
            self.inspection_server.shutdown()
        LOGGER.info(
            "%d jobs started. %d jobs successfully completed",
            self.request_counter.started,
            self.request_counter.completed,
        )
        LOGGER.info("All services stopped")

    def poll_loop(self):
        """Uses app.wait_for_slot() spawn new workers dynamically. This is useful, for example to wait for
        enough CPU, memory, or disk space, to start next job.

        `wait_for_slot` is expected to block until it's time to poll for a new job. It is given a function
        `halt` which it should poll intermittently to check if this worker is undergoing `shutdown()`.

        It may return an object, if so `obj.request_received(environ)` will be called when a request is
        received and `obj.done()` when either the request is received, or if polling failed in which case
        `request_received()` was never called.

        See pothead.gating for some ready-made `wait_for_slot` implementations"""

        while not self.stopping:
            # If all brokers are already waiting for a request, we want to hold off for a little bit
            self.broker_balancer.wait_if_all_busy()

            callbacks = self.wait_for_slot(lambda: bool(self.stopping))
            if self.stopping:
                break

            broker_instance_lease = self.broker_balancer.acquire_addr()
            if self.stopping:
                break

            Thread(
                target=self._run_one_poll, args=(broker_instance_lease, callbacks)
            ).start()

    def _run_one_poll(self, broker_instance_lease: ResourceLoan, callbacks):
        def request_received(environ):
            broker_instance_lease.release()
            getattr(callbacks, "request_received", lambda _: None)(environ)

        with broker_instance_lease as addr:
            self._fetch_and_run_one_job(
                addr, request_received, getattr(callbacks, "done", lambda: None)
            )

    def log(self, type, msg, *args, **kwargs):
        getattr(LOGGER, type)(msg.rstrip(), *args, **kwargs)


def install_term_handler(f):
    previous = []

    def on_term(_signal, _stack):
        Thread(target=f).start()
        for p in previous:
            p()

    p = signal(SIGTERM, on_term)
    if p:
        previous.append(p)


demo_app = simple_server.demo_app
demo_app.wait_for_slot = wait_for_idle_cpus(3)  # type: ignore


if __name__ == "__main__":
    from argparse import ArgumentParser
    from importlib import import_module
    from logging import INFO, basicConfig
    from sys import path

    path.insert(0, ".")

    def address(str):
        (host, port) = str.rsplit(":", 1)
        return (host, int(port))

    def func(str):
        (module, symbol) = str.rsplit(":", 1)
        module = import_module(module)
        return getattr(module, symbol)

    DEFAULT_WORKERS = int(environ.get("POTHEAD_WORKERS", 1))
    DEFAULT_MAX_PENDING = int(environ.get("POTHEAD_MAX_PENDING", 1))

    parser = ArgumentParser(description="Run WSGI app in sequential `worker` mode")
    parser.add_argument(
        "--connect",
        default="localhost:4040",
        type=address,
        help="Load Balancer Hub to connect to [host:port]",
    )
    parser.add_argument(
        "--redirect-response",
        default=None,
        help="When streaming successful responses, first redirect client to worker at [port]",
    )
    parser.add_argument(
        "--inspection-port",
        default=None,
        type=int,
        help="If set, the server will serve a small inspection-API on [port]",
    )
    parser.add_argument(
        "--use-request-subprocess",
        action="store_true",
        help=(
            "Spawn a separate WSGI app subprocess for handling each request. "
            + "Note: Only suitable for use cases where the request payload is small."
        ),
    )

    job_control_group = parser.add_mutually_exclusive_group()
    job_control_group.add_argument(
        "--workers",
        default=DEFAULT_WORKERS,
        type=int,
        help=f"Number of worker Processes (default: {DEFAULT_WORKERS})",
    )
    job_control_group.add_argument(
        "--poll-jobs",
        action="store_true",
        help="Use `app.wait_for_slot` to determine when to pull new jobs",
    )

    parser.add_argument(
        "app",
        nargs="?",
        default="pothead.worker:demo_app",
        type=func,
        help="The WSGI request handler to handle requests",
    )
    args = parser.parse_args()
    basicConfig(level=INFO)

    LOGGER.info("Initializing server for app %s", args.app)

    server = Server(
        args.connect,
        args.app,
        redirect_port=args.redirect_response,
        use_request_subprocess=args.use_request_subprocess,
        inspection_port=args.inspection_port,
    )

    install_term_handler(server.shutdown)

    if args.poll_jobs:
        LOGGER.info(
            "Starting up job-polling dynamic workers connecting to %s", args.connect
        )
        server.poll_loop()
        LOGGER.info("connect-loop shut down completed")
    else:
        LOGGER.info(
            "Starting up %d workers connecting to %s", args.workers, args.connect
        )
        workers = [Thread(target=server.worker) for _ in range(args.workers)]
        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join()
