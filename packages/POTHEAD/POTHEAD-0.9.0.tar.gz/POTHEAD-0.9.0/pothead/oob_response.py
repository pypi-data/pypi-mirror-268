from logging import getLogger
from os import environ, urandom
from threading import Lock, Thread, Timer
from time import monotonic, sleep
from typing import (
    Dict,
    Generator,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    Generic,
    TypeVar,
    Callable,
)
from warnings import warn

from werkzeug.serving import make_server

from .wsgi_typing import (
    Environ,
    ExcInfo,
    ResponseStream,
    StartResponse,
    WsgiApplication,
)
from .util import SocketCheckingWSGIHandler, JobTracker

# Interval of how often to attempt cleanup of unclaimed jobs
CLEANUP_INTERVAL_SECONDS = float(environ.get("OOB_CLEANUP_INTERVAL_SECONDS", "5"))

# Maximum time a process is allowed to remain unclaimed before attempting to clean it up
ITEM_EXPIRY_SECONDS = float(environ.get("OOB_ITEM_EXPIRY_SECONDS", "20"))

LOGGER = getLogger("pothead.oob_response")


class Response:
    def __init__(self, request_id, headers, body, on_done):
        self.request_id = request_id
        self.headers = headers
        self.body = body
        self.on_done = on_done

    def close(self):
        if self.on_done:
            self.body.close()
            self.on_done()
            self.on_done = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.close()


class KeyedTransfer:
    """Allows one thread to push a value, and get a (url-safe string) key back.
    At a later time, another thread can retrieve the value by the key.

    With regular intervals, unclaimed keys are purged. If the value has a method
    `close()`, it is called on purging."""

    def __init__(self, cleanup_interval_seconds: float, item_expiry_seconds: float):
        self._cleanup_interval_seconds = cleanup_interval_seconds
        self._item_expiry_seconds = item_expiry_seconds
        self._dict: Dict[str, Tuple[float, Response]] = dict()
        self._lock = Lock()
        self._shutdown = False

        self._cleanup()

    def push(self, value: Response):
        key = urandom(24).hex()
        now = monotonic()
        expires_at = now + self._item_expiry_seconds
        with self._lock:
            assert key not in self._dict
            self._dict[key] = (expires_at, value)

        return key

    def pop(self, key) -> Optional[Response]:
        with self._lock:
            return self._dict.pop(key, (None, None))[1]

    def close(self):
        self._shutdown = True
        with self._lock:
            for expires_at, job in self._dict.values():
                if hasattr(job, "close"):
                    job.close()
            self._dict.clear()

    def wait_for_clear(self):
        while True:
            with self._lock:
                if len(self._dict) == 0:
                    return
            sleep(self._cleanup_interval_seconds / 2)

    def requests(self) -> List[str]:
        with self._lock:
            return [job.request_id for expires_at, job in self._dict.values()]

    def _cleanup(self):
        if not self._shutdown:
            t = Timer(self._cleanup_interval_seconds, self._cleanup)
            t.daemon = True
            t.start()
        now = monotonic()
        with self._lock:
            new_dict = dict()
            for key, (expires_at, job) in self._dict.items():
                if expires_at > now:
                    new_dict[key] = (expires_at, job)
                elif hasattr(job, "close"):
                    job.close()
            self._dict = new_dict


AtomicReferenceT = TypeVar("AtomicReferenceT")


class AtomicReference(Generic[AtomicReferenceT]):
    def __init__(self):
        self._lock = Lock()

    def is_set(self) -> bool:
        with self._lock:
            return hasattr(self, "data")

    def set(self, data: AtomicReferenceT) -> None:
        with self._lock:
            self.data = data

    def get(self) -> AtomicReferenceT:
        with self._lock:
            return self.data


def take_until(
    iterable: Iterable[bytes], condition: Callable[[], bool]
) -> Generator[bytes, None, Iterator[bytes]]:
    """Yields chunks until the first one after which condition is true. That chunk, and all the remaining chunks, are
    returned via generator-return, as a new generator"""

    iterator = iter(iterable)

    def trimmed_generator(first_value):
        yield first_value
        yield from iterator

    for chunk in iterator:
        if condition():
            return trimmed_generator(chunk)
        else:
            yield chunk

    return iter(())


class OutOfBandResponder:
    def __init__(
        self,
        wrapped_app: WsgiApplication,
        port=0,
        cleanup_interval_seconds: Optional[float] = None,
        item_expiry_seconds: Optional[float] = None,
    ):
        if cleanup_interval_seconds is None:
            cleanup_interval_seconds = CLEANUP_INTERVAL_SECONDS
        if item_expiry_seconds is None:
            item_expiry_seconds = ITEM_EXPIRY_SECONDS

        self._job_transfer = KeyedTransfer(
            cleanup_interval_seconds, item_expiry_seconds
        )
        self.wrapped_app = wrapped_app

        wsgi_app = self._content_response_wsgi
        self._server = make_server(
            "0.0.0.0",
            port=port,
            app=wsgi_app,
            threaded=True,
            request_handler=SocketCheckingWSGIHandler,
        )
        responder_service = Thread(target=self._server.serve_forever)
        responder_service.daemon = True
        responder_service.start()
        self._worker_tracker = JobTracker()
        self._service_port = self._server.port

    def ongoing_requests(self) -> List[str]:
        return self._worker_tracker.ongoing_requests()

    def _content_response_wsgi(self, environ, start_response):
        path = environ["PATH_INFO"]
        if len(path) < 2 or path[0] != "/":
            start_response("404 Not Found", {})
            return []

        with self._worker_tracker.scope("<pending>") as work_scope:
            response_key = path[1:]
            response = self._job_transfer.pop(response_key)
            if response is None:
                start_response(
                    f"410 {response_key} is claimed, expired, or never registered", {}
                )
                return []

            work_scope.update(response.request_id)
            with response:
                start_response(
                    "200 OK",
                    response.headers,
                )
                yield b""  # Flush response to client
                for chunk in response.body:
                    yield chunk

    def shutdown(self):
        request_ids = self._job_transfer.requests()
        LOGGER.info(
            f"Draining pending redirects: {','.join(request_ids)}",
            extra={"requests": request_ids},
        )
        self._job_transfer.wait_for_clear()
        self._server.shutdown()
        LOGGER.info("Waiting for jobs to complete")
        self._worker_tracker.drain(LOGGER)
        LOGGER.info("Shutdown complete")

    def inspect(self):
        yield "OOB responses waiting:\n".encode()
        for request_id in self._job_transfer.requests():
            yield f"  {request_id}\n".encode()
        yield "OOB responses ongoing:\n".encode()
        for request_id in self._worker_tracker.ongoing_requests():
            yield f"  {request_id}\n".encode()

    def __call__(
        self,
        environ: Environ,
        start_response: StartResponse,
        assume_cleanup: Callable[[], Callable[[], None]],
    ) -> ResponseStream:
        start_response_called: AtomicReference[
            Tuple[str, Sequence[Tuple[str, str]], Optional[ExcInfo]]
        ] = AtomicReference()

        def my_start_response(
            status: str,
            headers: Sequence[Tuple[str, str]],
            exc_info: Optional[ExcInfo] = None,
        ):
            if start_response_called.is_set():
                warn("start_response called more than once")
            else:
                start_response_called.set((status, headers, exc_info))

        response_chunks = yield from take_until(
            self.wrapped_app(environ, my_start_response), start_response_called.is_set
        )
        if not start_response_called:
            msg = "Application Terminated Without Response"
            LOGGER.error(msg)
            return

        (status, headers, exc_info) = start_response_called.get()
        if not exc_info and status.startswith("200 "):
            on_done = assume_cleanup()
            request_id = environ.get("REQUEST_ID", "<unknown>")
            key = self._job_transfer.push(
                Response(request_id, headers, response_chunks, on_done)
            )
            start_response(
                "303 See Other",
                (
                    (
                        "Location",
                        f"http://{environ['SERVER_NAME']}:{self._service_port}/{key}",
                    ),
                ),
                None,
            )
        else:
            start_response(status, headers, exc_info)
            yield from response_chunks
