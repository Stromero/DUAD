#ejercicio_2
#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda
#my_string = 'Pizza con piña'

#for item in reversed(my_string):
 #   print(item)

my_string = 'Pizza con piña'
longitud = len(my_string)

for item in range(longitud-1,-1,-1):
    print(my_string[item])