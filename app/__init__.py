# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Je moet ingelogt zijn om deze pagina te bekijken"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    from app import models

    # temporary route
    @app.route('/')
    def hello_world():
      return 'Hello, World!'

    return app
