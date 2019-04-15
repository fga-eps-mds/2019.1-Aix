FROM python:3.7.2-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

#copies requirements to workdir
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/app

CMD python app.py run -h 0.0.0.0
