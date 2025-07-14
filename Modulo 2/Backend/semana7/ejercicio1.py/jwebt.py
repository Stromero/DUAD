import jwt
from functools import wraps
from datetime import datetime, timedelta
from flask import request, jsonify
from db import User

with open("config/private.pem", "r") as f:
    PRIVATE_KEY = f.read()

with open("config/public.pem", "r") as f:
    PUBLIC_KEY = f.read()

class JWT_Manager:
    def __init__(self):
        self.algorithm = "RS256"

    def encode(self, data):
        data['exp'] = datetime.utcnow() + timedelta(hours=2)
        return jwt.encode(data, PRIVATE_KEY, algorithm=self.algorithm)

    def decode(self, token):
        try:
            return jwt.decode(token, PUBLIC_KEY, algorithms=[self.algorithm])
        except Exception as e:
            print("Error al decodificar el token:", e)
            return None

jwt_manager = JWT_Manager()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        data = jwt_manager.decode(token)
        if not data:
            return jsonify({"error": "Token inválido o expirado"}), 401
        user = User.query.get(data["id"])
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404
        return f(user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.role != "admin":
            return jsonify({"error": "Solo admins pueden hacer esto"}), 403
        return f(current_user, *args, **kwargs)
    return decorated