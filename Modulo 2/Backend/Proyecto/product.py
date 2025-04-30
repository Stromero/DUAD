from flask import Flask, jsonify, request
import json
import data

app = Flask(__name__)

list_of_products = []
name = "products.json"

result = data.read_file_JSON(name)

list_of_products = result

#obtener todos los productos
@app.route("/products", methods=["GET"])
def get_products():    
    data.create_file_JSON(list_of_products, name)
    return list_of_products

#Crear un nuevo producto
@app.route("/products", methods=["POST"])
def create_produts():

    data_of_values = request.get_json()  # Tomamos los datos que llegan en formato JSON

    # Lista de campos obligatorios
    mandatory_fields = ['Product Name', 'Price']

    for field in mandatory_fields:
        value = data_of_values.get(field)
        if value is None or str(value).strip() == "":
            return jsonify({'error': f'the value "{value}" is mandatory and can not be empty.'}), 400
        else:
            new_product = {
        "Id": len(list_of_products) + 1,
        "Product Name": request.json["Product Name"],
        "Price": request.json["Price"],
    }
    list_of_products.append(new_product)
    data.create_file_JSON(list_of_products, name)
    return new_product


#Actualizar un producto
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    for product in list_of_products:
        if product["Id"] == product_id:
            product["Product Name"]=request.json["Product Name"]
            product["Price"]=request.json["Price"]
            data.create_file_JSON(list_of_products, name)
            return product
        
    return {"error":"The product can not be found"}

#Eliminar un producto
@app.route("/products/<int:product_id>", methods=["DELETE"])
def remove_product(product_id):
    for product in list_of_products:
        if product["Id"] == product_id:
            list_of_products.remove(product)
            data.create_file_JSON(list_of_products,name)
            return {"data":"product remove successfully!"}

if __name__ == "__main__":
     app.run(host="localhost",debug=True)