import csv
import json
import actions
from pathlib import Path

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

def export_file_data_to_csv(cvsfile):
        
        student_list = actions.get_student()

        write_csv_file(cvsfile,student_list,student_list_headers)

def csv_to_JSON(csvfilepath):

    path_file = Path(csvfilepath)

    if path_file.exists():
            print('Existe')
            

            with open(csvfilepath,encoding='UTF-8') as csvf:
                csvReader = csv.DictReader(csvf)

                for row in csvReader:
                        actions.add_student({
                            'nombre': row['nombre'],
                            'Seccion': row['Seccion'],
                            'Nota Espanol': row['Nota Espanol'],
                            'Nota Ingles': row['Nota Ingles'],
                            'Nota estudios sociales': row['Nota estudios sociales'],
                            'Nota de ciencias': row['Nota de ciencias'],
                            'Promedio': row['Promedio'] 
                            })

            
                
    else:
         print('No existe un archivo CSV previamente exportado')
                

    
    

