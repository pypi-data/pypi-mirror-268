from typing import List

from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.trace import TracerProvider
from starlette.requests import Request
from starlette.routing import Match
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from starlette.types import Message, Receive, Scope, Send
from . import monitoring_metrics as metrics


class MonitoringMiddleware:
    def __init__(
        self,
        app,
        app_name: str = "fastapi-app",
        tracer: TracerProvider = None,
        exclude_paths: List = None,
    ):
        self.app = app
        self.app_name = app_name
        self.tracer = trace.get_tracer("cdp-monitoring", tracer_provider=tracer)
        self.exclude_paths = exclude_paths or []

        metrics.INFO.labels(app_name=self.app_name).inc()

    @staticmethod
    def _get_endpoint(request: Request):
        for route in request.app.routes:
            match, child_scope = route.matches(request.scope)
            if match == Match.FULL:
                return True, route.endpoint

        return False, None

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        if scope["path"] in self.exclude_paths:
            return await self.app(scope, receive, send)

        request = Request(scope, receive=receive)

        is_handled_path, endpoint = self._get_endpoint(request)
        if not is_handled_path:
            return await self.app(scope, receive, send)

        async def receive_wrapper() -> Message:
            parent_span = trace.get_current_span()

            with self.tracer.start_as_current_span("http.request") as span:
                message = await receive()

                if message["type"] == "http.request":
                    request_body = message["body"].decode("utf-8")
                    parent_span.set_attribute("request.body", request_body)
                    span.set_attribute("request.body", request_body)

                return message

        async def send_wrapper(message: Message) -> None:
            parent_span = trace.get_current_span()

            if message["type"] == "http.response.start":
                parent_span.set_attribute("response.status_code", message["status"])
                parent_span.set_attribute("response.headers", str(message["headers"]))

                with self.tracer.start_as_current_span("http.response.start") as span:
                    span.set_attribute("response.status_code", message["status"])
                    span.set_attribute("response.headers", str(message["headers"]))

                    await send(message)

                    metrics.RESPONSES.labels(
                        method=scope["method"],
                        path=scope["path"],
                        status_code=message["status"],
                        app_name=self.app_name,
                    ).inc()

            if message["type"] == "http.response.body":
                parent_span.set_attribute("response.body", message["body"])

                with self.tracer.start_as_current_span("http.response.body") as span:
                    span.set_attribute("response.body", message["body"])

                    await send(message)

        metrics.REQUESTS.labels(
            method=scope["method"], path=scope["path"], app_name=self.app_name
        ).inc()

        with self.tracer.start_as_current_span(
            f"{scope['method']} {scope['path']}"
        ) as span:
            try:
                trace_id = trace.format_trace_id(span.get_span_context().trace_id)

                span.set_attribute("protocol", str(scope["type"]))
                span.set_attribute("http_version", str(scope["http_version"]))
                span.set_attribute("server.host", str(scope["server"][0]))
                span.set_attribute("server.port", str(scope["server"][1]))
                span.set_attribute("client.host", str(scope["client"][0]))
                span.set_attribute("client.port", str(scope["client"][1]))
                span.set_attribute("request.headers", str(scope["headers"]))
                span.set_attribute("request.query_string", str(scope["query_string"]))

                with metrics.REQUESTS_PROCESSING_TIME.labels(
                    method=scope["method"],
                    path=scope["path"],
                    app_name=self.app_name,
                ).time(exemplar={"TraceID": trace_id}):
                    with self.tracer.start_as_current_span(endpoint.__name__) as span:
                        await self.app(scope, receive_wrapper, send_wrapper)

            except Exception as e:
                metrics.EXCEPTIONS.labels(
                    method=scope["method"],
                    path=scope["path"],
                    exception_type=type(e).__name__,
                    app_name=self.app_name,
                ).inc()

                metrics.RESPONSES.labels(
                    method=scope["method"],
                    path=scope["path"],
                    status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                    app_name=self.app_name,
                ).inc()

                span.set_status(Status(StatusCode.ERROR))
                span.record_exception(e)
                raise e from None
