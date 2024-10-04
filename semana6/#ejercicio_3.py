#ejercicio_3
#Cree una función que retorne la suma de todos los numeros de una lista

def sum_numbers(number_list):
    final_sum = 0
    for item in number_list:
        final_sum = final_sum + item
    print(final_sum)

def main():
    number_list = [4,6,2,29]
    sum_numbers(number_list)

#if __name__ == "__main__":
main()
#