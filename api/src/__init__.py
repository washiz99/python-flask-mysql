from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    Migrate(app, db)

    from .api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app
