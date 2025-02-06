# Cree un decorador que haga print de los parámetros y retorno de la función que decore.


def my_personal_decorator(func):

    def wrapper(argumento_1, argumento_2):

        print(f'Values from original function are: {argumento_1} and {argumento_2}')

        return func(argumento_1, argumento_2)
    
    return wrapper

@my_personal_decorator
def greetings(parameter_1, parameter_2):
    print(f'Hello everyone, this is {parameter_1}, telling you that {parameter_2}')
    return parameter_1 and parameter_2

greetings('Steven', 'everything will be ok!')
