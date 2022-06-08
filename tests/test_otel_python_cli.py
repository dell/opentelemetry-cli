#!/usr/bin/env python

"""Tests for `otel-cli` package."""

import pytest
import json

from click.testing import CliRunner

from otel_cli import otel
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
    assert "--help  Show this message and exit." in help_result.output


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
