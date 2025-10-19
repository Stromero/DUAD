# roll_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_rolls_db, create_roll_db, update_roll_db, delete_roll_db, assign_roll_to_user_db
from cache import cache_response, invalidate_cache

roll_bp = Blueprint('roll', __name__)

@roll_bp.route("/rolls", methods=["GET"])
@jwt_required()
@cache_response("rolls_list", expire=60)
def get_rolls():
    rolls = get_all_rolls_db()
    return jsonify(rolls), 200

@roll_bp.route("/rolls", methods=["POST"])
@admin_required()
@invalidate_cache(["rolls_list"])

def register_roll():
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        if create_roll_db(data["description"]):
            return jsonify({"message": "Roll registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register roll"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@roll_bp.route("/rolls/<int:roll_id>", methods=["PUT"])
@admin_required()
@invalidate_cache(["rolls_list"])
def update_roll(roll_id):
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        if update_roll_db(roll_id, data["description"]):
            return jsonify({"message": "Roll updated successfully"}), 200
        else:
            return jsonify({"error": "Roll not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@roll_bp.route("/rolls/<int:roll_id>", methods=["DELETE"])
@admin_required()
@invalidate_cache(["rolls_list"])
def delete_roll(roll_id):
    try:
        if delete_roll_db(roll_id):
            return jsonify({"message": "Roll deleted successfully"}), 200
        else:
            return jsonify({"error": "Roll not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@roll_bp.route("/rolls/assign", methods=["POST"])
@admin_required()
def assign_roll_to_user():
    data = request.get_json()
    if not all(field in data for field in ["id_user", "id_rol"]):
        return jsonify({"error": "Missing required fields: id_user, id_rol"}), 400
    try:
        if assign_roll_to_user_db(data["id_user"], data["id_rol"]):
            return jsonify({"message": "Roll to user has been assigned successfully"}), 201
        else:
            return jsonify({"error": "Failed to assign roll to user"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500