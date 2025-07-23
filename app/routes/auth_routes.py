from flask import Blueprint

from app.controllers.auth_controllers import logout_user, signup_user, login_user

auth_bp = Blueprint('auth_routes', __name__, url_prefix='/')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    return signup_user()

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_user()

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return logout_user()
