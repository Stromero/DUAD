from db import PgManager

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="Stromero123@",
    host="localhost"
)

results = db_manager.execute_query("SELECT * FROM lyfter_duad.users;")
print(results)

db_manager.close_connection()