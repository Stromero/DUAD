# product_invoice_routes.py
from flask import request, jsonify
from jwebt import admin_required
from db.db_operations import create_product_invoice_db, delete_product_invoice_db

def register_product_invoice_routes(app):
    @app.route("/product_invoices", methods=["POST"])
    @admin_required()
    def register_product_invoice():
        data = request.get_json()
        required_fields = ["id_invoice", "id_product"]
        if not all(f in data for f in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        try:
            if create_product_invoice_db(data["id_invoice"], data["id_product"]):
                return jsonify({"message": "Product assigned to invoice successfully"}), 201
            else:
                return jsonify({"error": "Failed to assign product to invoice"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/product_invoices/<int:product_invoice_id>", methods=["DELETE"])
    @admin_required()
    def delete_product_invoice(product_invoice_id):
        try:
            if delete_product_invoice_db(product_invoice_id):
                return jsonify({"message": "Product-invoice relation deleted successfully"}), 200
            else:
                return jsonify({"error": "Product-invoice relation not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500