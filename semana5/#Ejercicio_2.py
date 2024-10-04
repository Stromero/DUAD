#Ejercicio_2
#Cree un programa que cree un diccionario usando 2 listas del mismo tamaño, usando una para sus keys y la otra para sus values

lits_a = ['First_name','last_name','role']
list_b = ['Steven','Romero','Software Enginner']

final_dictionary = {}

for key in lits_a:
    for value in list_b:
        final_dictionary[key] = value


print(f'El resultado final es: {final_dictionary}')