"""Console script for otel_python_cli."""
import sys
import click

from opentelemetry.sdk.trace.id_generator import RandomIdGenerator

from .otel import create_span


@click.group()
def main(args=None):
    pass  # pragma: no cover


@main.group()
def generate():
    pass  # pragma: no cover


@generate.command(name="trace_id")
@click.option(
    "-d", "--decimal", is_flag=True, default=False, help="Print in decimal base"
)
def generate_trace_id(decimal):
    trace_id = RandomIdGenerator().generate_trace_id()
    if decimal:
        click.echo(trace_id)
    else:
        click.echo(f"{trace_id:x}")


@generate.command(name="span_id")
@click.option(
    "-d", "--decimal", is_flag=True, default=False, help="Print in decimal base"
)
def generate_span_id(decimal):
    span_id = RandomIdGenerator().generate_span_id()
    if decimal:
        click.echo(span_id)
    else:
        click.echo(f"{span_id:x}")


@main.command()
@click.argument("span_name")
@click.option("-s", "--service", default="otel-cli-python")
@click.option(
    "--start", type=int, help="Span start time in nanoseconds since the epoch"
)
@click.option("--end", type=int, help="Span end time in nanoseconds since the epoch")
@click.option(
    "-v", "--verbose", is_flag=True, default=False, help="Print spans to stdout"
)
@click.option("--tp", "--traceparent", help="Trace parent")
@click.option("--span-id", help="Manually set span ID")
@click.option("--trace-id", help="Manually set trace ID")
def span(span_name, service, start, end, verbose, tp, span_id, trace_id):
    myspan = create_span(
        span_name,
        service_name=service,
        start_time=start,
        end_time=end,
        traceparent=tp,
        span_id=span_id,
        trace_id=trace_id,
    )
    if verbose:
        print(myspan.to_json())


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
