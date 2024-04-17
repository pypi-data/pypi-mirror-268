FROM python:3.11

RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pre-commit==3.6.0
