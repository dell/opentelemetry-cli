#!/usr/bin/env python

"""Tests for `otel-cli.utils` module."""

import pytest
from otel_cli import utils


def test_remove_prefix(monkeypatch):
    """Test utils.remove_prefix"""
    assert utils.remove_prefix("int:test", "int:") == "test"
    assert utils.remove_prefix("float:test", "float:") == "test"
    assert utils.remove_prefix("noprefix", "bool:") == "noprefix"


def test_parse_attributes():
    attributes = utils.parse_attributes(
        [
            "key1=value",
            "int:key2=100",
            "float:key3=0.1",
            "bool:key4=yes",
            "bool:key5=0",
            "str:key6=hello",
        ]
    )
    assert attributes["key1"] == "value"
    assert type(attributes["key2"]) is int
    assert attributes["key2"] == 100
    assert type(attributes["key3"]) is float
    assert attributes["key3"] == 0.1
    assert type(attributes["key4"]) is bool
    assert type(attributes["key5"]) is bool
    assert attributes["key4"] is True
    assert attributes["key5"] is False
    assert attributes["key6"] == "hello"

    with pytest.raises(ValueError):
        utils.parse_attributes(["int:key=NotANumber"])

    with pytest.raises(ValueError):
        utils.parse_attributes(["bool:key=NotABool"])
