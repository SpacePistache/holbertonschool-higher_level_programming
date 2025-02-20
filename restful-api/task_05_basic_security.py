#!/usr/bin/python3
"""
Flask API with Basic Authentication & JWT Authentication
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()


app.config['JWT_SECRET_KEY'] = 'supersecretkey'
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for Basic Authentication.
    """
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Route protected by Basic Authentication.
    """
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint (JWT Authentication).
    """
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]}
        )
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Route protected by JWT authentication.
    """
    current_user = get_jwt_identity()
    return jsonify({
        "message": "JWT Auth: Access Granted",
        "user": current_user
    })


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only route protected by JWT authentication.
    """
    current_user = get_jwt_identity()

    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"})


if __name__ == '__main__':
    app.run(debug=True)
