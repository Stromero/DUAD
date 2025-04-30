from flask import Flask, jsonify, request
import json
import data

app = Flask(__name__)

list_of_users = []
name = "users.json"

result = data.read_file_JSON(name)

list_of_users = result

#obtener todos los usuarios
@app.route("/users", methods=["GET"])
def get_user():    
    data.create_file_JSON(list_of_users,name)
    return list_of_users

#Crear un nuevo usuario
@app.route("/users", methods=["POST"])
def create_user():

    data_of_values = request.get_json()  # Tomamos los datos que llegan en formato JSON

    # Lista de campos obligatorios
    mandatory_fields = ['Rol', 'Name']

    for field in mandatory_fields:
        value = data_of_values.get(field)
        if value is None or str(value).strip() == "":
            return jsonify({'error': f'The field "{field}" is mandatory and can not be empty.'}), 400
        else:
            new_user = {
        "Id": len(list_of_users) + 1,
        "Rol": request.json["Rol"],
        "Name": request.json["Name"],
    }
    list_of_users.append(new_user)
    data.create_file_JSON(list_of_users,name)
    return new_user


#Actualizar un usuario
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    for user in list_of_users:
        if user["Id"] == user_id:
            user["Rol"]=request.json["Rol"]
            user["Name"]=request.json["Name"]
            data.create_file_JSON(list_of_users,name)
            return user
    
    return {"error":"The user could not be found"}

#Eliminar un usuario
@app.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    for user in list_of_users:
        if user["Id"] == user_id:
            list_of_users.remove(user)
            data.create_file_JSON(list_of_users, name)
            return {"data":"user remove successfully!"}


if __name__ == "__main__":
     app.run(host="localhost",debug=True)