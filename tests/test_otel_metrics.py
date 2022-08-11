#!/usr/bin/env python

"""Tests for `otel-cli` package."""

import pytest

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


def test_create_normal_counter():
    """Test create_counter with a counter_type of CounterType.NORMAL"""
    test_counter = otel.create_counter(
        "test-counter",
        value=1,
        counter_type=otel.CounterTypes.NORMAL,
        attributes={"test-attribute": "foo"},
        unit="test-unit",
        description="test description",
        service_name="test-service-name",
        service_version="0.0.1",
    )
    assert test_counter.name == "test-counter"
    assert test_counter.description == "test description"
    assert test_counter.unit == "test-unit"


def test_create_updown_counter():
    """Test create_counter with a counter_type of CounterType.UPDOWN"""
    test_counter = otel.create_counter(
        "test-counter",
        value=1,
        counter_type=otel.CounterTypes.UPDOWN,
        attributes={"test-attribute": "foo"},
        unit="test-unit",
        description="test description",
        service_name="test-service-name",
        service_version="0.0.1",
    )
    assert test_counter.name == "test-counter"
    assert test_counter.description == "test description"
    assert test_counter.unit == "test-unit"


def test_create_counter_invalid_type():
    with pytest.raises(ValueError):
        otel.create_counter("test-invalid-counter", value=1, counter_type="invalid")
