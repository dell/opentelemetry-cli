"""Console script for otel_python_cli."""
import sys
import click

from opentelemetry.sdk.trace.id_generator import RandomIdGenerator


@click.group()
def main(args=None):
    pass


@main.group()
def generate():
    pass


@generate.command(name="trace_id")
@click.option("-d", "--decimal", is_flag=True, default=False, help="Print in decimal base")
def generate_trace_id(decimal):
    trace_id = RandomIdGenerator().generate_trace_id()
    if decimal:
        click.echo(trace_id)
    else:
        click.echo(f"{trace_id:x}")


@generate.command(name="span_id")
@click.option("-d", "--decimal", is_flag=True, default=False, help="Print in decimal base")
def generate_span_id(decimal):
    span_id = RandomIdGenerator().generate_span_id()
    if decimal:
        click.echo(span_id)
    else:
        click.echo(f"{span_id:x}")


@main.command()
def span():
    pass


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
