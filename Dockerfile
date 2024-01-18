FROM python:3.11-slim

WORKDIR /docker_code

COPY requirements.txt pyproject.toml poetry.lock /docker_code/

RUN pip install --upgrade pip && pip install --require-hashes --no-deps -r requirements.txt

COPY . .

