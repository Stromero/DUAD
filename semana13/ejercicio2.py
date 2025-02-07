# 2. Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


#This is the decorator
def check_parameter(func):

    def wrapper(*args, **kwargs):

        for item in args:
            #print(item)
            if isinstance(item,int) or isinstance(item,float):
                print('The value is an integer or floating type')
            else:
                #print('The value is not integer nor floating type')
                raise ValueError('The value is not integer nor floating type')
            
                

        for key, value in kwargs.items():
            #print(key,value)
            if isinstance(value,int) or isinstance(value,float):
                print('The value is an integer or floating type')
            else:
                #print('The value is not integer nor floating type')
                raise ValueError('The value is not integer nor floating type')
            
            

        return func(args,kwargs) 

    return wrapper


@check_parameter
#This is the main function
def check_if_is_number(*args, **kwargs):
    print(f'The value is: {args} and {kwargs}')
    

#check_if_is_number(22, 13, 'Steven', 91, 64, param_1='I', param_2=23 , param_3='Michelle')
#check_if_is_number(22, 45, 98 , 'Miguel angelo')
#check_if_is_number(param_1='Steven', param_2=22, param_3=66,param_4='Love' )
check_if_is_number(1, 2,'Steven', 34.7, 28, 91.2, param_1='Palabra', param_2=64, param_3=68.9, param_4='Hope' )




