# syntax=docker/dockerfile:1

FROM python:3.10-slim

# good practice not to run as root
RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /app

COPY dist/*.whl .

RUN pip3 install --no-cache-dir ./*.whl \
    && rm -rf ./*.whl

RUN opentelemetry-bootstrap -a install

EXPOSE 5000

CMD ["opentelemetry-instrument","python-otel-experiment"]
# ENTRYPOINT ["python-otel-experiment"]