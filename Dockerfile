# syntax=docker/dockerfile:1

FROM python:3.8.20-slim

RUN apt-get update && apt-get -y install gcc

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "word_clock.main"]
