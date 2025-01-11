
class Bus:
    
    #
    def __init__(self, max_passengers):
        
        self.bus_passenger = []
        self.max_passengers = max_passengers

    def add_passenger_to_bus(self):

        while len(self.bus_passenger) <= self.max_passengers:
            person_name = input('add the name of the person: ')
            self.bus_passenger.append(person_name)
            if len(self.bus_passenger) == self.max_passengers:
                print('No more passengers are allowed to board, bus already full')
                break

    def remove_passengers_from_bus(self):
        while True:
            user_answer = input(str('Do you want to remove a passenger?'))
            if user_answer == 'Yes' or user_answer == 'yes':
                self.bus_passenger.pop()
            else:
                break
        

my_bus = Bus(5)

my_bus.add_passenger_to_bus()
my_bus.remove_passengers_from_bus()