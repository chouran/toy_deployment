FROM python:3.9-slim

LABEL maintainer="Chouran Camara <chouran.c@gmail.com>"

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 8000

CMD uvicorn api_request_processor:app --host=0.0.0.0 --reload

