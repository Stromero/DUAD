import data
import json
from os import path
from pathlib import Path

#Aqui esta la clase estudiante
class Student():
    def __init__(self, name, group_of_secondary, spanish_note, english_note, social_studies_note, sciences_note, average):

        self.name = name
        self.group_of_secondary = group_of_secondary
        self.spanish_note = spanish_note
        self.english_note = english_note
        self.social_studies_note = social_studies_note
        self.science_note = sciences_note
        self.average = average
        #self.students_list = []
    
    def __str__(self):
        return f'Nombre del estudiante: {self.name} , grupo: {self.group_of_secondary} , nota de español: {self.spanish_note} , nota de ingles: {self.english_note} , nota de estudios sociales: {self.social_studies_note} , nota de ciencias: {self.science_note}'

#This is the list student
students_list = []

def add_student(student):
    students_list.append(student)

def get_student():
    return students_list

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
                science_note = validate_int_entry('Ingrese la nota de Ciencias: ')
                
                student_average = calculate_average_of_student(spanish_note, english_note, social_studies_note, science_note)

                students_list.append(Student(name,group_of_secondary,spanish_note,english_note,social_studies_note,science_note,student_average))

                add_another_student = input('Desea agregar otro estudiante? :')

                if add_another_student == 'no':
                    break
        

def show_student_details():
        
    for student in students_list:
        print(student)
   

def sort_JSON():
        
    sorted_students = sorted(students_list,key=lambda x: x.average,
                        reverse=True)
    sorted_students = sorted_students[:3]
    
    for student in sorted_students:
        print('Nombre del estudiante: ' + student.name,
              'Promedio: ' + str(student.average))

def show_average_of_students_notes():  

    for student in students_list:
        print('Nombre estudiante: ' + student.name, 
              'Promedio: ' + str(student.average))



