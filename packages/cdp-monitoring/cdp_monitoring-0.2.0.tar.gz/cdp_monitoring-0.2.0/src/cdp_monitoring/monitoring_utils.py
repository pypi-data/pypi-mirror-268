import os
import logging
from typing import List
from datetime import datetime

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from prometheus_client import REGISTRY, CollectorRegistry
from prometheus_client.multiprocess import MultiProcessCollector
from prometheus_client.openmetrics.exposition import (
    CONTENT_TYPE_LATEST,
    generate_latest,
)
from starlette.responses import Response
from .monitoring_middleware import MonitoringMiddleware

logger = logging.getLogger(__name__)


def metrics(request):
    # multiprocessing 환경일 때 필수
    if "PROMETHEUS_MULTIPROC_DIR" in os.environ:
        registry = CollectorRegistry()
        MultiProcessCollector(registry)

        return Response(
            generate_latest(registry), headers={"Content-Type": CONTENT_TYPE_LATEST}
        )

    return Response(
        generate_latest(REGISTRY), headers={"Content-Type": CONTENT_TYPE_LATEST}
    )


def init_monitoring(app: FastAPI, version: str = None, exclude_paths: List[str] = None):
    """
    fast api app 에 프로메테우스 모니터링 및 오픈텔레메트리 트레이싱을 적용
    :param app:
    :param version: application 의 버전 (없으면 현재 시간을 prometheus app_name 으로 사용)
    :param exclude_paths: 모니터링을 적용하지 않을 path
    :return:
    """
    endpoint = os.environ.get("TEMPO_URL", None)
    if endpoint is None:
        logger.info("TEMPO_URL is not set. Not available now")
        return None

    if version is None:
        # version 이 주어지지 않으면 앱 실행 시간을 postfix 로 사용
        now = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        app_name = f'{app.title}-{now}'
    else:
        app_name = f'{app.title}-{version}'

    resource = Resource.create(
        attributes={"service.name": app_name, "compose_service": app_name}
    )

    tracer = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer)
    tracer.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))

    app.add_middleware(
        MonitoringMiddleware,
        app_name=app_name,
        tracer=tracer,
        exclude_paths=exclude_paths,
    )
    app.add_route("/metrics", metrics)
