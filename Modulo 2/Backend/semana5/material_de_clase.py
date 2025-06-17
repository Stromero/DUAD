import psycopg2

def format_user(user_record):
    return {
        "id": user_record[0],
        "full_name": user_record[1],
        "email": user_record[2],
        "password": user_record[3],
    }

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="Stromero123@",
    dbname="postgres",
)

print("Connected to the database")

cursor = connection.cursor()

cursor.execute("SELECT id, full_name, email, password FROM lyfter_duad.users;")

print("Query executed")

results = cursor.fetchall()

formatted_results = [format_user(result) for result in results]

print(formatted_results)

