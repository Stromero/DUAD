from flask_jwt_extended import get_jwt, create_access_token, jwt_required, JWTManager
from flask import jsonify
from functools import wraps

def is_admin():
    claims = get_jwt()
    return claims.get("role") == "admin"

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            if not is_admin():
                return jsonify({"msg": "Access denied. Admin role required."}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper