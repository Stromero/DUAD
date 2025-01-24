
class Bus:
    
    #
    def __init__(self, max_passengers):
        
        self.bus_passenger = []
        self.max_passengers = max_passengers

    def show_passenger(self):

        print(f'List of passenger are the following: {self.bus_passenger}' )
        

    def add_passenger_to_bus(self):

        while len(self.bus_passenger) <= self.max_passengers:
            
            person_name = validate_string_input('add the name of the person: ')

            self.bus_passenger.append(person_name)

            if len(self.bus_passenger) == self.max_passengers:

                print('No more passengers are allowed to board, bus already full')

                break

    def remove_passengers_from_bus(self):
        while True:
            user_answer = input(str('Do you want to remove a passenger?'))

            if user_answer == 'Yes' or user_answer == 'yes':

                if user_answer == 'Yes' or user_answer == 'yes':
                    #Here I will add a validation to ask the user if want to remove a passenger by name
                    remove_passenger_by_name = input(str('Do you want to remove a passenger by name'))

                    if remove_passenger_by_name == 'yes' or remove_passenger_by_name == 'Yes':

                        print(self.bus_passenger)

                        #name_to_remove_from_bus = input(str('Write the name of the passenger you want to remove'))
                        name_to_remove_from_bus = validate_string_input('Write the name of the passenger you want to remove')

                        self.bus_passenger.remove(name_to_remove_from_bus)

                        print(self.bus_passenger) 

                    else:
                        #If user does not want to remove a passenger by name will remove a passenger by default    
                        self.bus_passenger.pop()
            else:
                break


def validate_string_input(in_parameter):
        
        #https://www.geeksforgeeks.org/python-check-if-string-contains-any-number/
        #falta validar si la string tiene un digito.

        while True:        

            try:
               user_entry = input(str(in_parameter))

               if len(user_entry) == 0:
                   
                   print('The value you have entered is empty')


               elif len(user_entry) > 0:

                    result = False

                    for i in user_entry:
                        try:
                            int(i)
                            result = True
                            print('The value you have entered is contains a digit number')
                            break
                        except:
                            result = False

                    if result == False:
                        break

               else:
                   
                   print('The string is not empty')

                   break
               
            except ValueError:
                
                print('The value enter is incorrect')
                continue 
            
        return user_entry

my_bus = Bus(5)


my_bus.add_passenger_to_bus()
my_bus.show_passenger()
my_bus.remove_passengers_from_bus()
