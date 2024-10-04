#Ejercicio_7
#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

def retornar_lista_numeros_primos(list_number):
    primos = []
    for item in list_number:
        if es_primo(item):
            primos.append(item)
    return primos
        
def main():
    list_number = [1,4,6,7,13,67]
    retornar_lista_numeros_primos(list_number)
    print(retornar_lista_numeros_primos(list_number))

if __name__ == "__main__":
    main()