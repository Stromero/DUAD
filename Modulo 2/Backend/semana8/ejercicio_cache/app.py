from flask import Flask, request, jsonify
from datetime import datetime
from db import db, User, Product, Invoice
from jwebt import jwt_manager, token_required, admin_required
import redis
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Stromero123%40@localhost:5432/postgres"
db.init_app(app)

redis_client = redis.StrictRedis(host="localhost",port=6379,db=0)

with app.app_context():
    db.create_all()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    nuevo = User(username=data["username"], password=data["password"], role=data.get("role", "user"))
    db.session.add(nuevo)
    db.session.commit()
    token = jwt_manager.encode({"id": nuevo.id})
    return jsonify({"token": token})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        token = jwt_manager.encode({"id": user.id})
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@app.route("/me", methods=["GET"])
@token_required
def me(current_user):
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "role": current_user.role
    })

@app.route("/products", methods=["POST"])
@token_required
@admin_required

def crear_producto(current_user):

    data = request.get_json()

    nuevo = Product(
        name=data["name"],
        price=data["price"],
        date_of_entry=data["date_of_entry"],
        quantity=data["quantity"]
    )
    db.session.add(nuevo)
    db.session.commit()

    #here que are implementing the cache
    redis_client.setex(f'product:{nuevo.id}', 300, json.dumps({
        "id": nuevo.id,
        "name": nuevo.name,
        "price": nuevo.price,
        "quantity": nuevo.quantity
    }))

    #Invalidate caching the whole list
    redis_client.delete('products_list')

    return jsonify({"mensaje": "Producto creado", "id": nuevo.id})

@app.route("/products", methods=["GET"])
@token_required
def ver_productos(current_user):
    # Here is were we are implementing the caching section
    cached_data = redis_client.get('products_list')

    if cached_data:
        return jsonify({"source":"cache", "data": json.loads(cached_data)})

    productos = Product.query.all()
    
    products_list = []

    for p in productos:
        product_dict = {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "quantity": p.quantity
        }

        products_list.append(product_dict)   

        redis_client.setex(f'product:{p.id}', 300, json.dumps(product_dict))

    redis_client.setex('products_list', 60, json.dumps(products_list))

    return jsonify({"source":"db","data": products_list})


@app.route("/products/<int:pid>", methods=["PUT"])
@token_required
@admin_required
def actualizar_producto(current_user, pid):
    producto = Product.query.get(pid)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    data = request.get_json()
    for campo in ["name", "price", "date_of_entry", "quantity"]:
        if campo in data:
            setattr(producto, campo, data[campo])
    db.session.commit()

    #Here we implement the caching
    redis_client.setex(f'product:{producto.id}', 300, json.dumps({
        "id": producto.id,
        "name": producto.name,
        "price": producto.price,
        "quantity": producto.quantity

    }))

    #Invalidation of caching
    redis_client.delete('products_list')

    return jsonify({"mensaje": "Producto actualizado"})

@app.route("/products/<int:pid>", methods=["DELETE"])
@token_required
@admin_required
def eliminar_producto(current_user, pid):
    producto = Product.query.get(pid)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    db.session.delete(producto)
    db.session.commit()

    #Implementing of caching
    redis_client.delete(f'product:{pid}')
    redis_client.delete('products_list')

    return jsonify({"mensaje": "Producto eliminado"})

@app.route("/purchase", methods=["POST"])
@token_required
def comprar(current_user):
    data = request.get_json()
    producto = Product.query.get(data["product_id"])
    if not producto:
        return jsonify({"error": "Producto no existe"}), 404
    factura = Invoice(
        code=data["code"],
        date_of_register=datetime.utcnow(),
        total_amount=producto.price,
        user_id=current_user.id,
        product_id=producto.id
    )
    db.session.add(factura)
    db.session.commit()
    return jsonify({"mensaje": "Compra realizada", "invoice_id": factura.id})

@app.route("/invoices", methods=["GET"])
@token_required
def ver_facturas(current_user):
    facturas = Invoice.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        "code": f.code,
        "amount": f.total_amount,
        "date": str(f.date_of_register)
    } for f in facturas])

if __name__ == "__main__":
    app.run(debug=True)