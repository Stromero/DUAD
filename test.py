class Car:
	wheel_number = 4


my_car = Car()

my_truck = Car()
my_truck.wheel_number = 6

my_bigger_truck = Car()
my_bigger_truck.wheel_number = 8


print(my_car.wheel_number)
print(my_truck.wheel_number)
print(my_bigger_truck.wheel_number)