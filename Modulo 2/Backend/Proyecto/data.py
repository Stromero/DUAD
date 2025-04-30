from os import path
import json

#crear JSON
def create_file_JSON(data,name_file):

    with open(name_file,"w") as json_file:
        json.dump(data,json_file,indent=4)

    print('JSON file created successfully!')

#leer archivo JSON
def read_file_JSON(name_file):
    filename = name_file
    list_of_objects = []

    #Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')
    
    #Read JSON file
    with open(filename) as fp:
        list_of_objects = json.load(fp)
    
    #Verify existing file
    return list_of_objects