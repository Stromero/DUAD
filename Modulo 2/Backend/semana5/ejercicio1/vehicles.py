from flask import Flask, request, jsonify
from db import PgManager

app = Flask(__name__)

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()

    brand = data.get('brand')
    model = data.get('model')
    year_of_creation = data.get('year_of_creation')
    status = data.get('status')

    if not all([brand,model,year_of_creation,status]):
        return jsonify({'error': 'Missing mandatory fields'}), 400
    
    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('INSERT INTO lyfter_car_rental.vehicules(brand, model, year_of_creation, status) VALUES (%s, %s, %s, %s)',(brand, model, year_of_creation, status))
        conn.commit()
        return jsonify({'Message':'Vehiculo creado exitosamente'}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()

@app.route('/vehicles/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    data = request.get_json()

    status = data.get('status')

    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('UPDATE lyfter_car_rental.vehicules SET status = %s WHERE id = %s', (status, vehicle_id))
        conn.commit()
        return jsonify({'Message': 'Vehiculo actualizado con exito'}),201
    except Exception as e:
        return jsonify({'error': str(e)}),500
    finally:
        cur.close()
        conn.close()

@app.route('/vehicles', methods=['GET'])
def get_all_vehicules():

    conn = PgManager.create_connection(None,'postgres','postgres','Stromero123@','localhost', 5432)
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM lyfter_car_rental.vehicules')
        vehicules = cur.fetchall()
        return jsonify(vehicules),201
    except Exception as e:
        return jsonify({'error':str(e)}),500
    finally:
        cur.close()
        conn.close()

@app.route('/vehicles/filter', methods=['GET'])
def get_vehicule_by_filter():

    brand = request.args.get('brand')
    model = request.args.get('model')
    year_of_creation = request.args.get('year_of_creation')
    status = request.args.get('status')

    filters = []
    values = []

    if brand:
        filters.append("brand ILIKE %s")
        values.append(f"%{brand}%")
    if model:
        filters.append("model ILIKE %s")
        values.append(f"%{model}%")
    if year_of_creation:
        filters.append("year_of_creation ILIKE %s")
        values.append(f"%{year_of_creation}%")
    if status:
        filters.append("status ILIKE %s")
        values.append(f"%{status}%")

    query = "SELECT * FROM lyfter_car_rental.vehicules"
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