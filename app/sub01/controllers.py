from flask import Blueprint
from flask_restful import Resource, Api


sub01 = Blueprint('sub01', __name__)
api = Api(sub01)

class Sub01API(Resource):
    def get(self):
        return {'sub01': 'hello'}

api.add_resource(Sub01API, '/')
