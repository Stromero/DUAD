#Ejercicio_4
#Cree un programa que elimine los números impares de una lista
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

for item in lista_numeros:
    if(item % 2 == 0):
        continue
    else:
     #lista_numeros.pop(item)
     lista_numeros.remove(item)
     #print(lista_numeros)


print(lista_numeros)   

