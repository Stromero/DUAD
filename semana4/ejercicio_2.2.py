#ejercicio_2.2
#Cree un programa que le pida al usuario su nombre, apellido y edad, muestre si es un bebé, niño, preadolecente, adulto joven, adulto o adulto mayor

user_name = str(input("Write your name"))
user_last_name = str(input("Write your lastname"))
user_age = int(input("Write your age"))

if(user_age>=65):
    print(user_name + " " + user_last_name + " " + " es adulto mayor")
elif(user_age>=25 or user_age<=64):
    print(user_name + " " + user_last_name + " " + "es adulto")
elif(user_age>=18 and user_age<=24):
    print(user_name + " " + user_last_name + " " + "es adulto joven")
elif(user_age>=12 and user_age<=17):
    print(user_name + " " + user_last_name + " " + "es preadolencente")
elif(user_age>=6 and user_age<=11):
    print(user_name + " " + user_last_name + " " + "es niño")
else:    
    print(user_name + " " + user_last_name + " " + "es bebé")