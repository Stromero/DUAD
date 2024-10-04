#Ejercicio_de_Excepciones


def ingreso_de_valor():
        while True:
            try:
                primer_valor = int(input('Ingrese un valor numerico: '))
                break
            except ValueError as error:
                print('El valor ingresado: no corresponde a un numero, vuelva a intentarlo')

        return primer_valor

def validar_opcion_de_usuario():

    while True: 

        try:
            opcion = input("Seleccione una opción del menú o salir para terminar: ")
            if(opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4' or opcion == '5' or opcion == 'salir'):
                opcion_validad = opcion
                break
            else:
                print('El valor ingresado no es valido, por favor ingrese el numero de la operación que desea realizar o salir para finalizar')
        except ValueError as error:
           print('El valor ingresado no es valido, por favor ingrese el numero de la operación que desea realizar o salir para finalizar')

    return opcion_validad    

def main():
    
    resultado = ingreso_de_valor()

    print("Calculadora Básica")
    print("Operaciones disponibles")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")

    while True:
        #opcion_de_usuario = input("Seleccione una opción del menú o salir para terminar: ")
        opcion_de_usuario = validar_opcion_de_usuario()

        if opcion_de_usuario == 'salir':
            break

        if opcion_de_usuario == '5':
            resultado = 0
            main()


        segundo_numero = ingreso_de_valor()


        if  opcion_de_usuario == '1':
            resultado = resultado + segundo_numero
        elif opcion_de_usuario == '2':
            resultado = resultado - segundo_numero
        elif opcion_de_usuario == '3':
            resultado = resultado * segundo_numero
        elif opcion_de_usuario == '4':
            resultado = resultado / segundo_numero
        else:
            resultado = resultado

        print(f'el resultado de la operacion es : {resultado}')

print(f'sali del ciclo')

 

if __name__ == '__main__':
    main()