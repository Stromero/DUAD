# db_operations.py
from sqlalchemy import insert, update, delete, select
from datetime import datetime
from db.database import (
    engine, users_table, rolls_table, rolls_user_table, cart_table,
    brand_table, type_table, product_table, invoice_table, product_invoice_table
)

# --- User Operations ---
def get_all_users_db():
    with engine.connect() as conn:
        stmt = select(users_table)
        result = conn.execute(stmt)
        return [dict(row) for row in result.mappings()]

def get_user_by_id_db(user_id):
    with engine.connect() as conn:
        stmt = select(users_table).where(users_table.c.id == user_id)
        result = conn.execute(stmt).first()
        return dict(result._mapping) if result else None

def create_user_db(user_data):
    with engine.begin() as conn:
        new_user = {k: user_data[k] for k in ["name", "date_of_birth", "e_mail", "password", "phone_number", "address"]}
        new_user["date_of_register"] = datetime.now().date()
        stmt = insert(users_table).values(**new_user)
        conn.execute(stmt)
        return True

def update_user_db(user_id, update_data):
    with engine.begin() as conn:
        stmt = update(users_table).where(users_table.c.id == user_id).values(**update_data)
        result = conn.execute(stmt)
        return result.rowcount > 0

def delete_user_db(user_id):
    with engine.begin() as conn:
        stmt = delete(users_table).where(users_table.c.id == user_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

# --- Authentication Operations ---
def get_user_by_email_db(email):
    with engine.connect() as conn:
        stmt = select(users_table).where(users_table.c.e_mail == email)
        result = conn.execute(stmt).first()
        return dict(result._mapping) if result else None

def get_user_roles_db(user_id):
    with engine.connect() as conn:
        stmt_rol = select(rolls_table.c.description).join(
            rolls_user_table, rolls_table.c.id == rolls_user_table.c.id_rol
        ).where(rolls_user_table.c.id_user == user_id)
        return conn.execute(stmt_rol).scalars().all()

# --- Roll Operations ---
def get_all_rolls_db():
    with engine.connect() as conn:
        stmt = select(rolls_table)
        result = conn.execute(stmt)
        return [dict(row) for row in result.mappings()]

def create_roll_db(description):
    with engine.begin() as conn:
        stmt = insert(rolls_table).values(description=description)
        conn.execute(stmt)
        return True

def update_roll_db(roll_id, description):
    with engine.begin() as conn:
        stmt = update(rolls_table).where(rolls_table.c.id == roll_id).values(description=description)
        result = conn.execute(stmt)
        return result.rowcount > 0

def delete_roll_db(roll_id):
    with engine.begin() as conn:
        stmt = delete(rolls_table).where(rolls_table.c.id == roll_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

def assign_roll_to_user_db(id_user, id_rol):
    with engine.begin() as conn:
        stmt = insert(rolls_user_table).values(id_user=id_user, id_rol=id_rol)
        conn.execute(stmt)
        return True

# --- Cart Operations ---
def create_cart_db(id_user):
    with engine.begin() as conn:
        stmt = insert(cart_table).values(id_user=id_user)
        conn.execute(stmt)
        return True

def delete_cart_db(cart_id):
    with engine.begin() as conn:
        stmt = delete(cart_table).where(cart_table.c.id == cart_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

# --- Brand Operations ---
def get_all_brands_db():
    with engine.connect() as conn:
        stmt = select(brand_table)
        result = conn.execute(stmt)
        return [dict(row) for row in result.mappings()]

def create_brand_db(description):
    with engine.begin() as conn:
        stmt = insert(brand_table).values(description=description)
        conn.execute(stmt)
        return True

def update_brand_db(brand_id, description):
    with engine.begin() as conn:
        stmt = update(brand_table).where(brand_table.c.id == brand_id).values(description=description)
        result = conn.execute(stmt)
        return result.rowcount > 0

def delete_brand_db(brand_id):
    with engine.begin() as conn:
        stmt = delete(brand_table).where(brand_table.c.id == brand_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

# --- Type Operations ---
def get_all_types_db():
    with engine.connect() as conn:
        stmt = select(type_table)
        result = conn.execute(stmt)
        return [dict(row) for row in result.mappings()]

def create_type_db(description):
    with engine.begin() as conn:
        stmt = insert(type_table).values(description=description)
        conn.execute(stmt)
        return True

def update_type_db(type_id, description):
    with engine.begin() as conn:
        stmt = update(type_table).where(type_table.c.id == type_id).values(description=description)
        result = conn.execute(stmt)
        return result.rowcount > 0

def delete_type_db(type_id):
    with engine.begin() as conn:
        stmt = delete(type_table).where(type_table.c.id == type_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

# --- Product Operations ---
def get_all_products_db():
    with engine.connect() as conn:
        stmt = select(product_table)
        result = conn.execute(stmt)
        return [dict(row) for row in result.mappings()]

def create_product_db(product_data):
    with engine.begin() as conn:
        required_fields = ["code", "Price", "id_brand", "id_type"]
        new_product = {k: product_data[k] for k in required_fields}
        new_product["date_of_register"] = datetime.now().date()
        stmt = insert(product_table).values(**new_product)
        conn.execute(stmt)
        return True

def update_product_db(product_id, update_data):
    with engine.begin() as conn:
        stmt = update(product_table).where(product_table.c.id == product_id).values(**update_data)
        result = conn.execute(stmt)
        return result.rowcount > 0

def delete_product_db(product_id):
    with engine.begin() as conn:
        stmt = delete(product_table).where(product_table.c.id == product_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

# --- Invoice Operations ---
def get_all_invoices_db():
    with engine.connect() as conn:
        stmt = select(invoice_table)
        result = conn.execute(stmt)
        return [dict(row) for row in result.mappings()]

def create_invoice_db(invoice_data):
    with engine.begin() as conn:
        stmt = insert(invoice_table).values(**invoice_data)
        conn.execute(stmt)
        return True

def delete_invoice_db(invoice_id):
    with engine.begin() as conn:
        stmt = delete(invoice_table).where(invoice_table.c.id == invoice_id)
        result = conn.execute(stmt)
        return result.rowcount > 0

# --- Product-Invoice Operations ---
def create_product_invoice_db(id_invoice, id_product):
    with engine.begin() as conn:
        stmt = insert(product_invoice_table).values(id_invoice=id_invoice, id_product=id_product)
        conn.execute(stmt)
        return True

def delete_product_invoice_db(product_invoice_id):
    with engine.begin() as conn:
        stmt = delete(product_invoice_table).where(product_invoice_table.c.id == product_invoice_id)
        result = conn.execute(stmt)
        return result.rowcount > 0