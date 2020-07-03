FROM python:3

ADD . /bujo
WORKDIR /bujo

COPY requirements.txt /bujo/

RUN pip install -r requirements.txt

CMD [ "python", "bujo/bujo-cli.py" ]

