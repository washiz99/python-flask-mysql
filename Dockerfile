FROM python:3.6.6-slim

ENV FLASK_APP manage.py
ENV FLASK_ENV production

WORKDIR /app
COPY . /app

RUN pip install pipenv==v2018.7.1
RUN pipenv install --system

ENTRYPOINT ["flask"]
CMD ["run","--host","0.0.0.0","--port","5000"]
