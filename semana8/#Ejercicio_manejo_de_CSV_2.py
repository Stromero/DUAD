#Ejercicio_manejo_de_CSV_1
#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv

import csv

video_game_list = []

video_game_headers = (
    'Nombre',
    'Genero',
    'Desarrollador',
    'Clasificacion',
)

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers, delimiter='\t')
    writer.writeheader()
    writer.writerows(data)


def validar_opcion_de_usuario():

    #opcion_valida =''

    while True:
            selecion_de_usuario = input('Digite 1 o "guardar" para grabar detalles de un video juego o salir para terminar: ')

            if selecion_de_usuario == '1' or selecion_de_usuario == 'guardar' or selecion_de_usuario == 'salir':
                opcion_valida = selecion_de_usuario
                break
            else:    
                print('Opción no valida, por favor ingrese una de la opciones sugeridas para continuar')
                #validar_opcion_de_usuario()
        
    return opcion_valida 
    



def main():

    print('Bienvenido al programa para guardar detalles de un video juego')

    while True:

        seleccion_del_usuario = validar_opcion_de_usuario()

        if seleccion_del_usuario == 'salir' or seleccion_del_usuario == 'Salir':
            break
        
        video_game_list_dic = {}    

        nombre_del_videojuego = input('Ingrese el nombre del video juego: ')
        genero_del_videojuego = input('Ingrese el género del video juego: ')
        Desarrollador_del_videojuego = input('Ingrese el desarrollador del video juego: ')
        Clasificación_del_videojuego = input('Ingrese la clasificación del desarrollador del video juego: ')


        
        video_game_list_dic['Nombre'] = nombre_del_videojuego
        video_game_list_dic['Genero'] = genero_del_videojuego
        video_game_list_dic['Desarrollador'] = Desarrollador_del_videojuego
        video_game_list_dic['Clasificacion'] = Clasificación_del_videojuego

        

        video_game_list.append(video_game_list_dic)
        

    
    #print(video_game_list)
    print('sali del ciclo')
    write_csv_file('video_games.csv',video_game_list,video_game_headers)

if __name__ == '__main__':
    main()
