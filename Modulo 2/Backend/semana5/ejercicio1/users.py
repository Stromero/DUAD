from flask import Flask, request, jsonify
from db import PgManager

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    user_name = data.get('user_name')
    e_mail = data.get('e_mail')
    username = data.get('username')
    password = data.get('pass')
    date_of_birth = data.get('date_of_birth') #formato 'YYYY-MM-DD'
    status = data.get('status')

    if not all([user_name,e_mail,username,password,date_of_birth,status]):
        return jsonify({'error': 'Missing mandatory fields'}), 400
    
    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('INSERT INTO lyfter_car_rental.users(user_name, e_mail, username, pass, date_of_birth, status) VALUES (%s, %s, %s, %s, %s, %s)',(user_name, e_mail, username, password, date_of_birth, status))
        conn.commit()
        return jsonify({'Message':'Usuario creado exitosamente'}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    data = request.get_json()

    status = data.get('status')

    if not all([status]):
        return jsonify({'error': 'Missing mandatory fields'}), 400
    
    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()
    
    try:
        cur.execute('UPDATE lyfter_car_rental.users SET status = %s WHERE id = %s',(status,user_id))
        conn.commit()
        return jsonify({'Message':'Usuario actualizado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()
@app.route('/users',methods=['GET'])
def get_all_user():

    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('Select * from lyfter_car_rental.users')
        user = cur.fetchall()
        return jsonify(user),201
    except Exception as e:
        return jsonify({'error': str(e)}),500
    finally:
        cur.close()
        conn.close()

@app.route('/users/filter', methods=['GET'])
def get_data_by_filter():

    user_name = request.args.get('user_name')
    e_mail = request.args.get('e_mail')
    username = request.args.get('username')
    date_of_birth = request.args.get('date_of_birth')
    status = request.args.get('status')

    filters = []
    values = []

    if user_name:
        filters.append("user_name ILIKE %s")
        values.append(f"%{user_name}%")
    if e_mail:
        filters.append("e_mail ILIKE %s")
        values.append(f"%{e_mail}%")
    if username:
        filters.append("username ILIKE %s")
        values.append(f"%{username}%")
    if date_of_birth:
        filters.append("date_of_birth = %s")
        values.append(date_of_birth)
    if status:
        filters.append("status ILIKE %s")
        values.append(f"%{status}%")

    query = "SELECT * FROM lyfter_car_rental.users"
    if filters:
        query += " WHERE " + " AND ".join(filters)
    
    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute(query, tuple(values))
        result = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        users = [dict(zip(columns, row)) for row in result]
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()
    
if __name__ == '__main__':
    app.run()