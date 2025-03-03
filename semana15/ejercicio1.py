# 1.Crea un bubble_sort por tu cuenta sin revisar el codigo de la leccion anterior

def bubble_sort(list_to_sort):

    for external_index in range(0,len(list_to_sort) - 1):

        for index in range(0,len(list_to_sort) - 1):

            current_element = list_to_sort[index]

            next_element = list_to_sort[index + 1]

            print(f'Iteracion externa {external_index}, iteracion interna {index}, elemento actual {current_element}, siguiente elemento {next_element}')

            if current_element > next_element:

                list_to_sort[index] = next_element

                list_to_sort[index + 1 ] = current_element

                print(list_to_sort)    

my_list_to_sort = [18, -23, 96, 35, 2, -4, 86, 96, 52, 41]
bubble_sort(my_list_to_sort)

print(my_list_to_sort)