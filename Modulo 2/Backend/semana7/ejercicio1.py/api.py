from flask import Flask, request, jsonify
from datetime import datetime
from db import db, User, Product, Invoice
from jwebt import jwt_manager, token_required, admin_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Stromero123%40@localhost:5432/postgres"
db.init_app(app)

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
    return jsonify({"mensaje": "Producto creado", "id": nuevo.id})

@app.route("/products", methods=["GET"])
@token_required
def ver_productos(current_user):
    productos = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "quantity": p.quantity
    } for p in productos])

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