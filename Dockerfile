FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app/"

RUN groupadd django && useradd -m -g django django

RUN apt update && apt -y upgrade && apt install -y netcat postgresql-client python3-setuptools && pip install pipenv

RUN mkdir /app
RUN mkdir -p /app/media/cabinet
RUN mkdir -p /app/media/temporary
RUN mkdir -p /app/media/reports
RUN mkdir -p /app/media/cabinet/project-files
WORKDIR /app
COPY . .
RUN pipenv install --skip-lock --dev --system

RUN chown -R django:django /app

USER django