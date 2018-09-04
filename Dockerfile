FROM python:3.6.6-slim

WORKDIR /app
COPY . /app

RUN pip install pipenv==v2018.7.1
RUN pipenv install --system

ENTRYPOINT ["python"]
CMD ["run.py"]
