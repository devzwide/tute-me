from flask import Blueprint

auth_bp = Blueprint('auth_routes', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return "Login Page"

@auth_bp.route('/logout', methods=['GET'])
def logout():   
    return "Logout Page"

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return "Register Page"
