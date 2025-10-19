# type_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_types_db, create_type_db, update_type_db, delete_type_db
from cache import cache_response, invalidate_cache

type_bp = Blueprint('type', __name__)

@type_bp.route("/types", methods=["GET"])
@jwt_required()
@cache_response("types_list", expire=60)

def get_types():
    types = get_all_types_db()
    return jsonify({"source": "db", "data": types}), 200

@type_bp.route("/types", methods=["POST"])
@admin_required()
@invalidate_cache(["types_list"])

def register_type():
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        if create_type_db(data["description"]):
            return jsonify({"message": "Type registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register type"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@type_bp.route("/types/<int:type_id>", methods=["PUT"])
@admin_required()
@invalidate_cache(["types_list", "type:{type_id}"])
def update_type(type_id):
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        if update_type_db(type_id, data["description"]):
            return jsonify({"message": "Type updated successfully"}), 200
        else:
            return jsonify({"error": "Type not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@type_bp.route("/types/<int:type_id>", methods=["DELETE"])
@admin_required()
@invalidate_cache(["types_list", "type:{type_id}"])
def delete_type(type_id):
    try:
        if delete_type_db(type_id):
            return jsonify({"message": "Type deleted successfully"}), 200
        else:
            return jsonify({"error": "Type not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500