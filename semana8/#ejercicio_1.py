#ejercicio_1
#Cree un programa que lea nombres de canciones de un archivo(linea por linea) y guarde en otro archivo los mismos nombres ordenados alfabeticamente


def read_list_of_songs(file_path):
     
     try:
          with open(file_path, 'r' ) as f:
            lines = f.readlines()

            lines.sort()

            with open('sorted.txt','w') as f:
                f.write('\n'.join(str(n) for n in lines))
                 
     except Exception as error:
         print(f'ha ocurrido el siguiente error: {error}')
        
    
read_list_of_songs('List_of_songs.txt') 
