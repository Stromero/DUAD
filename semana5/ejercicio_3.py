#ejercicio_3
#Cree un programa que intercambie el primer y ultimo elementode una lista. Debe de funcionar con lista de cualquier tamaño

mi_lista = ['Hola','Esto','Es','un','test','Se','Debe','Hacer','Rapido']
ultimo_elemento = len(mi_lista)

#print(f'El primer elemento de la lista es: {mi_lista[0]}')
#print(f'El ultimo elemento de la lista es: {mi_lista[ultimo_elemento-1]}')

#mi_lista[0] = mi_lista[ultimo_elemento-1]
#mi_lista[ultimo_elemento-1] = mi_lista[0]

primer_valor = mi_lista[0]
ultimo_valor = mi_lista[ultimo_elemento-1]

mi_lista[0] = ultimo_valor
mi_lista[ultimo_elemento-1] = primer_valor


print(mi_lista)