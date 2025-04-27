from os import path
import json

#crear JSON
def crear_archivo_JSON(data,name_file):

    with open(name_file,"w") as json_file:
        json.dump(data,json_file,indent=4)

    print('JSON file created successfully!')

#leer archivo JSON
def leer_archivo_JSON(name_file):
    filename = name_file
    lista_de_objetos = []

    #Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')
    
    #Read JSON file
    with open(filename) as fp:
        lista_de_objetos = json.load(fp)
    
    #Verify existing file
    return lista_de_objetos