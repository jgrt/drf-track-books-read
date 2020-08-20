FROM python:3.7

WORKDIR /src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY drf.requirements.txt /src/drf.requirements.txt

RUN pip install --upgrade pip && pip install -r drf.requirements.txt

COPY src/ /src