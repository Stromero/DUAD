import csv
import json
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

def export_file_data_to_csv(cvsfile,filename):
        
        with open(filename) as fp:
            student_list = json.load(fp)

        write_csv_file(cvsfile,student_list,student_list_headers)

def csv_to_JSON(csvfilepath,JSONFilePath):

    path_file = Path(csvfilepath)

    if path_file.exists():
            print('Existe')
            jsonArray = []

            with open(csvfilepath,encoding='UTF-8') as csvf:
                csvReader = csv.DictReader(csvf)

                for row in csvReader:
                        jsonArray.append({
                            'nombre': row['nombre'],
                            'Seccion': row['Seccion'],
                            'Nota Espanol': row['Nota Espanol'],
                            'Nota Ingles': row['Nota Ingles'],
                            'Nota estudios sociales': row['Nota estudios sociales'],
                            'Nota de ciencias': row['Nota de ciencias'],
                            'Promedio': row['Promedio'] 
                            })

            with open(JSONFilePath,'w',encoding='utf-8') as jsonf:
                json.dump(jsonArray,jsonf,
                        indent=4,
                        separators=(',',':'))
    else:
         print('No existe un archivo CSV previamente exportado')

                    

    
    # jsonArray = []

    # #read csv file
    # with open(csvfilepath, encoding='UTF-8') as csvf:
    #     #load csv file data using csv library's dictionary reader
    #     csvReader = csv.DictReader(csvf)

    #     #convert each csv row into python dict
    #     for row in csvReader:
    #         #add this python dict to json array

    #         jsonArray.append({
    #             'nombre': row['nombre'],
    #             'Seccion': row['Seccion'],
    #             'Nota Espanol': row['Nota Espanol'],
    #             'Nota Ingles': row['Nota Ingles'],
    #             'Nota estudios sociales': row['Nota estudios sociales'],
    #             'Nota de ciencias': row['Nota de ciencias'],
    #             'Promedio': row['Promedio']
    #         })
        
    #     with open(JSONFilePath,'w',encoding='utf-8') as jsonf:
    #             json.dump(jsonArray,jsonf,
    #                 indent=4,
    #                     separators=(',',':'))

