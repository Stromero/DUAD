#ejercicio_5
#Cree una function que imprima el numero de mayusculas y minusculas de una string

def num_of_uppercase(text):
    sentence = text
    mayuscula = 0
    minuscula = 0

    for char in sentence:
        print(char)
        if(char != ' '):
            if( char == char.upper()):    
                print("Mayuscula")
                mayuscula = mayuscula + 1
            else:
                print("Minuscula")
                minuscula = minuscula + 1
    
    print(f'La cantidad de mayusculas es: {mayuscula} y la cantidad de minusculas es: {minuscula}')

num_of_uppercase('I Love Programming In Python')