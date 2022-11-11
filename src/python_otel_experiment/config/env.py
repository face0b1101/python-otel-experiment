#!/usr/bin/env python

from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).parent

LOG_LEVEL = config("LOG_LEVEL", cast=str, default="WARNING")
DEFAULT_TZ = config("TZ", cast=str, default="Europe/London")

APM_AGENT_KEY = config("APM_AGENT_KEY", cast=str)

OTEL_RESOURCE_ATTRIBUTES = config("OTEL_RESOURCE_ATTRIBUTES", cast=str)
OTEL_EXPORTER_OTLP_ENDPOINT = config("OTEL_EXPORTER_OTLP_ENDPOINT", cast=str)
OTEL_EXPORTER_OTLP_HEADERS = config("OTEL_EXPORTER_OTLP_HEADERS", cast=str)
OTEL_METRICS_EXPORTER = config("OTEL_METRICS_EXPORTER", cast=str)
OTEL_LOGS_EXPORTER = config("OTEL_LOGS_EXPORTER", cast=str)
