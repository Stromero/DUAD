# Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6

import re

#Exercise #3
def sum_numbers(number_list):
    if isinstance(number_list,list):
        final_sum = 0
        for item in number_list:
            final_sum = final_sum + item
        print(final_sum)

        return final_sum
    raise ValueError('Input value is not allow')



#Exercise #4
def reverse_string(input_text):
    if isinstance(input_text,str):
        #my_string = 'Pizza con piña'
        output_text = ''
        longitud = len(input_text)

        for item in range(longitud-1,-1,-1):
            #print(input_text[item])
            output_text += input_text[item]
        
        #print(output_text)
        return output_text 

    raise ValueError('The value enter is not string, incorrect value entry')


#Exercise #5
def num_of_uppercase(text):

    if isinstance(text,str):

        sentence = text
        mayuscula = 0
        minuscula = 0

        for char in sentence:
            
            #print(char)
                if(char != ' '):
                    if( char == char.upper()):    
                        #print("Mayuscula")
                        mayuscula = mayuscula + 1
                    else:
                        #print("Minuscula")
                        minuscula = minuscula + 1

        return mayuscula , minuscula
        
    raise ValueError('Value is not allow, please enter a text')


#Exercise #6
def order_alf(text):

    if isinstance(text,str):
        chain = text
        list_of_values = re.split(r'-',chain)
        #print(list_of_values)
        sorted_list = sorted(list_of_values)
        #print(sorted_list)
        #x = sorted_list.split("-")
        #print(x)
        result = "-".join(sorted_list)
        #print(result)
    
        return result

    raise ValueError('Incorrect value entry, Use string value')    

#text_to_process = 'python-variable-funcion-computadora-monitor'
#order_alf(text_to_process)


#Exercise #7
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

def retornar_lista_numeros_primos(list_number):
    if isinstance(list_number,list):

        primos = []
        for item in list_number:
            if es_primo(item):
                primos.append(item)
        return primos
    raise ValueError('Incorrect input format, please enter a list')