#ejercicio_3
#Cree un programa que intercambie el primer y ultimo elementode una lista. Debe de funcionar con lista de cualquier tamaño

my_list = ['Hola','Esto','Es','un','test','Se','Debe','Hacer','Rapido']
last_element = len(my_list)

#print(f'El primer elemento de la lista es: {mi_lista[0]}')
#print(f'El ultimo elemento de la lista es: {mi_lista[ultimo_elemento-1]}')

#mi_lista[0] = mi_lista[ultimo_elemento-1]
#mi_lista[ultimo_elemento-1] = mi_lista[0]

first_value = my_list[0]
last_value = my_list[last_element-1]

my_list[0] = last_value
my_list[last_element-1] = first_value


print(my_list)