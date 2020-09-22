FROM python:3.6.12-alpine3.12

WORKDIR /app
COPY . /app

RUN pip install pipenv==2020.8.13
RUN pipenv install --system

ENV FLASK_APP src/run.py
ENV FLASK_ENV production

ENTRYPOINT ["flask"]
CMD ["run","--host","0.0.0.0","--port","5000"]
