# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

# Programa que pide 10 números y muestra el mayor

# Creamos una lista vacía para guardar los números
numbers = []

# Pedimos 10 números al usuario
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numbers.append(num)

# Mostramos todos los números ingresados
print("\nLos números ingresados son:")
print(numbers)

# Calculamos el número más alto
max_number = max(numbers)
print(f"El número más alto es: {max_number}")