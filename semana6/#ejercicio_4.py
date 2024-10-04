#ejercicio_4
#Cree una function que le de la vuelta a una string y lo retorne

def reverse_string(input_text):
    #my_string = 'Pizza con piña'
    longitud = len(input_text)

    for item in range(longitud-1,-1,-1):
        print(input_text[item])

def main():
    reverse_string("Colega del trabajo")

main()










