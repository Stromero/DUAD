#Aca va estar la logica relaciona a las acciones del menu, excepto las de exportar e importa

def validate_string(parameter1):

    while True:
        try:
            string_entry_user = str(input(parameter1))
            break
        except ValueError:
            print('No ha ingresado el valor correcto, vuelva a intentarlo')
    
    return string_entry_user


def add_values_of_student():

    name = validate_string('Ingrese el Nombre Completo: ')
    prin(f'Name of the student is: {name}')
    group_of_secondary = input('Ingrese la Sección')
    spanish_note = input('Ingrese la nota de Español')
    social_studies_note = input('Ingrese la nota de Estudios Sociales')
    sciences_note = input('Ingrese la nota de Ciencias')


