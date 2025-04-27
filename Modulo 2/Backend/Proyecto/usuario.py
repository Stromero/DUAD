from flask import Flask, jsonify, request
import json
import data

app = Flask(__name__)

lista_de_usuarios = []
name = "usuarios.json"

resultado = data.leer_archivo_JSON(name)

lista_de_usuarios = resultado

#obtener todos los usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():    
    data.crear_archivo_JSON(lista_de_usuarios,name)
    return lista_de_usuarios

#Crear un nuevo usuario
@app.route("/usuarios", methods=["POST"])
def crear_usuario():

    datos = request.get_json()  # Tomamos los datos que llegan en formato JSON

    # Lista de campos obligatorios
    campos_obligatorios = ['Rol', 'Nombre']

    for campo in campos_obligatorios:
        valor = datos.get(campo)
        if valor is None or str(valor).strip() == "":
            return jsonify({'error': f'El campo "{campo}" es obligatorio y no puede estar vacío.'}), 400
        else:
            nuevo_usuario = {
        "Identificador": len(lista_de_usuarios) + 1,
        "Rol": request.json["Rol"],
        "Nombre": request.json["Nombre"],
    }
    lista_de_usuarios.append(nuevo_usuario)
    data.crear_archivo_JSON(lista_de_usuarios,name)
    return nuevo_usuario


#Actualizar un usuario
@app.route("/usuarios/<int:usuario_id>", methods=["PUT"])
def actualizar_usuario(usuario_id):
    for usuario in lista_de_usuarios:
        if usuario["Identificador"] == usuario_id:
            usuario["Rol"]=request.json["Rol"]
            usuario["Nombre"]=request.json["Nombre"]
            data.crear_archivo_JSON(lista_de_usuarios,name)
            return usuario
    
    return {"error":"el usuario no se logro encontrar"}

#Eliminar un usuario
@app.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def eliminar_tarea(usuario_id):
    for tarea in lista_de_usuarios:
        if tarea["Identificador"] == usuario_id:
            lista_de_usuarios.remove(tarea)
            data.crear_archivo_JSON(lista_de_usuarios, name)
            return {"data":"usuario eliminado con exito"}


if __name__ == "__main__":
     app.run(host="localhost",debug=True)