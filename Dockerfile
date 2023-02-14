FROM python:3.11.2-alpine

WORKDIR /app
COPY . /app/
RUN python3 -m pip install --no-cache-dir /app
ENTRYPOINT ["otel"]
