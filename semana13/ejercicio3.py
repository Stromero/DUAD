# 3.Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro que se
# encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class user:

    date_of_birth = date

    def __init__(self,date_of_birth_parameter):
        self.date_of_birth = date_of_birth_parameter

    @property
    def age(self):
        #debemos calcular la edad cada vez que la usemos
        # ya que va a variar dependiendo de la fecha actual
        today = date.today()
        return(today.year - self.date_of_birth.year -((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day) ))    
        

    def check_user_is_adult(func):
        def wrapper(arg):
            if int(arg) >= 18:
                print(('User is Adult'))
            else:
                raise ValueError('User is below the permited age')

        return wrapper

    @check_user_is_adult
    def check_age_of_user(paremeter):
        pass 

user_Steven = user(date(2015,3,22))
print(f'Age is: {user_Steven.age}')
user.check_age_of_user(user_Steven.age)