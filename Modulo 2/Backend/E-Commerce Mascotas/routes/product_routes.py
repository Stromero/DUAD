# product_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_products_db, create_product_db, update_product_db, delete_product_db
from cache import cache_response, invalidate_cache
from db.database import engine, product_table
from sqlalchemy import select, insert, update, delete
import datetime

product_bp = Blueprint('product', __name__)

@product_bp.route("/products", methods=["GET"])
@jwt_required()
@cache_response("products_list", expire=60)
def get_products():
    with engine.connect() as conn:
        result = conn.execute(select(product_table)).fetchall()
        products_list = [
            {
                "id": row.id,
                "code": row.code,
                "price": row.Price,
                "date_of_register": str(row.date_of_register),
                "id_brand": row.id_brand,
                "id_type": row.id_type
            }
            for row in result
        ]

    return jsonify({"source":"db","data":products_list})

# GET single product (cache indivudual)
@product_bp.route("/products/<int:pid>", methods=["GET"])
@cache_response("product:{pid}", expire=300)
def get_product(pid):
    with engine.connect() as conn:
        result = conn.execute(select(product_table).where(product_table.c.id == pid)).fetchone

        if not result:
            return jsonify({"error": "Producto no encontrado"}), 404
        
        prod_dict = {
            "id": result.id,
            "code": result.code,
            "price": result.Price,
            "date_of_register": str(result.date_of_register),
            "id_brand": result.id_brand,
            "id_type": result.id_type
        }
    
    return jsonify({"source":"db","data":prod_dict})


@product_bp.route("/products", methods=["POST"])
@admin_required()
@invalidate_cache(["products_list"])
def register_product():
    data = request.get_json()
    required_fields = ["code", "price", "id_brand", "id_type"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    new_product = {
        "code": data["code"],
        "Price": data["price"],
        "date_of_register": datetime.date.today(),
        "id_brand": data["id_brand"],
        "id_type": data["id_type"]
    }

    with engine.begin() as conn:
        result = conn.execute(insert(product_table).values(new_product))
        new_id = result.inserted_primary_key[0]

    new_product["date_of_register"] = str(new_product["date_of_register"])
    return jsonify({"message": "Product created", "id": new_id}), 201

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@admin_required()
@invalidate_cache(["products_list", "product:{product_id}"])
def update_product(product_id):
    data = request.get_json()

    with engine.begin() as conn:
        result = conn.execute(
            update(product_table).where(product_table.c.id == product_id).values(**data)
        )
        if result.rowcount == 0:
            return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto actualizado"}), 200


@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@admin_required()
@invalidate_cache(["products_list", "product:{product_id}"])
def delete_product(product_id):
    with engine.begin() as conn:
        result = conn.execute(
            delete(product_table).where(product_table.c.id == product_id)
        )
        if result.rowcount == 0:
            return jsonify({"error": "Producto no encontrado"}), 404
    
    return jsonify({"mensaje": "Producto eliminado"})