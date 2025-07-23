from urllib import request
from flask import Blueprint
from app.controllers.admin_controllers import create_module, search_modules, update_module, delete_module, get_all_users, update_user, delete_user
from functools import wraps
from flask import session, jsonify

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# User management routes

@admin_bp.route('/users', methods=['GET'])
def admin_get_users():
    return get_all_users()

@admin_bp.route('/users/<int:user_id>', methods=['PUT'])
def admin_update_user(user_id):
    return update_user(user_id)

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
def admin_delete_user(user_id):
    return delete_user(user_id)

# Module management routes

@admin_bp.route('/modules/new', methods=['POST'])
def create_module_route():
    return create_module()

@admin_bp.route('/modules/search', methods=['GET'])
def search_modules_route():
    search_term = request.args.get('q')
    return search_modules(search_term=search_term)

@admin_bp.route('/modules/<int:module_id>', methods=['PUT'])
def update_module_route(module_id):
    return update_module(module_id)

@admin_bp.route('/modules/<int:module_id>', methods=['DELETE'])
def delete_module_route(module_id):
    return delete_module(module_id)
