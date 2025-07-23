from app.controllers.student_controllers import get_student_dashboard_data
from flask import Blueprint

student_routes_bp = Blueprint('student_routes', __name__, url_prefix='/students')

@student_routes_bp.route('/', methods=['GET'])
def student_dashboard():
    return get_student_dashboard_data()
