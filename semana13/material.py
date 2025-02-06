#def my_funtion_with_infinite_params(*args):
 #   for index, arg in enumerate(args):
  #      print(f'Argument: {index}: {arg}')

#my_funtion_with_infinite_params(2,5,6,3,6,5,6)

#Tambien podemos combinarlos con otros parámetros.

#def my_function_with_infinite_params( my_other_param , *args):
 #   for index, arg in enumerate(args):
  #      print(f'Argument {index}:{arg}')
    
   # print(f'My other parameter is: {my_other_param}')

#my_function_with_infinite_params('steven',1,2,3,4,5,6,7,8,9,10)

#Los parámetros que no sean parte de los args y vayan después de estos hay que definirlos con su nombre al llamar la funcion (sino, Pyhton no sabra como diferenciarlos)

#def my_function_with_infinite_params(*args , my_other_params):
 #   for index, argument in enumerate(args):
  #      print(f'Element {index}:{argument}')
    
   # print(f'My other parameter is: {my_other_params}')

#my_function_with_infinite_params(1,2,3,4,5,6,7,8,9,10, my_other_params="Steven and Michelle love one each other")

#Kwargs

#def my_funtion_with_infinite_params(parameter_1, **kwargs):

  #  print(f'This is the first parameter: {parameter_1}')

   # print(f'The kwargs are: {kwargs}')

#my_funtion_with_infinite_params('Hello', first_parameter='Steven', second_parameter='Michelle')

#Los parametros args y kwargs se pueden combinar y usar en conjunto

def my_function(first_parameter, *args, **kwargs):

    print(f'This is the first parameter: {first_parameter}')

    for index, argument in enumerate(args):
        print(f'Element {index}:{argument}')

    print(f'Those are the Kwargs: {kwargs}')

my_function('Hello everyone', 1,2,3,4,5,6,7,8,9,10,first_kwargs='Steven', second_kwargs='Loves', third_kwargs='Michelle')