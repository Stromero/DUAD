# my_value = '18'

# if isinstance(my_value,int) and my_value >= 0 :
#     print('is numeric')
# else:
#     print('Not numeric')

try:
    user_input = int(input("Enter an integer: "))
    print("User input is an integer")
except ValueError:
    print("User input is not an integer")
