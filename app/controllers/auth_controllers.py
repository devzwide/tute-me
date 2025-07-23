from flask import request, jsonify, session, redirect
from app.models.user import User
from app.extensions import db

def start_user_session(user):
    session['user_id'] = user.user_id
    session['username'] = user.username
    session['role'] = user.role
    session['email'] = user.email

def signup_user():
    data = request.get_json()
    required_fields = ['username', 'email', 'name', 'surname', 'password']

    if not all(field in data for field in required_fields):
        return jsonify({"error": "All fields are required"}), 400

    username = data['username']
    email = data['email']
    name = data['name']
    surname = data['surname']
    role = data.get('role', 'student')
    password = data['password']
    
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 409
    
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400
    
    user = User(
        username=username,
        email=email,
        name=name,
        surname=surname,
        role=role
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    session.clear()

    start_user_session(user)

    return jsonify({"message": "User created successfully", "user_id": user.user_id}), 201

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        session.clear()
        start_user_session(user)

        return jsonify({
            "message": f"{user.role.capitalize()} login successful",
            "user_role": user.role,
            "user_id": user.user_id
        }), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401
    
def logout_user():
    session.clear()
    return jsonify({"message": "Logout successful"}), 200
