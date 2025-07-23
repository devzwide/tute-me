from flask import Flask
from .extensions import db
from .config import Config
from app.routes.auth_routes import auth_bp
from app.routes.student_routes import student_routes_bp
from app.routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_routes_bp)

    return app
