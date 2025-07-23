from flask import Flask
from .extensions import db
from .config import Config
from app.routes import router_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(router_bp)

    return app
