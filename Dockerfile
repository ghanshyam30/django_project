From python:3.7-stretch
MAINTAINER The Bad Coder

ENV PYTHONNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /django_project
WORKDIR /django_project
COPY ./django_project /django_project
WORKDIR /django_project