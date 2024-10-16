#Aca va estar la logica relaciona a las acciones del menu, excepto las de exportar e importa

import json
from os import path
import csv


filename = 'C:\\Users\\steve\\OneDrive\\Documentos\\DUAD\\semana10\\output.json'
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
    
    #check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')
    
    #Read JSON File
    with open(filename) as fp:
        student_list = json.load(fp)

    #Verify JSON File
    print(student_list)

def calculate_average_of_student(note1,note2,note3,note4):

    total_of_notes = note1 + note2 + note3 + note4
    average_of_student =  total_of_notes / 4

    return average_of_student    

def add_values_of_student():

    with open(filename) as fp:
        student_list = json.load(fp)

    while True:

        name = validate_string_entry('Ingrese el Nombre Completo: ')
        #print(f'Name of the student is: {name}')
        group_of_secondary = input('Ingrese la Sección: ')
        #print(f'The group of secondary is: {group_of_secondary}')
        spanish_note = validate_int_entry('Ingrese la nota de Español: ')
        #print(f'The spanish note is: {spanish_note}')
        english_note = validate_int_entry('Ingrese la nota de Ingles: ')
        #print(f'The english note is: {english_note}')
        social_studies_note = validate_int_entry('Ingrese la nota de Estudios Sociales: ')
        #print(f'The social studies note is: {social_studies_note}')
        sciences_note = validate_int_entry('Ingrese la nota de Ciencias: ')
        #print(f'the sciences note is: {sciences_note}')

        student_average = calculate_average_of_student(spanish_note,english_note,social_studies_note,sciences_note)

        student_list.append({
            'nombre': name,
            'Seccion': group_of_secondary,
            'Nota Espanol': spanish_note,
            'Nota Ingles': english_note,
            'Nota estudios sociales': social_studies_note,
            'Nota de ciencias': sciences_note,
            'Promedio': student_average
        })


        with open(filename,'w') as json_file:
            json.dump(student_list,json_file,
                      indent=4,
                      separators=(',',':'))

        add_another_student = input('Desea agregar otro estudiante? :')

        if add_another_student == 'no':
            break

def sort_JSON():
    
    with open(filename) as fp:
        student_list = json.load(fp)
    
    gradeOrder = sorted(student_list,key=lambda k:k['Promedio'],
                        reverse=True)
    gradeOrder = gradeOrder[:3]
    
    print(gradeOrder)


def show_average_of_students_notes():    

    with open(filename) as fp:
        student_list = json.load(fp)

    average_of_students = [(item['nombre'], item['Promedio']) for item in student_list]    

    print(average_of_students)



student_list_headers = (
           'nombre',
            'Seccion',
            'Nota Espanol',
            'Nota Ingles',
            'Nota estudios sociales',
            'Nota de ciencias',
            'Promedio',
)

def write_csv_file(file_path, data,headear):


    with open(file_path,'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file,headear)
        writer.writeheader()
        writer.writerows(data)

def export_file_data_to_csv():
        
        with open(filename) as fp:
            student_list = json.load(fp)

        write_csv_file('student_data.csv',student_list,student_list_headers)

# def import_file_data_from_csv():

#     with open(filename,'r') as f:
#         lines = f.readlines()

#     print(lines)   

def csv_to_JSON(csvfilepath,JSONFilePath):
    
    jsonArray = []

    #read csv file
    with open(csvfilepath, encoding='UTF-8') as csvf:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            jsonArray.append(row)
        
        #convert python jsonArray to JSON string and write to file
        with open(JSONFilePath,'w',encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray,indent='4')
            jsonf.write(jsonString)

    print(jsonArray)


