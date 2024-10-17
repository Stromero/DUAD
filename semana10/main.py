
import menu
import actions

def show_menu_option():
    print('¡Bienvenido al Sistema de Control de Estudiantes!')    
    print('1. Ingresar información de un estudiante')
    print('2. Ver la información de los estudiantes ingresados')
    print('3. Ver el top 3 de los estudiantes con la mejor nota promedio')
    print('4. Ver la nota promedio entre las notas de todos los estudiantes')
    print('5. Exportar los datos a un archivo CSV')
    print('6. Importar los datos de un archivo CSV')

    option_choose_by_user =  menu.validate_user_entry_option() 

    print(f'option choose by user is: {option_choose_by_user}')

    if option_choose_by_user == 1:
        actions.add_values_of_student()
    if option_choose_by_user == 2:
        actions.show_student_details()
    if option_choose_by_user == 3:
         actions.sort_JSON()
    if option_choose_by_user == 4:
         actions.show_average_of_students_notes()
    if option_choose_by_user == 5:
         actions.export_file_data_to_csv()
    if option_choose_by_user == 6:
            csvfilepath = "C:\\Users\\steve\\OneDrive\\Documentos\\DUAD\\semana10\\student_data.csv"
            JSONFilePath = 'C:\\Users\\steve\\OneDrive\\Documentos\\DUAD\\semana10\\output.json'
            actions.csv_to_JSON(csvfilepath,JSONFilePath)
    

def main():
        while True:
             
            show_menu_option()

            finish_section = input('Desea finalizar?: ')
            if finish_section == 'Si' or finish_section == 'si':
                 break    

if __name__ == '__main__':
    main()