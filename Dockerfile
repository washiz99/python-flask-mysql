FROM python:3.6.6

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["run.py"]
