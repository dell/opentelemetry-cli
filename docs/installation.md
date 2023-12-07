# Installing

## pip

```sh
$ pip install --user otel-cli
# pip installs by default to ~/.local/bin - this location must be in your PATH in order to run otel properly.
$ otel --help
```

## pipx

[pipx](https://pypa.github.io/pipx/) is a tool that lets you install Python applications in isolated environments, without polluting your main environment.

```sh
$ pipx install otel-cli
$ otel --help
```

## Docker

OpenTelemetry-CLI is available as a Docker image with all requirements packed into it. Running the docker image is effectively the same as running the `otel` command directly.

!!! tip
    If you want to give OpenTelemetry-CLI a try, you can create an alias which runs the Docker version without installing anything on your machine. Define this alias:

    ```
    alias otel="docker run --rm -e OTEL_EXPORTER_OTLP_ENDPOINT dell/opentelemetry-cli"
    ```

    Then, run the `otel` command as though it's already installed.
