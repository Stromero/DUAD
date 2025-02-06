# 2. Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


#This is the decorator
def check_parameter(func):
    def wrapper(arg1, arg2, arg3):

        my_numeric_list = []
        my_numeric_list.append(arg1)
        my_numeric_list.append(arg2)
        my_numeric_list.append(arg3)

      

        for i in my_numeric_list:
            
            if type(i) == int:
                print(f'The value of parameter {i} is number')
            else:
                raise ValueError (f'The value of parameter {i} is not number')
            continue

    return wrapper


@check_parameter
#This is the main function
def check_if_is_number(parameter_1, parameter_2, parameter_3):
    pass

check_if_is_number(1,'Michelle',3)





