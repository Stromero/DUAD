from flask import Flask, jsonify, request
import json
import data

app = Flask(__name__)

lista_de_productos = []
name = "productos.json"

resultado = data.leer_archivo_JSON(name)

lista_de_productos = resultado

#obtener todos los productos
@app.route("/productos", methods=["GET"])
def obtener_productos():    
    data.crear_archivo_JSON(lista_de_productos, name)
    return lista_de_productos

#Crear un nuevo producto
@app.route("/productos", methods=["POST"])
def crear_produtos():

    datos = request.get_json()  # Tomamos los datos que llegan en formato JSON

    # Lista de campos obligatorios
    campos_obligatorios = ['Nombre Producto', 'Precio']

    for campo in campos_obligatorios:
        valor = datos.get(campo)
        if valor is None or str(valor).strip() == "":
            return jsonify({'error': f'El campo "{campo}" es obligatorio y no puede estar vacío.'}), 400
        else:
            nuevo_producto = {
        "Identificador": len(lista_de_productos) + 1,
        "Nombre Producto": request.json["Nombre Producto"],
        "Precio": request.json["Precio"],
    }
    lista_de_productos.append(nuevo_producto)
    data.crear_archivo_JSON(lista_de_productos, name)
    return nuevo_producto


#Actualizar un producto
@app.route("/productos/<int:producto_id>", methods=["PUT"])
def actualizar_producto(producto_id):
    for producto in lista_de_productos:
        if producto["Identificador"] == producto_id:
            producto["Nombre Producto"]=request.json["Nombre Producto"]
            producto["Precio"]=request.json["Precio"]
            data.crear_archivo_JSON(lista_de_productos, name)
            return producto
        
    return {"error":"el producto no se logro encontrar"}

#Eliminar un producto
@app.route("/productos/<int:producto_id>", methods=["DELETE"])
def eliminar_producto(producto_id):
    for producto in lista_de_productos:
        if producto["Identificador"] == producto_id:
            lista_de_productos.remove(producto)
            data.crear_archivo_JSON(lista_de_productos,name)
            return {"data":"producto eliminado con exito"}

if __name__ == "__main__":
     app.run(host="localhost",debug=True)