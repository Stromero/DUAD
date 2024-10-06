
def show_menu_option():
    print('¡Bienvenido al Sistema de Control de Estudiantes!')    
    print('1. Ingresar información de un estudiante')
    print('2. Ver la información de los estudiantes ingresados')
    print('3. Ver el top 3 de los estudiantes con la mejor nota promedio')
    print('4. Ver la nota promedio entre las notas de todos los estudiantes')
    print('5. Exportar los datos a un archivo CSV')
    print('6. Importar los datos de un archivo CSV')

    try:
        option_choose_by_user = int(input('Ingrese el numero de la acción que desea realizar: '))
    except ValueError:
        print('No ha ingresado el valor correcto')

    print(f'option choose by user is: {option_choose_by_user}')   

def main():
    show_menu_option()

if __name__ == '__main__':
    main()