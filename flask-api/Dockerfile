FROM python:3.6.12-alpine3.12

ENV FLASK_APP run.py
ENV FLASK_ENV production

WORKDIR /app
COPY . /app

RUN pip install pipenv==2020.8.13
RUN pipenv install --system

ENTRYPOINT ["flask"]
CMD ["run","--host","0.0.0.0","--port","5000"]
