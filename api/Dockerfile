FROM python:3.9.11-buster

ENV TZ=Asia/Tokyo
ENV FLASK_ENV production

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["scripts/entrypoint.sh"]
