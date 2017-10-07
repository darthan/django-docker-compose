FROM python:3.6.2-stretch
ENV PYTHONUNBUFFERED 1
MAINTAINER "Erick Agrazal"
RUN mkdir /code
WORKDIR /code
ADD ./src/requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./src/ /code/