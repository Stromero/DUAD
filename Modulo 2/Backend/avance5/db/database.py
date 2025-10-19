from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Date, String, ForeignKey, insert, Update, Delete, select

DB_URI = 'postgresql://postgres:Stromero123%40@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)
metadata_obj = MetaData()

rolls_table = Table(
    "rolls",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("description", String)
)

users_table = Table (
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name",String),
    Column("date_of_birth", Date),
    Column("date_of_register", Date),
    Column("e_mail",String),
    Column("password",String),
    Column("phone_number",String),
    Column("address",String),
)

rolls_user_table = Table(
    "rolls_users",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_user", ForeignKey("users.id")),
    Column("id_rol",ForeignKey("rolls.id"))
)

cart_table = Table(
    "cart",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_user", ForeignKey("users.id"))
)

brand_table = Table(
    "brand",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("description", String),
)

type_table = Table(
    "type",
    metadata_obj,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("description",String)
)

product_table = Table(
    "product",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("code",String),
    Column("Price", Integer),
    Column("date_of_register", Date),
    Column("id_brand",ForeignKey("brand.id")),
    Column("id_type",ForeignKey("type.id"))
)

invoice_table = Table(
    "Invoice",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("code", String),
    Column("date_of_register", Date),
    Column("id_user",ForeignKey("users.id"))
)

product_invoice_table = Table(
    "product_invoice",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_invoice", ForeignKey("Invoice.id")),
    Column("id_product", ForeignKey("product.id"))
)

metadata_obj.create_all(engine)



