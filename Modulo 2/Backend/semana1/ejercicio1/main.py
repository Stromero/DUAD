from flask import Flask, jsonify, request
import json

app = Flask(__name__)

lista_de_tareas = [
    {
        "Identificador": 1,
        "Titulo": "Reunion de requerimientos",
        "Descripcion": "Crear una reunion para conocer el cliente y empezar la primera etapa de producto",
        "Estado": "Por hacer",
    }
]

#obtener todas las tareas
@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    return lista_de_tareas

#Crear una tarea
@app.route("/tareas", methods=["POST"])
def crear_tarea():
    nueva_tarea = {
        "Identificador": len(lista_de_tareas) + 1,
        "Titulo": request.json["Titulo"],
        "Descripcion": request.json["Descripcion"],
        "Estado": request.json["Estado"]
    }
    lista_de_tareas.append(nueva_tarea)
    return nueva_tarea

#Actualizar una tarea
@app.route("/tareas/<int:tarea_id>", methods=["PUT"])
def actualizar_tarea(tarea_id):
    for tarea in lista_de_tareas:
        if tarea["Identificador"] == tarea_id:
            tarea["Titulo"]=request.json["Titulo"]
            tarea["Descripcion"]=request.json["Descripcion"]
            tarea["Estado"]=request.json["Estado"]
            return tarea
    
    return {"error":"La tarea no logro encontrar"}

#Eliminar una tarea
@app.route("/tareas/<int:tarea_id>", methods=["DELETE"])
def eliminar_tarea(tarea_id):
    for tarea in lista_de_tareas:
        if tarea["Identificador"] == tarea_id:
            lista_de_tareas.remove(tarea)
            return {"data":"tarea eliminada con exito"}


if __name__ == "__main__":
    app.run(host="localhost",debug=True)