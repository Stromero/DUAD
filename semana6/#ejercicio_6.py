#ejercicio_6
#Cree una funcióm que acepte una string con palabras separadas por guion y retorne una string igual pero ordenada alfabeticamente

import re

def ordenar_alfabeticamente(text):
    chain = text
    list_of_values = re.split(r'-',chain)
    #print(list_of_values)
    sorted_list = sorted(list_of_values)
    print(sorted_list)
    #x = sorted_list.split("-")
    #print(x)
    result = "-".join(sorted_list)
    print(result)


    #for char in text:
       # print(char)


ordenar_alfabeticamente('python-variable-funcion-computadora-monitor')

