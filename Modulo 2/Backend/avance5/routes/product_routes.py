# product_routes.py
from flask import Blueprint, request, jsonify
from jwebt import jwt_required, admin_required
from db.db_operations import get_all_products_db, create_product_db, update_product_db, delete_product_db
from cache import get_cache,set_cache, delete_cache
from db.database import engine, product_table
from sqlalchemy import select, insert, update, delete
import datetime

product_bp = Blueprint('product', __name__)

@product_bp.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    #Check if exist in cache
    cached_data = get_cache("products_list")
    if cached_data:
        return jsonify({"source":"cache","data":cached_data})
    
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

    set_cache("products_list", products_list, expire=60)
    return jsonify({"source":"db","data":products_list})

# GET single product (cache indivudual)
@product_bp.route("/products/<int:pid>", methods=["GET"])
def get_product(pid):
    cached_data = get_cache(f"product:{pid}")
    if cached_data:
        return jsonify({"source": "cache", "data":cached_data})
    
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
    
    set_cache(f"product:{pid}", prod_dict, expire=300)
    return jsonify({"source":"db","data":prod_dict})

# POST create product (invalid cache of the list and safe individual)
# @product_bp.route("/products", methods=["POST"])
# @admin_required()
# def register_product():
#     data = request.get_json()
#     new_product = {
#         "code": data["code"],
#         "Price": data["price"],
#         "date_of_register": datetime.date.today(),
#         "id_brand": data["id_brand"],
#         "id_type": data["id_type"]
#     }

#     with engine.begin() as conn:
#         result = conn.execute(insert(product_table).values(new_product))
#         new_id = result.inserted_primary_key[0]
    
#     delete_cache("products_list")
#     set_cache(f"product:{new_id}", {**new_product, "id": new_id}, expire=300)

#     return jsonify({"message": "Product created", "id":new_id})

@product_bp.route("/products", methods=["POST"])
@admin_required()
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

    delete_cache("products_list")
    new_product["date_of_register"] = str(new_product["date_of_register"])
    set_cache(f"product:{new_id}", {**new_product, "id": new_id}, expire=300)

    return jsonify({"message": "Product created", "id": new_id}), 201

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@admin_required()
def update_product(product_id):
    data = request.get_json()

    with engine.begin() as conn:
        result = conn.execute(
            update(product_table).where(product_table.c.id == product_id).values(**data)
        )

        if result.rowcount == 0:
            return jsonify({"error":"Producto no encontrado"}), 404
    
    #invalidamos lista y actualizamos cache individual
    delete_cache("products_list")

    with engine.connect() as conn:
        updated = conn.execute(
            select(product_table).where(product_table.c.id == product_id)
        ).fetchone()

        prod_dict = {
            "id": update.id,
            "code": update.code,
            "price": update.Price,
            "date_of_register": str(updated.date_of_register),
            "id_type": updated.id_type
        }
    
    #set_cache(f"product:{product_id}", prod_dict, expire=300)
    prod_dict["date_of_register"] = str(prod_dict["date_of_register"])
    set_cache(f"product:{product_id}", {**prod_dict, "id": product_id}, expire=300)

    return jsonify({"mensaje": "Producto actualizado"})

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@admin_required()
def delete_product(product_id):
    with engine.begin() as conn:
        result = conn.execute(
            delete(product_table).where(product_table.c.id == product_id)
        )

        if result.rowcount == 0:
            return jsonify({"error": "Producto no encontrado"}), 404
    
    delete_cache(f"product:{product_id}")
    delete_cache("products_list")

    return jsonify({"mensaje": "Producto eliminado"})