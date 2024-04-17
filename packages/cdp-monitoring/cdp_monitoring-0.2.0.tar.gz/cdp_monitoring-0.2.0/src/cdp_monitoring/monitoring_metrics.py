from timeit import default_timer
from prometheus_client import Counter, Gauge
from prometheus_client.context_managers import Timer as BaseTimer
from prometheus_client.metrics import Histogram as BaseHistogram


class Timer(BaseTimer):
    def __init__(self, metric, callback_name, *args, **kwargs):
        super().__init__(metric, callback_name)
        self._callback_args = args
        self._callback_kwargs = kwargs

    def __exit__(self, typ, value, traceback):
        duration = max(default_timer() - self._start, 0)
        callback = getattr(self._metric, self._callback_name)
        callback(duration, *self._callback_args, **self._callback_kwargs)


class Histogram(BaseHistogram):
    def time(self, *args, **kwargs):
        return Timer(self, "observe", *args, **kwargs)


INFO = Gauge("fastapi_app_info", "FastAPI application information.", ["app_name"])
REQUESTS = Counter(
    "fastapi_requests_total",
    "Total count of requests by method and path.",
    ["method", "path", "app_name"],
)
RESPONSES = Counter(
    "fastapi_responses_total",
    "Total count of responses by method, path and status codes.",
    ["method", "path", "status_code", "app_name"],
)
REQUESTS_PROCESSING_TIME = Histogram(
    "fastapi_requests_duration_seconds",
    "Histogram of requests processing time by path (in seconds)",
    ["method", "path", "app_name"],
)
EXCEPTIONS = Counter(
    "fastapi_exceptions_total",
    "Total count of exceptions raised by path and exception type",
    ["method", "path", "exception_type", "app_name"],
)


__all__ = [
    "INFO",
    "REQUESTS",
    "RESPONSES",
    "REQUESTS_PROCESSING_TIME",
    "EXCEPTIONS",
]
