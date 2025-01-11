import csv
#import actions 
from pathlib import Path
import pandas as pd
import actions


def write_csv_file(file_path, data):
     
     with open(file_path,'w', newline='') as f:
            writer = csv.writer(f)
            for student in data:
                  writer.writerow([student.name, student.group_of_secondary, student.spanish_note, student.english_note, student.social_studies_note, student.science_note, student.average ])


def add_header(cvsfile):
      #Read content of csv file
      file = pd.read_csv(cvsfile)
      print("\nOriginal file:")

      #adding header
      headerList = ['Nombre','Seccion','Nota Espanol','Nota Ingles','Nota estudios sociales','Nota de ciencias','Promedio',]

      #converting data frame to csv
      file.to_csv(cvsfile, header=headerList, index=False)

      #display modified csv file
      file2 = pd.read_csv(cvsfile)
      print("\nModified file:") 
      print(file2)



def export_file_data_to_csv(cvsfile):
        
        student_list = actions.get_student()

        write_csv_file(cvsfile,student_list)

        add_header(cvsfile)



def csv_to_Object(csvfilepath):

    path_file = Path(csvfilepath)

    if path_file.exists():
            print('Existe')
            

            with open(csvfilepath,'r', encoding='UTF-8') as csvfile:
                csvReader = csv.DictReader(csvfile)

                for row in csvReader:
                        student =  (str(row['Nombre']), str(row['Seccion']), ['Nota Espanol'], row['Nota Ingles'], row['Nota estudios sociales'], row['Nota de ciencias'], row['Promedio'])
                                

                actions.add_student(student)
                
    else:
         print('No existe un archivo CSV previamente exportado')

def MakeCSV(csvfilepath):

    student_list = actions.get_student()  

    with open(csvfilepath,'w', newline='') as f:
            writer = csv.writer(f)
            for student in student_list:
                  writer.writerow([student.name, student.group_of_secondary, student.spanish_note, student.english_note, student.social_studies_note, student.science_note, student.average ])