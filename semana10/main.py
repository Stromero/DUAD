
import menu
import actions
import data

csvfilepath = './student_data.csv'
filename = './output.json'
#csvfilepath = "C:\\Temp\\student_data.csv"
#filename = "C:\\Temp\\output.json"


def show_menu_option():
    print('¡Bienvenido al Sistema de Control de Estudiantes!')    
    print('1. Ingresar información de un estudiante')
    print('2. Ver la información de los estudiantes ingresados')
    print('3. Ver el top 3 de los estudiantes con la mejor nota promedio')
    print('4. Ver la nota promedio entre las notas de todos los estudiantes')
    print('5. Exportar los datos a un archivo CSV')
    print('6. Importar los datos de un archivo CSV')

    option_choose_by_user =  menu.validate_user_entry_option() 

    if option_choose_by_user == 1:
        actions.add_values_of_student(filename)
    if option_choose_by_user == 2:
        actions.show_student_details(filename)
    if option_choose_by_user == 3:
         actions.sort_JSON(filename)
    if option_choose_by_user == 4:
         actions.show_average_of_students_notes(filename)
    if option_choose_by_user == 5:
         data.export_file_data_to_csv(csvfilepath,filename)
    if option_choose_by_user == 6:
        data.csv_to_JSON(csvfilepath,filename)
    
def main():
        while True:
             
            show_menu_option()

            finish_section = input('Desea finalizar?: ')
            if finish_section == 'Si' or finish_section == 'si':
                 break    

if __name__ == '__main__':
    main()