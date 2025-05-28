from flask import Flask, request, jsonify
from db import PgManager

app = Flask(__name__)

@app.route('/rents', methods=['POST'])
def create_rents():
    data = request.get_json()

    customer_id = data.get('customer_id')
    vehicule_id = data.get('vehicule_id')
    status = data.get('status')

    if not all([customer_id,vehicule_id,status]):
        return jsonify({'error': 'Missing mandatory fields'}), 400
    
    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('INSERT INTO lyfter_car_rental.rents(customer_id, vehicule_id, status) VALUES (%s, %s, %s)',(customer_id, vehicule_id, status))
        conn.commit()
        return jsonify({'Message':'Alquiler creado exitosamente'}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

@app.route('/rents/<int:id_rent>',methods=['PUT'])
def update_rent(id_rent):

    data = request.get_json()

    status = data.get('status')

    if not all([status]):
        return jsonify({'error': 'Missing mandatory fields'}), 400
    
    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('UPDATE lyfter_car_rental.rents SET status = %s WHERE id = %s',(status,id_rent))
        conn.commit()
        return jsonify({'Message':'Alquiler actualizado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()
    
@app.route('/rents', methods=['GET'])
def get_all_rents():

    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM lyfter_car_rental.rents')
        rents = cur.fetchall()
        return jsonify(rents)
    except Exception as e:
        return jsonify({'error': str(e)}),500
    finally:
        cur.close()
        conn.close()

@app.route('/rents/filter', methods=['GET'])
def get_rents_by_filter():

    customer_id = request.args.get('customer_id')
    vehicule_id = request.args.get('vehicule_id')
    date_of_register = request.args.get('date_of_register')
    status = request.args.get('status')

    filters = []
    values = []

    if customer_id:
        filters.append("customer_id = %s")
        values.append(customer_id)
    if vehicule_id:
        filters.append("vehicule_id = %s")
        values.append(vehicule_id)
    if date_of_register:
        filters.append("date_of_register = %s")
        values.append(date_of_register)
    if status:
        filters.append("status ILIKE %s")
        values.append(f"%{status}%")

    query = "SELECT * FROM lyfter_car_rental.rents"
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