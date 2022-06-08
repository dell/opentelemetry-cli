#!/usr/bin/env python

"""Tests for `otel-cli` package."""

from opentelemetry.trace import SpanKind

from otel_cli import otel


def test_create_span():
    """Test create_span"""
    sample_trace_id = "f00df00d7e1d4947bd4ba6551cdaaf63"
    sample_span_id = "baff0450bf417425"
    sample_start_time = 1654087297682580181
    sample_end_time = 1654087304700987616
    test_span = otel.create_span(
        "test-span-name",
        service_name="test-service-name",
        service_version="0.0.1",
        kind="server",
        trace_id=sample_trace_id,
        span_id=sample_span_id,
        start_time=sample_start_time,
        end_time=sample_end_time,
    )
    assert test_span.name == "test-span-name"
    assert test_span.kind == SpanKind.SERVER
    assert test_span.resource.attributes.get("service.name") == "test-service-name"
    assert test_span.resource.attributes.get("service.version") == "0.0.1"
    assert f"{test_span.context.trace_id:x}" == sample_trace_id
    assert f"{test_span.context.span_id:x}" == sample_span_id
    assert test_span.start_time == sample_start_time
    assert test_span.end_time == sample_end_time


def test_create_span_with_traceparent():
    """Test create_span with a traceparent provided"""
    sample_span_id = "baff0450bf417425"
    test_span = otel.create_span(
        "test-span-name",
        service_name="test-service-name",
        service_version="0.0.1",
        kind="internal",
        span_id=sample_span_id,
        traceparent="00-0af7651916cd43dd8448eb211c80319c-00f067aa0ba902b7-01",
    )
    assert test_span.name == "test-span-name"
