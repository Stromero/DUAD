from flask import Flask, request, jsonify
from sqlalchemy import insert, update, delete, select
from datetime import datetime

# Importamos las configuraciones de la base de datos y JWT
from db import (
    engine, users_table, rolls_table, rolls_user_table, cart_table,
    brand_table, type_table, product_table, invoice_table, product_invoice_table
)
from jwebt import create_access_token, JWTManager, jwt_required, admin_required

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secreta-key-para-jwt"
jwt = JWTManager(app)

# --- Endpoints de Autenticación ---

# ... (el resto de las importaciones y la configuración de Flask)

@app.route("/login", methods=["POST"])
def login():
    e_mail = request.json.get("e_mail", None)
    password = request.json.get("password", None)

    if not e_mail or not password:
        return jsonify({"msg": "Faltan credenciales"}), 400

    try:
        with engine.connect() as conn:
            # 1. Buscar el usuario por email
            stmt_user = select(users_table).where(users_table.c.e_mail == e_mail)
            user_result = conn.execute(stmt_user).first()

            if not user_result:
                return jsonify({"msg": "Correo o contraseña incorrectos"}), 401

            user_data = dict(user_result._mapping)
            
            # 2. Verificar la contraseña (ejemplo simplificado)
            # En una aplicación real, se usaría un hash como bcrypt.
            if user_data['password'] != password:
                return jsonify({"msg": "Correo o contraseña incorrectos"}), 401

            # 3. Obtener el rol del usuario
            # Usamos un JOIN para obtener la descripción del rol
            stmt_rol = select(rolls_table.c.description).join(
                rolls_user_table, rolls_table.c.id == rolls_user_table.c.id_rol
            ).where(rolls_user_table.c.id_user == user_data['id'])
            
            rol_result = conn.execute(stmt_rol).scalars().all()
            
            if not rol_result:
                return jsonify({"msg": "Usuario no tiene un rol asignado"}), 403

                        # Lógica para elegir el rol prioritario (por ejemplo, "admin")
            if "admin" in rol_result:
                final_role = "admin"
            else:
                # Si no es admin, toma el primer rol que encuentre
                final_role = rol_result[0]

            # 4. Crear el token con la información del rol de la base de datos
            additional_claims = {"role": final_role}
            access_token = create_access_token(identity=e_mail, additional_claims=additional_claims)
            
            return jsonify(access_token=access_token)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    with engine.connect() as conn:
        stmt = select(users_table)
        result = conn.execute(stmt)
        users = [dict(row) for row in result.mappings()]
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    with engine.connect() as conn:
        stmt = select(users_table).where(users_table.c.id == user_id)
        result = conn.execute(stmt).first()
        if not result:
            return jsonify({"error": "User not found"}), 404
        user = dict(result.mappings())
    return jsonify(user), 200

@app.route("/register_user", methods=["POST"])
@admin_required()
def register_user():
    data = request.get_json()
    required_fields = ["name", "date_of_birth", "e_mail", "password", "phone_number", "address"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    new_user = {k: data[k] for k in required_fields}
    new_user["date_of_register"] = datetime.now().date()
    try:
        with engine.begin() as conn:
            stmt = insert(users_table).values(**new_user)
            conn.execute(stmt)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_user/<int:user_id>", methods=["PUT"])
@admin_required()
def update_user(user_id):
    data = request.get_json()
    allowed_fields = ["name", "date_of_birth", "e_mail", "password", "phone_number", "address"]
    fields_to_update = {field: data[field] for field in allowed_fields if field in data}
    if not fields_to_update:
        return jsonify({"error": "No valid fields to update provided"}), 400
    try:
        with engine.begin() as conn:
            stmt = update(users_table).where(users_table.c.id == user_id).values(**fields_to_update)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
@admin_required()
def delete_user(user_id):
    try:
        with engine.begin() as conn:
            stmt = delete(users_table).where(users_table.c.id == user_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Roles ---

@app.route("/rolls", methods=["GET"])
@jwt_required()
def get_rolls():
    with engine.connect() as conn:
        stmt = select(rolls_table)
        result = conn.execute(stmt)
        rolls = [dict(row) for row in result.mappings()]
    return jsonify(rolls), 200

@app.route("/register_roll", methods=["POST"])
@admin_required()
def register_roll():
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    new_roll = {"description": data["description"]}
    try:
        with engine.begin() as conn:
            stmt = insert(rolls_table).values(**new_roll)
            conn.execute(stmt)
        return jsonify({"message": "Roll registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_roll/<int:id_roll>", methods=["PUT"])
@admin_required()
def update_roll(id_roll):
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        with engine.begin() as conn:
            stmt = update(rolls_table).where(rolls_table.c.id == id_roll).values(description=data["description"])
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Roll not found"}), 404
        return jsonify({"message": "Roll updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_roll/<int:id_roll>", methods=["DELETE"])
@admin_required()
def delete_roll(id_roll):
    try:
        with engine.begin() as conn:
            stmt = delete(rolls_table).where(rolls_table.c.id == id_roll)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Roll not found"}), 404
        return jsonify({"message": "Roll deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/register_roll_to_user", methods=["POST"])
@admin_required()
def register_roll_to_user():
    data = request.get_json()
    if not all(field in data for field in ["id_user", "id_rol"]):
        return jsonify({"error": "Missing required fields: id_user, id_rol"}), 400
    value_to_user = {"id_user": data["id_user"], "id_rol": data["id_rol"]}
    try:
        with engine.begin() as conn:
            stmt = insert(rolls_user_table).values(**value_to_user)
            conn.execute(stmt)
        return jsonify({"message": "Roll to user has been assigned successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Carrito ---

@app.route("/register_cart", methods=["POST"])
@jwt_required()
def register_cart():
    data = request.get_json()
    if "id_user" not in data:
        return jsonify({"error": "id_user is required"}), 400
    try:
        with engine.begin() as conn:
            stmt = insert(cart_table).values(id_user=data["id_user"])
            conn.execute(stmt)
        return jsonify({"message": "Cart registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_cart/<int:cart_id>", methods=["DELETE"])
@jwt_required()
def delete_cart(cart_id):
    try:
        with engine.begin() as conn:
            stmt = delete(cart_table).where(cart_table.c.id == cart_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Cart not found"}), 404
        return jsonify({"message": "Cart deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Marcas ---

@app.route("/brands", methods=["GET"])
@jwt_required()
def get_brands():
    with engine.connect() as conn:
        stmt = select(brand_table)
        result = conn.execute(stmt)
        brands = [dict(row) for row in result.mappings()]
    return jsonify(brands), 200

@app.route("/register_brand", methods=["POST"])
@admin_required()
def register_brand():
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        with engine.begin() as conn:
            stmt = insert(brand_table).values(description=data["description"])
            conn.execute(stmt)
        return jsonify({"message": "Brand registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_brand/<int:brand_id>", methods=["PUT"])
@admin_required()
def update_brand(brand_id):
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        with engine.begin() as conn:
            stmt = update(brand_table).where(brand_table.c.id == brand_id).values(description=data["description"])
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Brand not found"}), 404
        return jsonify({"message": "Brand updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_brand/<int:brand_id>", methods=["DELETE"])
@admin_required()
def delete_brand(brand_id):
    try:
        with engine.begin() as conn:
            stmt = delete(brand_table).where(brand_table.c.id == brand_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Brand not found"}), 404
        return jsonify({"message": "Brand deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Tipos ---

@app.route("/types", methods=["GET"])
@jwt_required()
def get_types():
    with engine.connect() as conn:
        stmt = select(type_table)
        result = conn.execute(stmt)
        types = [dict(row) for row in result.mappings()]
    return jsonify(types), 200

@app.route("/register_type", methods=["POST"])
@admin_required()
def register_type():
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        with engine.begin() as conn:
            stmt = insert(type_table).values(description=data["description"])
            conn.execute(stmt)
        return jsonify({"message": "Type registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_type/<int:type_id>", methods=["PUT"])
@admin_required()
def update_type(type_id):
    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    try:
        with engine.begin() as conn:
            stmt = update(type_table).where(type_table.c.id == type_id).values(description=data["description"])
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Type not found"}), 404
        return jsonify({"message": "Type updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_type/<int:type_id>", methods=["DELETE"])
@admin_required()
def delete_type(type_id):
    try:
        with engine.begin() as conn:
            stmt = delete(type_table).where(type_table.c.id == type_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Type not found"}), 404
        return jsonify({"message": "Type deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Productos ---

@app.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    with engine.connect() as conn:
        stmt = select(product_table)
        result = conn.execute(stmt)
        products = [dict(row) for row in result.mappings()]
    return jsonify(products), 200

@app.route("/register_product", methods=["POST"])
@admin_required()
def register_product():
    data = request.get_json()
    required_fields = ["code", "Price", "id_brand", "id_type"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    new_product = {k: data[k] for k in required_fields}
    new_product["date_of_register"] = datetime.now().date()
    try:
        with engine.begin() as conn:
            stmt = insert(product_table).values(**new_product)
            conn.execute(stmt)
        return jsonify({"message": "Product registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_product/<int:product_id>", methods=["PUT"])
@admin_required()
def update_product(product_id):
    data = request.get_json()
    allowed_fields = ["code", "Price", "id_brand", "id_type"]
    fields_to_update = {f: data[f] for f in allowed_fields if f in data}
    if not fields_to_update:
        return jsonify({"error": "No valid fields provided"}), 400
    try:
        with engine.begin() as conn:
            stmt = update(product_table).where(product_table.c.id == product_id).values(**fields_to_update)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_product/<int:product_id>", methods=["DELETE"])
@admin_required()
def delete_product(product_id):
    try:
        with engine.begin() as conn:
            stmt = delete(product_table).where(product_table.c.id == product_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Facturas ---

@app.route("/invoices", methods=["GET"])
@jwt_required()
def get_invoices():
    with engine.connect() as conn:
        stmt = select(invoice_table)
        result = conn.execute(stmt)
        invoices = [dict(row) for row in result.mappings()]
    return jsonify(invoices), 200

@app.route("/register_invoice", methods=["POST"])
@admin_required()
def register_invoice():
    data = request.get_json()
    required_fields = ["code", "date_of_register", "id_user"]
    if not all(f in data for f in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        with engine.begin() as conn:
            stmt = insert(invoice_table).values(**data)
            conn.execute(stmt)
        return jsonify({"message": "Invoice registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_invoice/<int:invoice_id>", methods=["DELETE"])
@admin_required()
def delete_invoice(invoice_id):
    try:
        with engine.begin() as conn:
            stmt = delete(invoice_table).where(invoice_table.c.id == invoice_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Invoice not found"}), 404
        return jsonify({"message": "Invoice deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Endpoints para Relaciones Producto-Factura ---

@app.route("/register_product_invoice", methods=["POST"])
@admin_required()
def register_product_invoice():
    data = request.get_json()
    required_fields = ["id_invoice", "id_product"]
    if not all(f in data for f in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        with engine.begin() as conn:
            stmt = insert(product_invoice_table).values(**data)
            conn.execute(stmt)
        return jsonify({"message": "Product assigned to invoice successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete_product_invoice/<int:product_invoice_id>", methods=["DELETE"])
@admin_required()
def delete_product_invoice(product_invoice_id):
    try:
        with engine.begin() as conn:
            stmt = delete(product_invoice_table).where(product_invoice_table.c.id == product_invoice_id)
            result = conn.execute(stmt)
        if result.rowcount == 0:
            return jsonify({"error": "Product-invoice relation not found"}), 404
        return jsonify({"message": "Product-invoice relation deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)