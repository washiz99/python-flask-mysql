FROM python:3.9.11-buster

WORKDIR /app
COPY . /app

RUN pip install pipenv==2022.4.8
RUN pipenv install --system

ENV FLASK_ENV production

CMD ["scripts/entrypoint.sh"]
