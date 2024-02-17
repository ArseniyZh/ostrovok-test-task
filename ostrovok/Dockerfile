FROM python:3.11-slim

WORKDIR /usr/src/ostrovok/

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
