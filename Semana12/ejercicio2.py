# Cree una clase abstracta de shape que:
# a.tenga los metodos abstractos de "calculate_perimeter" y "calculate_area"
# b.Ahora cree las siguientes clases que hereden de shape e implementen esos metodos: circle, square y rectangle
# c.Cada una de estas necesita los atributos respectivos para poder calcular el area y el perimetro

import math

from abc import ABC, abstractmethod 

class Shape(ABC):

    

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius_parameter):
        #super().__init__()
        self.radius = radius_parameter


    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f'The perimeter of circle is: {perimeter}')
    
    def calculate_area(self):
        area = math.pi * pow(self.radius,2)
        print(f'The area of the circle is: {area}')

    
class Square(Shape):

    def __init__(self, side_parameter):
        #super().__init__()
        self.side_of_square = side_parameter

    def calculate_perimeter(self):
        square_perimeter =  4 * self.side_of_square
        print(f'The perimeter of square is: {square_perimeter}')

    def calculate_area(self):
        square_area = 2 * self.side_of_square
        print(f'The area of the square is: {square_area}')
        
    
class Rectangle(Shape):

    def __init__(self , base_parameter, high_parameter):
        #super().__init__()
        self. base_of_rectangule = base_parameter
        self.high_of_rectangule = high_parameter
    
    def calculate_perimeter(self):
        rectangle_perimeter = 2 * (self.high_of_rectangule + self.base_of_rectangule)
        print(f'The perimeter of the rectangle is: {rectangle_perimeter}')
    
    def calculate_area(self):
        rectangle_area = self.high_of_rectangule * self.base_of_rectangule 
        print(f'The area of rectangle is: {rectangle_area}')
        

