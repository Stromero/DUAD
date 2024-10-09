#Aca va estar la logica relaciona a las acciones del menu, excepto las de exportar e importa

import json
from os import path

student_list = []

def validate_string_entry(parameter1):

    while True:
        try:
            string_entry_user = str(input(parameter1))
            break
        except ValueError:
            print('No ha ingresado el valor correcto, vuelva a intentarlo')
    
    return string_entry_user

def validate_note_is_from_0_to_100(entry_number):

    while True:
        if entry_number >=0 and entry_number <= 100:
            break
        else:
            entry_number = int(input('Nota no válida, Ingrese un valor entre 0 y 100: '))
    
    return entry_number


def validate_int_entry(parameter1):

    while True:
        try:
            int_entry_user = int(input(parameter1))
            int_entry_user = validate_note_is_from_0_to_100(int_entry_user)
            break
        except ValueError:
            print('No ha ingresado el valor correcto, vuelva a intentarlo')
               
    
    return int_entry_user

def show_student_details():
    filename = 'C:\\Users\\steve\\OneDrive\\Documentos\\DUAD\\semana10\\output.json'
    #listObj = []
    #student_list = []


    #check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')
    
    #Read JSON File
    with open(filename) as fp:
        student_list = json.load(fp)

    #Verify JSON File
    print(student_list)

def add_values_of_student():

    

    filename = 'C:\\Users\\steve\\OneDrive\\Documentos\\DUAD\\semana10\\output.json'
    
    with open(filename) as fp:
        student_list = json.load(fp)

    while True:

        name = validate_string_entry('Ingrese el Nombre Completo: ')
        print(f'Name of the student is: {name}')
        group_of_secondary = input('Ingrese la Sección: ')
        print(f'The group of secondary is: {group_of_secondary}')
        spanish_note = validate_int_entry('Ingrese la nota de Español: ')
        print(f'The spanish note is: {spanish_note}')
        social_studies_note = validate_int_entry('Ingrese la nota de Estudios Sociales: ')
        print(f'The social studies note is: {social_studies_note}')
        sciences_note = validate_int_entry('Ingrese la nota de Ciencias: ')
        print(f'the sciences note is: {sciences_note}')


        student_list.append({
            'nombre': name,
            'Seccion': group_of_secondary,
            'Nota Espanol': spanish_note,
            'Nota estudios sociales': social_studies_note,
            'Nota de ciencias': sciences_note
        })


        with open(filename,'w') as json_file:
            json.dump(student_list,json_file,
                      indent=4,
                      separators=(',',':'))

        add_another_student = input('Desea agregar otro estudiante? :')

        if add_another_student == 'no':
            break


