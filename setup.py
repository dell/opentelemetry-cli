#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "opentelemetry-proto>=1.11.1",
    "opentelemetry-sdk>=1.11.1",
    "opentelemetry-exporter-otlp>=1.11.1",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Moshi Binyamini",
    author_email="moshi.binyamini@dell.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="CLI for OpenTelemetry Traces and Metrics in Python",
    entry_points={
        "console_scripts": [
            "otel-cli=otel_cli.cli:main",
        ],
    },
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="otel-cli",
    name="otel-cli",
    packages=find_packages(include=["otel_cli", "otel_cli.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://eos2git.cec.lab.emc.com/binyam/otel-client-python",
    version="0.1.0",
    zip_safe=False,
)
