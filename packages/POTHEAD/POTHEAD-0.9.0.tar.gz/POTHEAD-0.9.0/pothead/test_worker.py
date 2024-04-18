from socket import AF_INET, SOCK_STREAM, socket, timeout as TimeoutError, SHUT_RDWR
from threading import Thread
from time import sleep, monotonic
from typing import Optional
from unittest import TestCase
from unittest.mock import MagicMock
from urllib.request import urlopen
from logging import INFO
from uuid import uuid4

from pytest import fixture

from pothead.test_subprocess_middleware import wait_for, worker_running

OOB_CLEANUP_INTERVAL_SECONDS = 0.05
OOB_ITEM_EXPIRY_SECONDS = 0.5
REQUEST_ID = "im-quite-unique!"

from pothead.gating import wait_for_idle_cpus  # noqa: E402 override environ first

from .util import ObjectProxy  # noqa: E402
from .worker import LoadBalancer, Server  # noqa: E402


class Flag:
    def __init__(self) -> None:
        self.v = False

    def set(self):
        self.v = True

    def is_set(self) -> bool:
        return self.v


def demo_app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path == "/":
        start_response("200 OK", ())
        yield b"Hello World!"
    elif path == "/crash":
        raise Exception("Nope nope nope")
    elif path == "/slow_loris":
        sleep(0.05)
        start_response("200 OK", ())
        for byte in b"This might take a while...":
            sleep(0.1)
            yield byte
    elif path == "/hang_forever":
        do_yield = environ.get("HTTP_YIELD", "").lower() == "true"
        if environ.get("HTTP_START_RESPONSE", "").lower() == "true":
            start_response("200 OK", ())
        while True:
            if do_yield:
                yield b""
            sleep(0.01)
    else:
        start_response("404 Not Found", ())


def tracked_demo_app(is_terminated: Flag):
    def app(environ, start_response):
        try:
            demo_app(environ, start_response)
        finally:
            is_terminated.set()

    return app


class WorkerConnection:
    def __init__(self, sock: socket):
        self.sock = sock

    def send_request(self, path="/", headers={}):
        if "x-request-id" not in headers:
            headers["x-request-id"] = REQUEST_ID
        self.sock.sendall(f"GET {path} HTTP/1.1\r\n".encode("ascii"))
        for k, v in headers.items():
            self.sock.send(f"{k}: {v}\r\n".encode("ascii"))
        self.sock.sendall(b"\r\n")

    def read_response(self):
        buf = b""
        read = True
        while read:
            read = self.sock.recv(1024)
            buf += read
        return buf

    def parse_response(self):
        response = self.read_response()
        response_lines = iter(response.split(b"\r\n"))
        (_http_version, status, *_) = next(response_lines).split()
        headers = {}
        for line in response_lines:
            if line == b"":
                break
            (name, value) = line.split(b":", maxsplit=1)
            headers[name.strip().lower().decode("ascii")] = str(
                value.strip().decode("ascii")
            )
        return int(status), headers

    def disconnect(self):
        self.sock.shutdown(SHUT_RDWR)
        self.sock.close()


class DummyBroker:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(("localhost", 0))
        self.sock.listen(1)

    def addr(self):
        return self.sock.getsockname()

    def accept(self, timeout) -> Optional[WorkerConnection]:
        self.sock.settimeout(timeout)
        try:
            sock, _ = self.sock.accept()
            return WorkerConnection(sock)
        except TimeoutError:
            return None


def mock_balancer(addresses):
    class MockBalancer(LoadBalancer):
        def refresh(self):
            self._balancer.provision(addresses)

    return MockBalancer


class WorkerTest(TestCase):
    def test_load_balancing(self):
        broker_a, broker_b = (DummyBroker() for _ in range(2))
        app = ObjectProxy(demo_app)
        app.wait_for_slot = wait_for_idle_cpus(0, max_concurrent=10)

        worker = Server(
            ("", 0),
            app,
            load_balancer=mock_balancer(map(DummyBroker.addr, (broker_a, broker_b))),
        )
        Thread(target=worker.poll_loop, daemon=True).start()

        connection_a = broker_a.accept(0.1)
        connection_b = broker_b.accept(0.1)

        assert broker_a.accept(0.2) is None
        assert broker_b.accept(0.2) is None

        connection_b.send_request()
        assert broker_b.accept(0.2) is not None

        connection_a.send_request()
        assert broker_a.accept(0.2) is not None

    def test_cancel_hung_request(self):
        broker = DummyBroker()
        request_finished = Flag()

        app = ObjectProxy(tracked_demo_app(request_finished))
        app.wait_for_slot = wait_for_idle_cpus(0, max_concurrent=10)

        server = Server(
            ("", 0),
            app,
            load_balancer=mock_balancer([broker.addr()]),
        )
        Thread(target=server.poll_loop, daemon=True).start()
        connection = broker.accept(0.1)

        connection.send_request("/hang_forever", {"yield": True})
        sleep(0.1)
        connection.disconnect()

        sleep(0.1)

        assert request_finished.is_set()


class WaitForFirstSlot:
    def __init__(self, callbacks):
        self.counter = 0
        self.callbacks = callbacks

    def __call__(self, halt):
        self.counter += 1
        if self.counter <= 1:
            return self.callbacks
        else:
            from time import sleep

            while not halt():
                sleep(0.05)


class OutOfBandResponseTest(TestCase):
    @fixture(autouse=True)
    def use_caplog(self, caplog):
        caplog.set_level(INFO)
        self.caplog = caplog

    def setUp(self):
        broker = DummyBroker()
        self.callbacks = MagicMock()

        app = ObjectProxy(demo_app)
        app.wait_for_slot = WaitForFirstSlot(self.callbacks)

        self.server = Server(
            ("", 0),
            app,
            load_balancer=mock_balancer([broker.addr()]),
            redirect_port=0,
            oob_cleanup_interval_seconds=OOB_CLEANUP_INTERVAL_SECONDS,
            oob_item_expiry_seconds=OOB_ITEM_EXPIRY_SECONDS,
        )
        Thread(target=self.server.poll_loop, daemon=True).start()
        self.connection = broker.accept(0.1)

    def tearDown(self):
        self.server.shutdown()

    def test_response_redirect(self):
        self.connection.send_request()
        status, headers = self.connection.parse_response()
        assert status == 303

        with urlopen(headers.get("location")) as real_response:
            assert real_response.status == 200
            assert real_response.read().startswith(b"Hello World!")

    def test_reject_no_redirect(self):
        self.connection.send_request("/nonexisting")
        resp = self.connection.read_response().split(b"\r\n")

        assert resp[0] == b"HTTP/1.1 404 Not Found"
        assert b"Location" not in [x.split(b":") for x in resp]

    def test_fail_no_redirect(self):
        self.connection.send_request("/crash")
        resp = self.connection.read_response().split(b"\r\n")

        assert resp[0] == b"HTTP/1.1 500 INTERNAL SERVER ERROR"
        assert b"Location" not in [x.split(b":") for x in resp]

    def test_ondone_deferred(self):
        self.connection.send_request()
        status, headers = self.connection.parse_response()
        assert status == 303

        self.callbacks.done.assert_not_called()

        with urlopen(headers.get("location")) as real_response:
            assert real_response.status == 200
            assert real_response.read().startswith(b"Hello World!")

        self.callbacks.done.assert_called()

    def test_ondone_called_for_crash(self):
        self.connection.send_request("/crash")
        self.connection.read_response()

        self.callbacks.done.assert_called()

    def test_ondone_called_for_reject(self):
        self.connection.send_request("/nonexisting")
        self.connection.read_response()

        self.callbacks.done.assert_called()

    def test_ondone_called_after_timeout(self):
        self.connection.send_request()
        self.connection.read_response()

        self.callbacks.done.assert_not_called()

        sleep(OOB_ITEM_EXPIRY_SECONDS + 2 * OOB_CLEANUP_INTERVAL_SECONDS)

        self.callbacks.done.assert_called()

    def test_log_elapsed_after_success(self):
        self.connection.send_request()
        self.connection.read_response()

        sleep(0.05)

        assert f"[{REQUEST_ID}] Elapsed: " in self.caplog.text

    def test_log_elapsed_after_crash(self):
        self.connection.send_request("/crash")
        self.connection.read_response()

        sleep(0.05)

        assert f"[{REQUEST_ID}] Elapsed: " in self.caplog.text

    def test_log_elapsed_after_disconnect(self):
        self.connection.send_request("/slow_loris")
        self.connection.disconnect()

        sleep(0.2)

        assert f"[{REQUEST_ID}] Elapsed: " in self.caplog.text


class OutOfBandResponseWithSubprocessTest(TestCase):
    def setUp(self):
        broker = DummyBroker()
        self.on_done = MagicMock()

        self.server = Server(
            ("", 0),
            demo_app,
            load_balancer=mock_balancer([broker.addr()]),
            redirect_port=0,
            use_request_subprocess=True,
            oob_cleanup_interval_seconds=OOB_CLEANUP_INTERVAL_SECONDS,
            oob_item_expiry_seconds=OOB_ITEM_EXPIRY_SECONDS,
        )
        Thread(
            target=self.server._fetch_and_run_one_job,
            kwargs={
                "addr": broker.addr(),
            },
            daemon=True,
        ).start()
        self.connection = broker.accept(0.1)
        self.request_id = str(uuid4())

    def tearDown(self):
        self.server.shutdown()

    def test_abandoned_request_is_aborted_before_responding(self):
        self.connection.send_request(
            "/hang_forever",
            {"yield": False, "start-response": False, "x-request-id": self.request_id},
        )
        wait_for(lambda: worker_running(self.request_id))

        self.connection.disconnect()
        wait_for(lambda: not worker_running(self.request_id), timeout=2)

    def test_abandoned_request_is_aborted_when_oob_not_requested(self):
        self.connection.send_request(
            "/hang_forever",
            {"yield": False, "start-response": True, "x-request-id": self.request_id},
        )
        status, _headers = self.connection.parse_response()
        assert status == 303

        # We never connect to read the response. Request should
        # be aborted after OOB_CLEANUP_INTERVAL_SECONDS and
        # OOB_ITEM_EXPIRY_SECONDS
        wait_for(
            lambda: not worker_running(self.request_id),
            timeout=1 + OOB_CLEANUP_INTERVAL_SECONDS + OOB_ITEM_EXPIRY_SECONDS,
        )

    def test_abandoned_request_is_aborted_after_started_response(self):
        self.connection.send_request(
            "/hang_forever",
            {"yield": False, "start-response": True, "x-request-id": self.request_id},
        )
        status, headers = self.connection.parse_response()
        assert status == 303
        with urlopen(headers.get("location")):
            pass

        # We connected, but abandoned the response before reading. Request should be aborted momentarily
        wait_for(lambda: not worker_running(self.request_id), timeout=2)


class TestShutdown(TestCase):
    DELAY_START_RESPONSE = 0.3
    DELAY_FINISH_RESPONSE = 0.8

    @fixture(autouse=True)
    def use_caplog(self, caplog):
        caplog.set_level(INFO)
        self.caplog = caplog

    def setUp(self):
        broker = DummyBroker()
        self.callbacks = MagicMock()

        def app(environ, start_response):
            sleep(self.DELAY_START_RESPONSE)
            start_response("200 OK", {})
            yield b" "
            sleep(self.DELAY_FINISH_RESPONSE)
            yield b"done"

        app.wait_for_slot = WaitForFirstSlot(self.callbacks)

        self.server = Server(
            ("", 0),
            app,
            load_balancer=mock_balancer([broker.addr()]),
            redirect_port=0,
            oob_cleanup_interval_seconds=OOB_CLEANUP_INTERVAL_SECONDS,
            oob_item_expiry_seconds=OOB_ITEM_EXPIRY_SECONDS,
        )
        Thread(target=self.server.poll_loop, daemon=True).start()
        self.connection = broker.accept(0.1)

    def test_ptth_finish_before_shutdown(self):
        self.connection.send_request()
        Thread(target=self.connection.read_response).start()
        self.assertGreaterEqual(
            self.shutdown_time(), OOB_ITEM_EXPIRY_SECONDS + self.DELAY_START_RESPONSE
        )
        assert f"Draining ongoing requests: {REQUEST_ID}" in self.caplog.text

    def test_pending_oob_expire_before_shutdown(self):
        self.connection.send_request()
        self.connection.read_response()
        st = self.shutdown_time()
        self.assertGreaterEqual(st, OOB_ITEM_EXPIRY_SECONDS)
        self.assertLessEqual(st, self.DELAY_FINISH_RESPONSE)
        assert f"Draining pending redirects: {REQUEST_ID}" in self.caplog.text

    def test_oob_finish_before_shutdown(self):
        self.connection.send_request()
        status, headers = self.connection.parse_response()
        assert status == 303

        with urlopen(headers.get("location")) as real_response:
            assert real_response.status == 200

            # Still running the request, we expect it to be finished before shutdown
            self.assertGreaterEqual(self.shutdown_time(), self.DELAY_FINISH_RESPONSE)

            assert f"Draining ongoing requests: {REQUEST_ID}" in self.caplog.text

    def shutdown_time(self):
        start = monotonic()
        self.server.shutdown()
        return monotonic() - start
