# invoice_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_invoices_db, create_invoice_db, delete_invoice_db

invoice_bp = Blueprint('invoice', __name__)

@invoice_bp.route("/invoices", methods=["GET"])
@jwt_required()
def get_invoices():
    invoices = get_all_invoices_db()
    return jsonify(invoices), 200

@invoice_bp.route("/invoices", methods=["POST"])
@admin_required()
def register_invoice():
    data = request.get_json()
    required_fields = ["code", "date_of_register", "id_user"]
    if not all(f in data for f in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        if create_invoice_db(data):
            return jsonify({"message": "Invoice registered successfully"}), 201
        else:
            return jsonify({"error": "Failed to register invoice"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@invoice_bp.route("/invoices/<int:invoice_id>", methods=["DELETE"])
@admin_required()
def delete_invoice(invoice_id):
    try:
        if delete_invoice_db(invoice_id):
            return jsonify({"message": "Invoice deleted successfully"}), 200
        else:
            return jsonify({"error": "Invoice not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500