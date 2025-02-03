#Semana 11 ejercicio de OOP.

def validate_user_entry_option():
        
        while True:
            
            try:
                parameter = int(input('Ingrese el numero de la acción que desea realizar: '))
                break
            except ValueError:
                print('No ha ingresado el valor correcto, vuelva a intentarlo')
                continue
        
        return parameter