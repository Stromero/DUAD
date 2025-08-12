# app.py
from flask import Flask
from jwebt import JWTManager # Jwebt is the existing file name for JWT related functions

# Import database initialization (metadata_obj.create_all(engine) should run here or in db.py)
from db import database
from db import db_operations

# Import blueprints
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.roll_routes import roll_bp
from routes.cart_routes import cart_bp
from routes.brand_routes import brand_bp
from routes.type_routes import type_bp
from routes.product_routes import product_bp
from routes.invoice_routes import invoice_bp
from routes.product_invoice_routes import product_invoice_bp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secreta-key-para-jwt"
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(roll_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(brand_bp)
app.register_blueprint(type_bp)
app.register_blueprint(product_bp)
app.register_blueprint(invoice_bp)
app.register_blueprint(product_invoice_bp)


if __name__ == "__main__":
    database.metadata_obj.create_all(database.engine)
    app.run(debug=True)