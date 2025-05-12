from flask import Flask, jsonify, request
import json

import data

app = Flask(__name__)

lista_de_tareas = []

resultado = data.leer_archivo_JSON()

lista_de_tareas = resultado

#obtener todas las tareas
@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    estado = request.args.get("Estado")

    if estado:
        tareas_filtradas = [tarea for tarea in lista_de_tareas if tarea["Estado"] == estado]
        return tareas_filtradas
    
    data.crear_archivo_JSON(lista_de_tareas)
    return lista_de_tareas

#Crear una tarea
@app.route("/tareas", methods=["POST"])
def crear_tarea():

    datos = request.get_json()  # Tomamos los datos que llegan en formato JSON

    # Lista de campos obligatorios
    campos_obligatorios = ['Titulo', 'Descripcion', 'Estado']

    for campo in campos_obligatorios:
        valor = datos.get(campo)
        if valor is None or str(valor).strip() == "":
            return jsonify({'error': f'El campo "{campo}" es obligatorio y no puede estar vacío.'}), 400
        else:
            nueva_tarea = {
        "Identificador": len(lista_de_tareas) + 1,
        "Titulo": request.json["Titulo"],
        "Descripcion": request.json["Descripcion"],
        "Estado": request.json["Estado"]
    }
    lista_de_tareas.append(nueva_tarea)
    data.crear_archivo_JSON(lista_de_tareas)
    return nueva_tarea


#Actualizar una tarea
@app.route("/tareas/<int:tarea_id>", methods=["PUT"])
def actualizar_tarea(tarea_id):
    for tarea in lista_de_tareas:
        if tarea["Identificador"] == tarea_id:
            tarea["Titulo"]=request.json["Titulo"]
            tarea["Descripcion"]=request.json["Descripcion"]
            tarea["Estado"]=request.json["Estado"]
            data.crear_archivo_JSON(lista_de_tareas)
            return tarea
    
    return {"error":"La tarea no logro encontrar"}

#Eliminar una tarea
@app.route("/tareas/<int:tarea_id>", methods=["DELETE"])
def eliminar_tarea(tarea_id):
    for tarea in lista_de_tareas:
        if tarea["Identificador"] == tarea_id:
            lista_de_tareas.remove(tarea)
            data.crear_archivo_JSON(lista_de_tareas)
            return {"data":"tarea eliminada con exito"}


if __name__ == "__main__":
     app.run(host="localhost",debug=True)