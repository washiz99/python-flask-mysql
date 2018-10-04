from flask import jsonify, request, url_for, current_app
from . import api
from .. import db
from ..models import User


@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
        page, per_page=current_app.config['FLASK_PER_PAGE'],
        error_out=False)
    users = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_users', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_users', page=page+1)
    return jsonify({
        'users': [user.to_json() for user in users],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/users', methods=['POST'])
def new_user():
    user = User(
        email=request.json['email'],
        username=request.json['username'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201


@api.route('/users/<int:id>', methods=['PUT'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if 'username' in request.json:
        user.username = request.json['username']
    if 'email' in request.json:
        user.email = request.json['email']
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())


@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.to_json())
