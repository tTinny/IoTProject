FROM python:3.8

RUN apt-get update

ADD . /home/src

WORKDIR /home/src

RUN pip3 install -r requirements.txt

CMD python3 mqtt_subscribe.py