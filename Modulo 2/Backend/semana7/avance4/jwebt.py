from flask_jwt_extended import get_jwt, create_access_token, jwt_required, JWTManager
from flask import jsonify
from functools import wraps

# Función de ayuda para verificar el rol de administrador
def is_admin():
    claims = get_jwt()
    return claims.get("role") == "admin"

# Decorador para requerir rol de administrador
def admin_required():
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            if not is_admin():
                return jsonify({"msg": "Acceso denegado. Se requiere el rol de admin."}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper