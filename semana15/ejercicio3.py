# Ejercicio 1 de análisis de algoritmos
# Analice el algoritmo de bubble_sort usando la Big O Notation

def bubble_sort(list_to_sort): 

    for external_index in range(0,len(list_to_sort) - 1): # O (log n)

        for index in range(0,len(list_to_sort) - 1): # O (log n)

            current_element = list_to_sort[index] # O (n)

            next_element = list_to_sort[index + 1] # O (n)

            print(f'Iteracion externa {external_index}, iteracion interna {index}, elemento actual {current_element}, siguiente elemento {next_element}') # O (1)

            if current_element > next_element: # O (n)

                list_to_sort[index] = next_element # O (n)

                list_to_sort[index + 1 ] = current_element # O (n)

                print(list_to_sort) # O (1) 

my_list_to_sort = [18, -23, 96, 35, 2, -4, 86, 96, 52, 41] # O (1)
bubble_sort(my_list_to_sort) # O (1)

print(my_list_to_sort) # O (1)