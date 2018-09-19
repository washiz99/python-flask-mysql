from . import api
from flask_restful import Resource, reqparse
from app.models.user import User


class UsersResource(Resource):
    def get(self, user_id):
        return {'users-get': user_id}

    def delete(self, user_id):
        return {'users-delete': user_id}

    def put(self, user_id):
        return {'users-put': user_id}

class UsersList(Resource):
    def get(self):
        return {'users-get': 'list'}

    def post(self):
        return {'users-post': 'list'}


api.add_resource(UsersResource, '/users/<int:user_id>')
api.add_resource(UsersList, '/users')
