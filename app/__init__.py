from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.api import api_blueprint

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.register_blueprint(api_blueprint)
