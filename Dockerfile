# Before execute
#     Linux   -> cp env-docker ./.env
#     Windows -> copy env-docker .env
# After execute 'docker-compose up -d --build'

FROM python:3.9-slim AS builder

RUN apt-get update -y
RUN apt-get install build-essential  -y

EXPOSE 5000

WORKDIR /app

ARG DEBUGGER
ENV DEBUGGER $DEBUGGER

ENV VIRTUAL_ENV=/opt/venv
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./ .

CMD [ "python", "run.py" ]