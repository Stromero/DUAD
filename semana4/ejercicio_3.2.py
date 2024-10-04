#ejercicio_3.2
#Cree un programa con un numero secreto de 1 a 10, El programa no debe cerrarse hasta que el usuario adivine el numero. 
#
#

import random

#Generamos un número aleatorio entre 1 y 10
secret_number = random.randint(1,10)
#print("The random number is: ", number_random)
#my_counter = 0

#user_number = int(input("Ingrese un numero"))

#while(my_counter <=10):
#    print(my_counter)
#    if(user_number == number_random):
#        print("adivinaste")
#        break
#    else:
#        print("vuelve a intentarlo")
#    my_counter = my_counter + 1


#if(user_number == number_random):
#    print("Adivinaste, Felcidades!!")
#    break
#else:
 #   print("Vuelve a intentarlo")

#Inicializamos el contador de intentos
amount_of_tries = 0

print("Bienvenido al juego de adivinar el numero secreto entre 1 y 10!")

#Comienza el bucle para permitir al jugador adivinar

while True:
    #Solicitamos al jugador que ingrese un número
    user_number = int(input("Ingrese un numero entre 1 y 10"))
    amount_of_tries = amount_of_tries + 1

    #Verificamos si el intento coincide con el número secreto
    if user_number == secret_number:
        print("Feliciades has adivinado el numero secreto")
        print(f'Numero de intentos {amount_of_tries}')
        break
    else:
        print("Numero incorrecto, intentalo de nuevo")