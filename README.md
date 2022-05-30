# python-flask-api
Sample program using the lightweight web framework Flask.


## Requirements

- The following apps must be installed
  - docker
  - docker-compose
  - python 3.9
  - pip

## Pre-install

for CentOS

```
$ sudo yum install python3-devel mysql-devel
```

for Ubuntu

```
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

## Setup

### git clone

```
$ git clone https://github.com/washiz99/python-flask-mysql.git
$ cd python-flask-mysql
```

### for local debug

pipenv setup

```
$ cd api
$ pipenv install
$ pipenv shell
```

init database

```
$ export FLASK_APP=src/run.py
$ export FLASK_ENV=development
$ flask db init
$ flask db migrate
$ flask db upgrade
```

run shell

```
$ ./scripts/entrypoint.sh
```


### another terminal

- post

```
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/api/v1/users -d '{"email": "abc@test.jp", "username": "washi"}'
```

- get

```
curl http://127.0.0.1:5000/api/v1/users/1
```

- put

```
curl -X PUT -H "Content-Type: application/json" http://127.0.0.1:5000/api/v1/users/1 -d '{"username": "washiz"}'
```

- delete

```
$ curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5000/api/v1/users/1
```


