FROM python:3

RUN mkdir /bujo-cli
WORKDIR /bujo-cli

COPY requirements.txt /bujo-cli/

RUN pip install -r requirements.txt


