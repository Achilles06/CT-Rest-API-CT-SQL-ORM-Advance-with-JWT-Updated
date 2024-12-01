
from flask import Blueprint, request, jsonify
from models import User
from utils.token import encode_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = encode_token(user.id)
        return jsonify({"message": "Login successful", "token": token})
    return jsonify({"message": "Invalid credentials"}), 401
