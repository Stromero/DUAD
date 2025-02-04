# Cree una clase abstracta de shape que:
# a.tenga los metodos abstractos de "calculate_perimeter" y "calculate_area"
# b.Ahora cree las siguientes clases que hereden de shape e implementen esos metodos: circle, square y rectangle
# c.Cada una de estas necesita los atributos respectivos para poder calcular el area y el perimetro

import math

from abc import ABC, abstractmethod 

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter():
        pass
    
    @abstractmethod
    def calculate_area():
        pass

class Circle(Shape):

    def calculate_perimeter(self, radius_parameter):
        perimeter = 2 * 3.14 * radius_parameter
        print(f'The perimeter of circle is: {perimeter}')
    
    def calculate_area(self, radius_parameter):
        area = 3.14 * pow(radius_parameter,2)
        print(f'The area of the circle is: {area}')

    
class Square(Shape):

    def calculate_perimeter(self, side_parameter):
        square_perimeter =  side_parameter + side_parameter + side_parameter + side_parameter
        print(f'The perimeter of square is: {square_perimeter}')

    def calculate_area(self, side_parameter):
        square_area = side_parameter * side_parameter
        print(f'The area of the square is: {square_area}')
        
    
class Rectangle(Shape):
    
    def calculate_perimeter(self, base_parameter, high_parameter):
        rectangle_perimeter = 2 * (high_parameter + base_parameter)
        print(f'The perimeter of the rectangle is: {rectangle_perimeter}')
    
    def calculate_area(self, base_parameter, high_parameter):
        rectangle_area = high_parameter * base_parameter
        print(f'The area of rectangle is: {rectangle_area}')
        

