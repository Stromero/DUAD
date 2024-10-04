#Ejercicio 5.2
cantidad_de_notas = int(input('Ingrese la cantidad de notas:'))

print(f'cantidad de notas: ', cantidad_de_notas)

counter = 0
cantidad_aprobadas = 0
cantidad_reprobadas = 0
sum_average = 0
sum_aprobadas = 0
sum_reprobadas = 0
final_average = 0
average_aprobadas = 0
average_reprobadas = 0



while(counter < cantidad_de_notas):
    nota_estudiante = int(input('Ingrese la nota del estudiante'))
    if(nota_estudiante>=70):
        cantidad_aprobadas = cantidad_aprobadas + 1
        sum_aprobadas = sum_aprobadas + nota_estudiante
    else:
        cantidad_reprobadas = cantidad_reprobadas + 1
        sum_reprobadas = sum_reprobadas + nota_estudiante
        

    counter = counter +1
    sum_average = sum_average + nota_estudiante

final_average = sum_average / cantidad_de_notas
average_aprobadas = sum_aprobadas / cantidad_aprobadas 
average_reprobadas = sum_reprobadas / cantidad_reprobadas    

print("Cantidad de notas ingresadas: ", cantidad_de_notas, "\n",
          "Cantidad de notas aprobadas: ", cantidad_aprobadas, "\n",
          "Cantidad de notas no aprobadas: ", cantidad_reprobadas, "\n",
          "El promedio de las notas es: ", final_average, "\n",
          "El promedio de las notas aprobadas es: ", "%.2f" % average_aprobadas, "\n",
          "El promedio de las notas no aprobadas es: ", average_reprobadas
          )