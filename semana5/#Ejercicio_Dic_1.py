#Ejercicio_Dic_1
#Cree un diccionario que guarde la siguiente informacion sobre un hotel
#nombre
#bumero_de_estrellas
#habitaciones
#habitaciones debe ser una lista, y cada lista debe tener la siguiente informacion:
#numero
#piso
#precio_por_noche

Diccionario_hotel = {}

Diccionario_hotel['nombre'] = 'San Jose Palacio'
Diccionario_hotel['numero_de_estrellas'] = 5
Diccionario_hotel['habitaciones'] = [
    {
        "numero" : 1,
        "piso" : 1,
        "precio_por_noche" : "$40",
    },
    {
        "numero" : 2,
        "piso" : 2,
        "precio_por_noche" : "$50"
    }
]

print(f'{Diccionario_hotel}')