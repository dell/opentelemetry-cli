FROM python:3.12.0-alpine

WORKDIR /app
COPY . /app/
RUN python3 -m pip install --no-cache-dir /app
ENTRYPOINT ["otel"]
