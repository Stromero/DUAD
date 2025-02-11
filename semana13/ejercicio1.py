# Cree un decorador que haga print de los parámetros y retorno de la función que decore.


def my_personal_decorator(func):

    def wrapper(*args, **kwargs):

        print(f'Values of parameters are: {args}  {kwargs}')

        #Capturar el retorno de la funcion 

        result = func(*args,**kwargs )

        # Imprimir el retorno antes de devolverlo
        print(f'return value: {result}')

        return result
    
    return wrapper

@my_personal_decorator
def greetings(*args, **kwargs):

    return f'Values are {args} and {kwargs}'

greetings('Steven', 'everything will be ok!')
