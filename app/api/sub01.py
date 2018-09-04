from app.api import api
from flask_restful import Resource


class Sub01Resource(Resource):
    def get(self):
        return {'sub01': 'hello'}

api.add_resource(Sub01Resource, '/sub01')
