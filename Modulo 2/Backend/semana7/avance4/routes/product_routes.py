# product_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_products_db, create_product_db, update_product_db, delete_product_db

product_bp = Blueprint('product', __name__)

@product_bp.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    products = get_all_products_db()
    return jsonify(products), 200

@product_bp.route("/products", methods=["POST"])
@admin_required()
def register_product():
    data = request.get_json()
    required_fields = ["code", "Price", "id_brand", "id_type"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        if create_product_db(data):
            return jsonify({"message": "Product registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register product"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@admin_required()
def update_product(product_id):
    data = request.get_json()
    allowed_fields = ["code", "Price", "id_brand", "id_type"]
    fields_to_update = {f: data[f] for f in allowed_fields if f in data}
    if not fields_to_update:
        return jsonify({"error": "No valid fields provided"}), 400
    try:
        if update_product_db(product_id, fields_to_update):
            return jsonify({"message": "Product updated successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@admin_required()
def delete_product(product_id):
    try:
        if delete_product_db(product_id):
            return jsonify({"message": "Product deleted successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500