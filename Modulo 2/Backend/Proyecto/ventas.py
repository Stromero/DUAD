from flask import Flask, jsonify, request
import json
import data

app = Flask(__name__)

lista_de_ventas = []
name = "ventas.json"

resultado = data.leer_archivo_JSON(name)

lista_de_ventas = resultado

#obtener todas las ventas
@app.route("/ventas", methods=["GET"])
def obtener_ventas():    
    data.crear_archivo_JSON(lista_de_ventas,name)
    return lista_de_ventas

#Crear una nueva venta
@app.route("/ventas", methods=["POST"])
def crear_venta():

    datos = request.get_json()  # Tomamos los datos que llegan en formato JSON

    # Lista de campos obligatorios
    campos_obligatorios = ['Descripcion']

    for campo in campos_obligatorios:
        valor = datos.get(campo)
        if valor is None or str(valor).strip() == "":
            return jsonify({'error': f'El campo "{campo}" es obligatorio y no puede estar vacío.'}), 400
        else:
            nueva_venta = {
        "Identificador": len(lista_de_ventas) + 1,
        "Descripcion": request.json["Descripcion"],
    }
    lista_de_ventas.append(nueva_venta)
    data.crear_archivo_JSON(lista_de_ventas,name)
    return nueva_venta


#Actualizar una venta
@app.route("/ventas/<int:venta_id>", methods=["PUT"])
def actualizar_venta(venta_id):
    for venta in lista_de_ventas:
        if venta["Identificador"] == venta_id:
            venta["Descripcion"]=request.json["Descripcion"]
            data.crear_archivo_JSON(lista_de_ventas, name)
            return venta
    
    return {"error":"la venta no se logro encontrar"}

#Eliminar un usuario
@app.route("/ventas/<int:ventas_id>", methods=["DELETE"])
def eliminar_tarea(ventas_id):
    for venta in lista_de_ventas:
        if venta["Identificador"] == ventas_id:
            lista_de_ventas.remove(venta)
            data.crear_archivo_JSON(lista_de_ventas,name)
            return {"data":"venta eliminada con exito"}


if __name__ == "__main__":
     app.run(host="localhost",debug=True)