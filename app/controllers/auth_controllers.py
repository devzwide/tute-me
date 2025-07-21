from flask import request, jsonify, session
from app.models.user import User
from app.extensions import db

def signup_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    name = data.get('name')
    surname = data.get('surname')
    role = data.get('role')
    password = data.get('password')

    if not all([username, email, name, surname, role, password]):
        return jsonify({"error": "All fields are required"}), 400
    
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 409
    
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

    session['user_id'] = user.user_id
    session['username'] = user.username
    session['role'] = user.role
    session['email'] = user.email

    return jsonify({"message": "User created successfully"}), 201

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        session['user_id'] = user.user_id
        session['username'] = user.username
        session['role'] = user.role
        session['email'] = user.email

        if user.role == 'admin':
            return jsonify({"message": "Admin Login successful", "user_role": user.role}), 200
        elif user.role == 'student':
            return jsonify({"message": "Student Login successful", "user_role": user.role}), 200
        elif user.role == 'tutor':
            return jsonify({"message": "Tutor Login successful", "user_role": user.role}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401
    
def logout_user():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    session.pop('email', None)
    session.clear()

    return jsonify({"message": "Logout successful"}), 200
