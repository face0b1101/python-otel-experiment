# Python OTEL (Docker) Experiment #

Quick and dirty, horribly-coded, `insert excuse for bad coding here`, project to demonstrate Python utilizing OpenTelemetry instrumentation, within a Docker container.

This is *not* production-ready, nowhere near :), and is purely to demonstrate that sending OTEL instrumentation from within a Docker container is straightforward.

- [Python OTEL (Docker) Experiment](#python-otel-docker-experiment)
  - [Python](#python)
    - [Poetry](#poetry)
  - [Docker](#docker)
    - [Build Docker Container Image](#build-docker-container-image)
    - [Run using Docker-Compose](#run-using-docker-compose)

## Python ##

The sample application is pretty much directly copied from [opentelemetry.io's](https://opentelemetry.io/) *[Getting Started](https://opentelemetry.io/docs/instrumentation/python/getting-started)* and *[Exporters](https://opentelemetry.io/docs/instrumentation/python/exporters)* examples using a Flask app. The app fires up a single web page returning a 'random' dice roll (from a D6).

A combination of Auto and Manual instrumentation then sends stuff to an OTLP endpoint, in my case I used an Elasticsearch APM endpoint running in [Elastic Cloud](https://cloud.elastic.co). This is configured using Environment variables. An example .env file is included in the repo.

### Poetry ###

The project uses [Poetry](https://python-poetry.org/) for package management etc. The instructions below expect you to use Poetry to build the app.

## Docker ##

### Build Docker Container Image ###

You won't be able to push to my GHCR registry, so just build and retag to something more suitable.

```bash
poetry build; poetry run poetry-lock-package --build
docker build -f dockerfile -t ghcr.io/face0b1101/python-otel-experiment:{VERSION} .
docker tag ghcr.io/face0b1101/python-otel-experiment:{VERSION} ghcr.io/face0b1101/python-otel-experiment:latest
docker push
```

### Run using [Docker-Compose](https://docs.docker.com/compose/) ###

Use the following `docker-compose.yml` example to run the app. Make sure you have a properly configured `.env` file, use `.env.example` for inspiration.

```yaml
---
version: "3.8"

services:
  python-otel-experiment:
    image: ghcr.io/face0b1101/python-otel-experiment:latest
    container_name: python-otel-experiment
    working_dir: $PWD
    volumes:
      - "$PWD:$PWD"
    tty: true
    env_file:
      - .env

```
