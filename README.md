# otel-client-python: human-friendly OpenTelemetry CLI

Provides a CLI for crafting and sending telemetry data over OTLP (OpenTelemetry Line Protocol).

## Requirements

## Installation

There are several ways of running this CLI.

### Docker

```sh
docker pull afeoscyc-mw.cec.lab.emc.com/otel-cli-python:<version>
```

You can specify a version like `0.0.1` or use `latest` to get the most up-to-date version.

Run latest version of the CLI in a container:

```sh
# set OTEL_EXPORTER_OTLP_ENDPOINT to your OTel collector instance
export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4317
docker run --rm -e OTEL_EXPORTER_OTLP_ENDPOINT afeoscyc-mw.cec.lab.emc.com/otel-cli-python:latest --help
```

Replace `--help` with any `otel` command, without `otel` itself.

### PyPI

TBD

## Usage

First, define `OTEL_EXPORTER_OTLP_ENDPOINT` in your shell and set it to the OTLP collector instance you want to use.
For a local collector, set this to `http://127.0.0.1:4317` like so:

```sh
export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4317
```

### Spans

To send a span, run:

```sh
otel span "span name"
```

To set a different service name, use the `--service` flag:

```sh
otel span --service "My Service" "span name"
```

You can also pass custom start and end dates. These should be *nanoseconds* since the epoch:

```sh
SPAN_START_DATE=$(date --date "2 minutes ago" +%s%N)
SPAN_END_DATE=$(date +%s%N)
otel span --start "$SPAN_START_DATE" --end "$SPAN_END_DATE" "span name"
```

By default, spans are reported with a status of `UNKNOWN`. To pass a different status, use the `--status` option:

```sh
otel span --status OK "successful span"
otel span --status ERROR "failed span"
```

To add attributes to spans, use the `--attribute|-a` option. It accepts attributes in a `key=value` format. Use multiple instances of this option to send multiple attributes.

```sh
otel span -a "my.foo=bar" -a "my.bar=baz" "span name"
```

otel will create a random trace ID and span ID. You can override those:

```sh
otel span --trace-id "4d999706756fd1859345f8dc6d0af218" --span-id "ac2a3b2b19ac602d"
```

#### Sending multiple spans in a trace

To create a single trace with one root span and multiple child spans, we first need to generate a trace ID for the entire trace and a span ID for the parent span. Use `otel generate` to create those:

```sh
TRACE_ID=$(otel generate trace_id)
PARENT_SPAN=$(otel generate span_id)
```

Then, when creating children span, we pass this information in the format of a `TRACEPARENT`:

```sh
TRACEPARENT="00-${TRACE_ID}-${PARENT_SPAN}-01"
otel span --traceparent "$TRACEPARENT" "Child A Name"
otel span --traceparent "$TRACEPARENT" "Child B Name"
```

Finally, send the parent span using the pre-generated IDs:

```sh
otel span --trace-id "$TRACE_ID" --span-id "$PARENT_SPAN" "Parent Span Name"
```

### Metrics

Use `otel metric` to send metric data. The following metric types are currently supported:

- Counter
- UpDownCounter

#### Counter

Counters are metrics that can count only up.
By specifying just the counter name, it will be incremented by 1:

```sh
otel metric counter my-counter
```

You can specify a different value to increase by. For example, this will increase the counter by 1024:

```sh
otel metric counter total-bytes 1024
```

Counters support attributes just like spans, using the `-a|--attribute` option.

```sh
otel metric counter my-counter -a "host.name=localhost"
```

By default, attributes are strings. You can set them to other types by using one of the following prefixes:

- `int:` - value will be converted to an integer.
- `float:` - value will be converted to a floating point number.
- `bool:` - value will be converted to a boolean.
  - Values of `y`, `yes`, `t`, `true`, `on`, and `1` are converted to `True`.
  - Values of `n`, `no`, `f`, `false`, `off`, and `0` are converted to `False`.
  - Values are __not__ case-sensitive.

Example:

```sh
otel metric counter my-counter \
    -a "key1=just a string" \
    -a "int:key2=10" \
    -a "float:key3=3.14" \
    -a "bool:key4=YES"
```

#### UpDownCounter

UpDownCounters are metrics that count up or down.
If not given a value, the UpDownCounter will increment by one:

```sh
otel metric updown queue-length
```

You can specify a different value to increase by. For example, this will increase the counter by 1024:

```sh
otel metric updown my-updowncounter 1024
```

To decrease the counter number, pass a negative number like so:

```sh
otel metric updown queue-length -1
```

## Packaging
This project uses [poetry](https://python-poetry.org/) to manage dependencies, build, etc.
