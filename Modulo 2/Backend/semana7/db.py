from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import insert, select

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(30)),
    Column("password",String),
)

class DB_Manager:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://postgres:Stromero123%40@localhost:5432/postgres")
        metadata_obj.create_all(self.engine)
    
    def insert_user(self, username, password):
        statement = insert(user_table).returning(user_table.c.id).values(
            username=username,
            password=password
        )
        with self.engine.connect() as conn:
            result = conn.execute(statement)
            conn.commit()
            return result.all()[0]
        
    
    def get_user(self, username, password):
        statement = select(user_table).where(user_table.c.username == username).where(user_table.c.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(statement)
            users = result.all()

            if (len(users)==0):
                return None
            else:
                return users[0]
            
    def get_user_by_id(self, id):
        statement = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(statement)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]