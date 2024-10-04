#Ejercicio_3_Dic
#Cree un programa que use una lista para eliminar keys de un diccionario

list_of_keys = ['access_level','age']
employee = {
    "name" : "Steven",
    "email" : "steven@gmail.com",
    "access_level" : 2,
    "age" : "31"
}

for key_of_list in list_of_keys:
        for key_of_dic in employee.keys():
                if(key_of_list == key_of_dic):
                        employee.pop(key_of_list)
                        break
  

print(f'{employee}')