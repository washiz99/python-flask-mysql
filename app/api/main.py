from app.api import api
from flask_restful import Resource, Api


class MainResource(Resource):
    def get(self):
        return {'main': 'hello'}

api.add_resource(MainResource, '/main')
