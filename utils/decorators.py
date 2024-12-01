
from functools import wraps
from flask import request, jsonify
from utils.token import decode_token

def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({"message": "Missing token"}), 403
            user_id = decode_token(token.split(" ")[1])
            if isinstance(user_id, str):
                return jsonify({"message": user_id}), 403
            # Check user role logic here (assume a User model with role attribute)
            from models import User
            user = User.query.get(user_id)
            if user.role != required_role:
                return jsonify({"message": "Unauthorized"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
