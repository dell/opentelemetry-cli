FROM python:3.11.0-alpine

WORKDIR /app
COPY . /app/
RUN python3 -m pip install /app
ENTRYPOINT ["otel"]
