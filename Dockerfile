FROM python:3.10.14-alpine

WORKDIR /app

COPY . .

RUN apk add openssh-client && \
    pip3 install virtualenv && \
    python3 -m venv .venv && \
    pip3 install poetry && \
    poetry install && \
    apk add bash

VOLUME [ "/app/.venv" ]

RUN chmod +x . &&\
    apk add git

CMD tail -f /dev/null