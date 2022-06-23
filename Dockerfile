FROM afeoscyc-mw.cec.lab.emc.com/python:3.10.5-alpine

WORKDIR /app
COPY . /app/
RUN python3 -m pip install /app
ENTRYPOINT ["otel-cli"]