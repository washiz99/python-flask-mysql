from flask import Blueprint
from flask_restful import Resource, Api


main = Blueprint('main', __name__)
api = Api(main)

class MainAPI(Resource):
    def get(self):
        return {'main': 'hello'}

api.add_resource(MainAPI, '/')
