# Home

OpenTelemetry-CLI is a shell utility to craft and send telemetry data in OpenTelemetry Line Protocol (OTLP) format.

## Features

- Craft custom **traces** and **spans**
- Send **metrics** such as **Counter**, **UpDownCounter**
- Send to either **gRPC** or **HTTP** OTLP receivers
- Add rich **attributes** to telemetry signals
- Generate **trace IDs** and **span IDs**

## Quickstart

### Setup

To install OpenTelemetry-CLI, run the following command in your terminal:

```sh
$ pip install otel-cli
```

See the [Installation](installation.md) section of the documentation for more options.

Point OTEL_EXPORTER_OTLP_ENDPOINT at a collector instance

```sh
$ export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

### Sending metrics

```sh
# Increment a counter by 1 (default)
$ otel metric counter my-counter-name

# Decrease an UpDownCounter and add attributes
$ otel metric updown -a foo=bar -a baz=qux my-updown-name -1
```

### Sending traces

Sending a span with a known beginning and end time. Note that the time format is Unix time with nanosecon precision.

```sh
# Send a span with a known beginning and end date
$ span_start=$(date --date='5 minutes ago' +%s%n)
$ span_end=$(date --date='3 minutes ago' +%s%n)
$ otel span --start $span_start --end $span_end my-span-name
```

Crafting an entire trace from scratch

```sh
$ trace_id=$(otel generate trace_id)
$ span_id=$(otel generate span_id)
# Set this trace+span ID as the traceparent
$ traceparent="00-${trace_id}-${span_id}-01"
# Send child spans first
$ otel span --tp "$traceparent" my-child-span
$ otel span --tp "$traceparent" my-other-child-span
# Then send the parent
$ otel span --trace-id "$trace_id" --span-id "$span_id" my-top-span
```

Define the environment variable `OTEL_EXPORTER_OTLP_ENDPOINT` to point at your observability frontend.
This can be an instance of [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), or any other observability frontend which supports OTLP, for example Jaeger, LGTM stack (Loki, Grafana, Tempo, Mimir), ELK stack.
