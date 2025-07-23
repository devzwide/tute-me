from app.models.module import Module
from app.extensions import db
from sqlalchemy import or_

from flask import request

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

    return {"message": "Search results", "modules": [module.module_name for module in modules]}

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



def get_student_dashboard_data():
    search_modules()

    return {"message": "Welcome to the Student Dashboard!", "status": "success"}
