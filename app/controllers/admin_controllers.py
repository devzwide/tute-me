from flask import Blueprint, request, session, jsonify
from functools import wraps
from sqlalchemy import or_
from app.models.module import Module
from app.models.user import User
from app.extensions import db

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return f(*args, **kwargs)
    return decorated_function

# Blueprint for admin routes

def get_all_users():
    search_term = request.args.get('q')
    query = User.query

    if search_term:
        query = query.filter(
            or_(
                User.username.ilike(f"%{search_term}%"),
                User.email.ilike(f"%{search_term}%"),
                User.name.ilike(f"%{search_term}%"),
                User.surname.ilike(f"%{search_term}%"),
                User.role.ilike(f"%{search_term}%")
            )
        )
    
    users = query.all()
    return jsonify({
        "users": [
            {
                "user_id": u.user_id,
                "username": u.username,
                "email": u.email,
                "name": u.name,
                "surname": u.surname,
                "role": u.role
            }
            for u in users
        ]
    })

def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.name = data.get("name", user.name)
    user.surname = data.get("surname", user.surname)
    user.role = data.get("role", user.role)

    password = data.get("password")
    if password:
        if len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters"}), 400
        user.set_password(password)

    db.session.commit()
    return jsonify({"message": "User updated successfully"})

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

# Module management functions

def create_module():
    data = request.get_json()

    module_name = data.get("module_name")
    module_code = data.get("module_code")
    description = data.get("description")

    if not module_name or not module_code:
        return {"message": "Module name and code are required", "status": "error"}, 400

    if Module.query.filter_by(module_code=module_code).first():
        return {"message": "Module code already exists", "status": "error"}, 409

    new_module = Module(module_name=module_name, module_code=module_code, description=description)
    db.session.add(new_module)
    db.session.commit()

    return {"message": "Module created successfully", "status": "success"}, 201

def search_modules(search_term=None):
    if search_term:
        modules = Module.query.filter(
            or_(
                Module.module_name.ilike(f'%{search_term}%'),
                Module.module_code.ilike(f'%{search_term}%'),
                Module.description.ilike(f'%{search_term}%')
            )
        ).all()
    else:
        modules = Module.query.all()

    return {
        "message": "Search results",
        "status": "success",
        "modules": [{"id": m.module_id, "name": m.module_name, "code": m.module_code, "description": m.description} for m in modules]
    }

def update_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        return {"message": "Module not found", "status": "error"}, 404

    data = request.get_json()
    module.module_name = data.get("module_name", module.module_name)
    module.module_code = data.get("module_code", module.module_code)
    module.description = data.get("description", module.description)

    db.session.commit()
    return {"message": "Module updated successfully", "status": "success"}

def delete_module(module_id):
    module = Module.query.get(module_id)
    if not module:
        return {"message": "Module not found", "status": "error"}, 404

    db.session.delete(module)
    db.session.commit()

    return {"message": "Module deleted successfully", "status": "success"}
