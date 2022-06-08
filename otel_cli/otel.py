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

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


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
    my_span = tracer.start_span(
        span_name,
        start_time=start_time,
        kind=span_kind,
        context=context,
        attributes=attributes,
    )
    my_span.end(end_time=end_time)
    return my_span
