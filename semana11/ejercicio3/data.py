import csv 
from pathlib import Path
import pandas as pd 
import actions

def write_csv_file(file_path, data):
     
     with open(file_path,'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            #escribir encabezados
            writer.writerow(['nombre',
            'Seccion',
            'Nota Espanol',
            'Nota Ingles',
            'Nota estudios sociales',
            'Nota de ciencias',
            'Promedio',])

            for student in data:
                  writer.writerow([student.name, student.group_of_secondary, student.spanish_note, student.english_note, student.social_studies_note, student.science_note, student.average ])


def export_file_data_to_csv(cvsfile):
        
        student_list = actions.get_student()

        write_csv_file(cvsfile,student_list)

        



def csv_to_Object(csvfilepath):

    path_file = Path(csvfilepath)

    if path_file.exists():
            print('Existe')
            

            with open(csvfilepath,'r', encoding='UTF-8') as csvfile:
                csvReader = csv.DictReader(csvfile)

                for row in csvReader:
                        student = (str(row['nombre']), str(row['Seccion']), row['Nota Espanol'], row['Nota Ingles'], row['Nota estudios sociales'], row['Nota de ciencias'], row['Promedio'])
                        actions.add_student(student)
                
    else:
         print('No existe un archivo CSV previamente exportado')

def MakeCSV(csvfilepath):

    student_list = actions.get_student()  

    with open(csvfilepath,'w', newline='') as f:
            writer = csv.writer(f)
            for student in student_list:
                  writer.writerow([student.name, student.group_of_secondary, student.spanish_note, student.english_note, student.social_studies_note, student.science_note, student.average ])