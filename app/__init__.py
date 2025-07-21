from flask import Flask
from .extensions import db
from .config import Config
from app.routes.auth_routes import auth_bp
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_routes.login' # Set the endpoint for the login view

    app.register_blueprint(auth_bp)

    return app
