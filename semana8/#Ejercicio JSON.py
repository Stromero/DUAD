#Ejercicio JSON

import json
from os import path

#Create the JSON file 
def create_JSON_file():
    data_JSON = [
  {
    "name": {
      "english": "Pikachu"
    },
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  }
]

    with open("output.json","w") as json_file:
        json.dump(data_JSON,json_file,indent=4)

    print('JSON file created successfully!')

#----------------------------------------------------------------------------------------------------------------------------

def read_JSON_file():
    filename = 'C:\\Users\\steve\\OneDrive\\Documentos\\Usuario a desarrollador\\Semana 8\\output.json'
    listObj = []

    #Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')
    
    #Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)
    
    #Verify existing file
    print(listObj)

#---------------------------------------------------------------------------ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
def append_JSON_file():
    filename = 'C:\\Users\\steve\\OneDrive\\Documentos\\Usuario a desarrollador\\Semana 8\\output.json'
    listObj = []

    #Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')
    
    #Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)
    
    #Verify existing file
    print(listObj)
    print(type(listObj))

    while True:
        print('Bienvenido al programa para agregar pokemones al JSON')

        seleccion_de_usuario = input('Digite guardar para continuar o salir para terminar')

        if seleccion_de_usuario == 'salir':
            break

        nombre_del_pokemon = input('Ingrese el nombre del pokemon')
        tipo_de_pokemon = input('Ingrese el tipo al que pertenece el pokemon')
        hp = input('ingrese el valor de hp del pokemon')
        attack = input('ingrese el valor de ataque del pokemon')
        defense = input('ingrese el valor de defensa del pokemon')
        special_attack = input('ingrese el valor de ataque special del pokemon')
        special_defense = input('ingrese el valor de defensa especial del pokemon')
        spped = input('ingrese el valor de speed del pokemon')

        listObj.append({
            "name": {
                "english": nombre_del_pokemon
            },
            "type": [
                tipo_de_pokemon
            ],
            "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": special_attack,
            "Sp. Defense": special_defense,
            "Speed": spped
            }
        })

        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file,
                    indent=4,
                    separators=(',',':'))
        
        print(listObj)
        print('JSON file created successfully!')


def main():
    create_JSON_file()
    append_JSON_file()

if __name__ == '__main__':
    main()