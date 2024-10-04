#Pedir al usuario que ingrese 3 numeros
first_number = int(input("Ingrese el primer número: "))
second_number = int(input("Ingrese el segundo número: "))
third_number = int(input("ingrese el tercer número: "))


if(first_number >= second_number and first_number >= third_number):
    major_number = first_number
elif (second_number >= first_number and second_number >= third_number):
    major_number = second_number
elif (third_number >= first_number and third_number >= second_number):
    major_number = third_number
else:
    major_number = "There is no major number"

print("El numero mayor es: ", major_number)