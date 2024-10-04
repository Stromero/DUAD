#Ejercicio_1
#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo
first_list = ['hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

#for tupla in zip(first_list,second_list):
#    print(tupla[0],tupla[1])

for value_a, value_b in zip(first_list,second_list):
    print(value_a,value_b)