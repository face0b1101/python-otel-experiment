#!/usr/bin/env python

# OTEL Python test for exporting basic OpenTelemetry data to Elastic APM

# OTLP reference code shamelessly stolen from:
# https://opentelemetry.io/docs/instrumentation/python/getting-started/
# https://opentelemetry.io/docs/instrumentation/python/exporters/#otlp-endpoint-or-collector

import logging
from random import randint

from flask import Flask

# These are the necessary import declarations
from opentelemetry import metrics, trace
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from rich.logging import RichHandler

from .config.env import (
    DEFAULT_TZ,
    LOG_LEVEL,
    OTEL_EXPORTER_OTLP_ENDPOINT,
    OTEL_EXPORTER_OTLP_HEADERS,
)

# Service name is required for most backends
resource = Resource(attributes={SERVICE_NAME: "Python OTEL Experiment"})
# resource = Resource(
#     attributes={
#         "service.name": "Python OTEL Experiment",
#         "service.version": 0.1,
#         "deployment.environment": "dev",
#     }
# )

# OTLP Tracer configuration
# Use Environment Variables by default, uncomment to explicitly set values
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(
    OTLPSpanExporter()
    # OTLPSpanExporter(
    #     endpoint=OTEL_EXPORTER_OTLP_ENDPOINT, headers=OTEL_EXPORTER_OTLP_HEADERS
    # )
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# OTLP Metrics configuration
# Use Environment Variables by default, uncomment to explicitly set values
reader = PeriodicExportingMetricReader(
    OTLPMetricExporter()
    # OTLPMetricExporter(
    #     endpoint=OTEL_EXPORTER_OTLP_ENDPOINT, headers=OTEL_EXPORTER_OTLP_HEADERS
    # )
)
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)

# Acquire a tracer
tracer = trace.get_tracer(__name__)

# Acquire a meter.
meter = metrics.get_meter(__name__)

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)

app = Flask(__name__)

# Check for debug environment variable
if LOG_LEVEL.upper() == "DEBUG":
    app.debug = True


@app.route("/rolldice")
def roll_dice():
    return str(do_roll())


def do_roll():
    with tracer.start_as_current_span("do_roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": res})
        return res


def main():
    """
    Main entry point for the application.
    """
    # setup basic logging
    logging.basicConfig(
        format="%(levelname)s %(asctime)s %(module)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
        level=LOG_LEVEL.upper(),
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    logging.info(f"LOG_LEVEL: {logging.getLevelName(logging.root.level)}")
    logging.info(f"DEFAULT_TZ: {DEFAULT_TZ}")
    logging.debug(f"ENDPOINT: {OTEL_EXPORTER_OTLP_ENDPOINT}")
    logging.debug(f"HEADER: {OTEL_EXPORTER_OTLP_HEADERS}")

    app.run(host="0.0.0.0")
