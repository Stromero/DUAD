
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert, Update, Delete, select

#This is an example to make sure SQLAlchemy is install properly
#print(sqlalchemy.__version__)

metadata_obj = MetaData()

DB_URI = 'postgresql://postgres:Stromero123%40@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name",String(30)),
    Column("lastname",String(30))
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("description",String),
    Column("user_id",ForeignKey("users.id"), nullable=False)
)

cars_table = Table(
    "cars",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("brand",String),
    Column("type", String),
    Column("plate", String),
    Column("color", String),
    Column("user_id",ForeignKey("users.id"), nullable=True)
)

metadata_obj.create_all(engine)

# This is the inser of users

#statement = Insert(user_table).values(name="Priscilla")
with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name":"Michelle","lastname":"Barrantes"},
            {"name":"Silvio","lastname":"Rodriguez"},       
            {"name":"Rebecca","lastname":"Santamaria"},
            {"name":"Nabelio","lastname":"Rubio"},
            {"name":"Steven","lastname":"Romero"},
            {"name":"Priscilla","lastname":"Chaves"},
        ],
    )
    conn.commit()

# This is the update of user
statement = (
    Update(user_table).where(user_table.c.name == "Steven").values(lastname="Morera")
)
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# This is the delete from users
statement = Delete(user_table).where(user_table.c.name == "Michelle")
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# This is the insert of the cars
with engine.connect() as conn:
    result = conn.execute(
        insert(cars_table),
        [
            {"brand":"Toyota","type":"RAV4","plate":"JFI-489","color":"Yellow", "user_id":2},
            {"brand":"Kia","type":"Rio","plate":"SWQ-741","color":"White","user_id":None},
            {"brand":"Ford","type":"F150","plate":"CBV-766","color":"Black","user_id":6},
            {"brand":"Chevrolet","type":"Silverado","plate":"ASS-778","color":"Red", "user_id":None},
            {"brand":"Mazda","type":"CX-5","plate":"SFG-111","color":"Wine", "user_id":None},
            {"brand":"Kia","type":"Sportage","plate":"XCC-987","color":"Green", "user_id":None},
        ],
    )
    conn.commit()

# This is the update of cars
statement = (
    Update(cars_table).where(cars_table.c.id == 3).values(type="Raptor")
)
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# This is the delete from cars
statement = Delete(cars_table).where(cars_table.c.id == 5)
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# This is the insert of the address
with engine.connect() as conn:
    result = conn.execute(
        insert(address_table),
        [
            {"description":"350 mts este del puente arena, barrio monserrat, alajuela","user_id":2},
            {"description":"CCI Torre C, C. 28, San José, San Bosco, 10103","user_id":3},
            {"description":"Carretera al Volcán Irazú 219, Provincia de Cartago, Cartago, 30701","user_id":4},
            {"description":"Ruta Nacional Secundaria 155, Provincia de Guanacaste, Huacas","user_id":5},
        ],
    )
    conn.commit()

# This is the update of address
statement = (
    Update(address_table).where(address_table.c.id == 3).values(description="frente al Teatro, Jacó Centro, Plaza Coral sobre, Av. Pastor Díaz, Provincia de Puntarenas, Jacó")
)
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# This is the delete from cars
statement = Delete(address_table).where(address_table.c.id == 4)
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

# Asociar un automovil a un usuario
# This is the update of cars
statement = (
    Update(cars_table).where(cars_table.c.id == 6).values(user_id=5)
)
with engine.connect() as conn:
    result = conn.execute(statement)
    conn.commit()

#Select all user
statement = select("name:" + user_table.c.name, "lastname:" + user_table.c.lastname).order_by(user_table.c.id)
with engine.connect() as conn:
    for row in conn.execute(statement):
        print(row)

statement = select("brand:" + cars_table.c.brand, "type:" + cars_table.c.type, "plate:" + cars_table.c.plate, "color:" + cars_table.c.color).order_by(cars_table.c.id)
with engine.connect() as conn:
    for row in conn.execute(statement):
        print(row)

statement = select("description:" + address_table.c.description).order_by(address_table.c.id)
with engine.connect() as conn:
    for row in conn.execute(statement):
        print(row)
