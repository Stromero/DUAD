# cart_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required
from db.db_operations import create_cart_db, delete_cart_db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route("/carts", methods=["POST"])
@jwt_required()
def register_cart():
    data = request.get_json()
    if "id_user" not in data:
        return jsonify({"error": "id_user is required"}), 400
    try:
        if create_cart_db(data["id_user"]):
            return jsonify({"message": "Cart registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register cart"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@cart_bp.route("/carts/<int:cart_id>", methods=["DELETE"])
@jwt_required()
def delete_cart(cart_id):
    try:
        if delete_cart_db(cart_id):
            return jsonify({"message": "Cart deleted successfully"}), 200
        else:
            return jsonify({"error": "Cart not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500