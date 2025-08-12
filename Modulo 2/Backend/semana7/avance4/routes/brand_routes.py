# brand_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_brands_db, create_brand_db, update_brand_db, delete_brand_db

brand_bp = Blueprint('brand', __name__)

@brand_bp.route("/brands", methods=["GET"])
@jwt_required()
def get_brands():
    brands = get_all_brands_db()
    return jsonify(brands), 200

@brand_bp.route("/brands", methods=["POST"])
@admin_required()
def register_brand():
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        if create_brand_db(data["description"]):
            return jsonify({"message": "Brand registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register brand"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@brand_bp.route("/brands/<int:brand_id>", methods=["PUT"])
@admin_required()
def update_brand(brand_id):
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        if update_brand_db(brand_id, data["description"]):
            return jsonify({"message": "Brand updated successfully"}), 200
        else:
            return jsonify({"error": "Brand not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@brand_bp.route("/brands/<int:brand_id>", methods=["DELETE"])
@admin_required()
def delete_brand(brand_id):
    try:
        if delete_brand_db(brand_id):
            return jsonify({"message": "Brand deleted successfully"}), 200
        else:
            return jsonify({"error": "Brand not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500