#!/usr/bin/env python

"""Tests for `otel-cli` package."""

from otel_cli import otel


def test_create_counter():
    """Test create_counter"""
    test_counter = otel.create_counter(
        "test-counter",
        value=1,
        attributes={"test-attribute": "foo"},
        unit="test-unit",
        description="test description",
        service_name="test-service-name",
        service_version="0.0.1",
    )
    assert test_counter.name == "test-counter"
    assert test_counter.description == "test description"
    assert test_counter.unit == "test-unit"
