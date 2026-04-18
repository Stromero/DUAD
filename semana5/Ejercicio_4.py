#Ejercicio_4
#Cree un programa que elimine los números impares de una lista
list_numbers = [1,2,3,4,5,6,7,8,9,10]

new_list = []

for item in list_numbers:
    if(item % 2 == 0):
        new_list.append(item)

print(new_list)   

