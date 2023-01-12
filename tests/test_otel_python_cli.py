#!/usr/bin/env python

"""Tests for `otel-cli` package."""

import pytest
import json

from click.testing import CliRunner

from otel_cli import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output


def test_generate_trace_id():
    """Test generating trace ID"""
    runner = CliRunner()
    result = runner.invoke(cli.generate_trace_id)
    assert result.exit_code == 0
    assert int(result.output.strip(), 16)
    decimal_result = runner.invoke(cli.generate_trace_id, ["-d"])
    assert decimal_result.exit_code == 0
    assert decimal_result.output.strip().isdigit()


def test_generate_span_id():
    """Test generating span ID"""
    runner = CliRunner()
    result = runner.invoke(cli.generate_span_id)
    assert result.exit_code == 0
    assert int(result.output.strip(), 16)
    decimal_result = runner.invoke(cli.generate_span_id, ["-d"])
    assert decimal_result.exit_code == 0
    assert decimal_result.output.strip().isdigit()


def test_send_span():
    """Test sending a span"""
    runner = CliRunner()
    result = runner.invoke(cli.span, args=["my-span", "-v"])
    assert result.exit_code == 0
    span_data = json.loads(result.output)
    assert span_data is not None


def test_send_counter():
    """Test sending a counter"""
    runner = CliRunner()
    result = runner.invoke(cli.main, args=["metric", "counter", "my-counter"])
    assert result.exit_code == 0


def test_send_counter_multiple_attributes():
    """Test sending a counter with multiple attributes"""
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        args=[
            "metric",
            "counter",
            "my-counter",
            "-a",
            "test.foo=1",
            "-a",
            "test.bar=baz",
        ],
    )
    assert result.exit_code == 0


def test_send_updown_counter():
    """Test sending an updown counter"""
    runner = CliRunner()
    result = runner.invoke(cli.main, args=["metric", "updown", "my-counter"])
    assert result.exit_code == 0


def test_send_updown_counter_negative():
    """Test sending an updown counter with a negative value"""
    runner = CliRunner()
    result = runner.invoke(cli.main, args=["metric", "updown", "my-counter", "-1"])
    assert result.exit_code == 0


def test_send_counter_attribute_file(tmp_path):
    """Test sending a counter with multiple attributes from a file"""
    attribute_content = "\n".join(("test.foo=1", "test.bar=baz"))
    attribute_file = tmp_path / "attributes.lst"
    attribute_file.write_text(attribute_content)
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        args=[
            "metric",
            "counter",
            "my-counter",
            "-A",
            str(attribute_file),
        ],
    )
    assert result.exit_code == 0


def test_send_counter_attribute_file_and_cmdline(tmp_path):
    """
    Test sending a counter with multiple attributes from a file, in addition to
    attributes provided in the command line.
    """
    attribute_content = "\n".join(("test.foo=1", "test.bar=baz"))
    attribute_file = tmp_path / "attributes.lst"
    attribute_file.write_text(attribute_content)
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        args=[
            "metric",
            "counter",
            "my-counter",
            "-A",
            str(attribute_file),
            "-a",
            "test.foo=2",
        ],
    )
    assert result.exit_code == 0
