from flask import Blueprint
from app.routes.auth_routes import auth_bp
from app.routes.admin_routes import admin_bp

router_bp = Blueprint('router', __name__, url_prefix='/api/v1')

@router_bp.route('/', methods=['GET'])
def index():
    return {"message": "Welcome to the API"}, 200

router_bp.register_blueprint(auth_bp, url_prefix='/auth')
router_bp.register_blueprint(admin_bp, url_prefix='/admin')
