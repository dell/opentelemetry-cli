from . import __version__

from typing import Optional, Literal, Mapping
from time import time_ns
from opentelemetry import trace
from opentelemetry.sdk.trace import Span
from opentelemetry.trace import SpanKind
from opentelemetry.context import Context
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace.status import Status, StatusCode
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk._metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc._metric_exporter import OTLPMetricExporter


def create_span(
    span_name: str,
    service_name: str = "otel-cli-python",
    service_version: str = "0.0.1",
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
    trace_id: Optional[str] = None,
    span_id: Optional[str] = None,
    kind: Literal["client", "consumer", "internal", "producer", "server"] = "internal",
    traceparent: Optional[str] = None,
    attributes: Mapping[str, str] = None,
    status_code: Literal["UNSET", "OK", "ERROR"] = "UNSET",
    status_message: Optional[str] = None,
) -> Span:
    resource = Resource.create(
        attributes={
            "service.name": service_name,
            "service.version": service_version,
        }
    )
    provider = TracerProvider(resource=resource)
    otlp_exporter = OTLPSpanExporter()
    provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    tracer = trace.get_tracer("otel-cli-python", __version__, tracer_provider=provider)

    if trace_id is not None:
        tracer.id_generator.generate_trace_id = lambda: int(trace_id, 16)

    if span_id is not None:
        tracer.id_generator.generate_span_id = lambda: int(span_id, 16)

    if start_time is None:
        start_time = time_ns()

    if end_time is None:
        end_time = time_ns()

    # Create a new context to avoid reusing context created by pytest
    context = Context()
    if traceparent is not None:
        carrier = {"traceparent": traceparent}
        context = TraceContextTextMapPropagator().extract(carrier)

    span_kind = SpanKind[kind.upper()]
    statuscode = StatusCode[status_code]
    span_status = Status(statuscode, description=status_message)
    my_span = tracer.start_span(
        span_name,
        start_time=start_time,
        kind=span_kind,
        context=context,
        attributes=attributes,
    )
    my_span._status = span_status
    my_span.end(end_time=end_time)
    return my_span


def create_counter(
    counter_name: str,
    value: int,
    unit: str = "",
    description: str = "",
    attributes: Mapping[str, str] = None,
    service_name: str = "otel-cli-python",
    service_version: str = "0.0.1",
):
    resource = Resource.create(
        attributes={
            "service.name": service_name,
            "service.version": service_version,
        }
    )
    exporter = OTLPMetricExporter()
    reader = PeriodicExportingMetricReader(exporter)
    provider = MeterProvider(metric_readers=[reader], resource=resource)
    meter = provider.get_meter("otel-cli-python", __version__)
    counter = meter.create_counter(
        name=counter_name, unit=unit, description=description
    )
    counter.add(amount=value, attributes=attributes)
    return counter
