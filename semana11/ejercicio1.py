import math

class Circle:
    def __init__(self, radius): 

        self.radius = radius

    def get_area(self):
        #radius = input('Ingrese el radio del circulo')

        #area = math.pi * radius ** 2

        #print(f'El area del circulo es: {area}')
        return math.pi * (self.radius ** 2)

my_circle = Circle(5)
#my_circle.get_area(2)
print(f'El area del circulo es: {my_circle.get_area()}')