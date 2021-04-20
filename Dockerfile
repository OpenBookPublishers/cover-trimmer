FROM python:3.8.0-slim-buster

WORKDIR /cover

RUN apt-get update && \
    apt-get install -y gcc poppler-utils

RUN rm -rf /var/cache/apt/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY ./src/ ./

ENV cover_type royaloctavo

CMD python main.py ${cover_type}