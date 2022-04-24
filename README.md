# python-flask-api
python flask api sample



sudo yum install python3-devel mysql-devel



```
$ git clone https://github.com/washiz99/python-flask-mysql.git
$ cd python-flask-mysql
```



```
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/api/v1/users -d '{"email": "abc@test.jp", "username": "washi"}'
```

```
curl http://127.0.0.1:5000/api/v1/users/1
```

```
curl -X PUT -H "Content-Type: application/json" http://127.0.0.1:5000/api/v1/users/1 -d '{"username": "washiz"}'
```

```
$ curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5000/api/v1/users/1
```


docker run -it -d -p 5000:5000 flask-api


