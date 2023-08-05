FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN python -m pip install temporalio pytest pytest-asyncio

ENTRYPOINT ["/bin/bash","start.sh"]
