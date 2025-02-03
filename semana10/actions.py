#Aca va estar la logica relaciona a las acciones del menu, excepto las de exportar e importa

import data
import json
from os import path
from pathlib import Path


student_list = []

def add_student(student):
    student_list.append(student)

def get_student():
    return student_list

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
            continue   
    
    return int_entry_user

def calculate_average_of_student(note1,note2,note3,note4):

    total_of_notes = note1 + note2 + note3 + note4
    average_of_student =  total_of_notes / 4

    return average_of_student    

def add_values_of_student():
        
        while True:
        
                name = validate_string_entry('Ingrese el Nombre Completo: ')                
                group_of_secondary = input('Ingrese la Sección: ')                
                spanish_note = validate_int_entry('Ingrese la nota de Español: ')                
                english_note = validate_int_entry('Ingrese la nota de Ingles: ')                
                social_studies_note = validate_int_entry('Ingrese la nota de Estudios Sociales: ')                
                sciences_note = validate_int_entry('Ingrese la nota de Ciencias: ')
                
                student_average = calculate_average_of_student(spanish_note,english_note,social_studies_note,sciences_note)

                add_student({
                'nombre': name,
                'Seccion': group_of_secondary,
                'Nota Espanol': spanish_note,
                'Nota Ingles': english_note,
                'Nota estudios sociales': social_studies_note,
                'Nota de ciencias': sciences_note,
                'Promedio': student_average
                })

                add_another_student = input('Desea agregar otro estudiante? :')

                if add_another_student == 'no':
                    break
        

def show_student_details():
    
    student = get_student()

    for stud in student:
        print(stud)
   

def sort_JSON():
        
    gradeOrder = sorted(student_list,key=lambda k:k['Promedio'],
                        reverse=True)
    gradeOrder = gradeOrder[:3]
    
    for item in gradeOrder:
         print('Nombre:' + item['nombre'],
               'Promedio' + str(item['Promedio'])
              )

def show_average_of_students_notes():  

    average_of_students = [(item['nombre'], item['Promedio']) for item in student_list]    

    print(average_of_students)



