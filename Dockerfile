FROM python:3.8

USER root

ADD ./mqtt_subscribe.py /home/src

WORKDIR /home/src

RUN pip3 install -r requirements.txt

CMD python3 mqtt_subscribe.py