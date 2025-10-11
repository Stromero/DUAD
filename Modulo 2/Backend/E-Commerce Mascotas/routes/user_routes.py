# user_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_users_db, get_user_by_id_db, create_user_db, update_user_db, delete_user_db
from cache import cache_response, invalidate_cache

user_bp = Blueprint('user', __name__)

@user_bp.route("/users", methods=["GET"])
@jwt_required()
@cache_response("users_list", expire=60)

def get_users():
    users = get_all_users_db()
    return jsonify(users), 200

@user_bp.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
@cache_response("user:{user_id}", expire=300)

def get_user(user_id):
    user = get_user_by_id_db(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@user_bp.route("/users", methods=["POST"])
@admin_required()
@invalidate_cache(["users_list"])

def register_user():
    data = request.get_json()
    required_fields = ["name", "date_of_birth", "e_mail", "password", "phone_number", "address"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        if create_user_db(data):
            return jsonify({"message": "User registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register user"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route("/users/<int:user_id>", methods=["PUT"])
@admin_required()
@invalidate_cache(["users_list", "user:{user_id}"])

def update_user(user_id):
    data = request.get_json()
    allowed_fields = ["name", "date_of_birth", "e_mail", "password", "phone_number", "address"]
    fields_to_update = {field: data[field] for field in allowed_fields if field in data}
    if not fields_to_update:
        return jsonify({"error": "No valid fields to update provided"}), 400
    try:
        if update_user_db(user_id, fields_to_update):
            return jsonify({"message": "User updated successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
@admin_required()
@invalidate_cache(["users_list", "user:{user_id}"])

def delete_user(user_id):
    try:
        if delete_user_db(user_id):
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500