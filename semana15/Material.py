# def bubble_sort(list_to_sort):
#     for index in range(0,len(list_to_sort)):
#         #We save the values of the current element and next one
#         current_element = list_to_sort[index]
#         next_element = list_to_sort[index + 1]

#         print(f'-- Iteración {index}. elemento actual: {current_element}, siguiente elemento: {next_element}')

# my_test_list = [18, -11, 68, 6, 32, 53 -2]
# bubble_sort(my_test_list)

# print(my_test_list)


#
# -----------------------------------------------------------------------------------------------------------
#

# def bubble_sort(list_to_sort):
#     for index in range(0,len(list_to_sort)-1):
#         #We save the values of the current element and next one
#         current_element = list_to_sort[index]
#         next_element = list_to_sort[index + 1]

#         print(f'-- Iteración {index}. elemento actual: {current_element}, siguiente elemento: {next_element}')

# my_test_list = [18, -11, 68, 6, 32, 53, -2]
# bubble_sort(my_test_list)

# print(my_test_list)

#
# ------------------------------------------------------------------------------------------------------------
#

#
#-------------------------------------------------------------------------------------------------------------
#Este es el algortimo de ordenamiento
#
# def bubble_sort(list_to_sort):
#     #le restamos uno al largo de la lista para detener el ciclo en el penultimo elemento.
#     for index in range(0, len(list_to_sort)-1):
#         #Guardamos los valores del elemento actual y el siguiente
#         current_element = list_to_sort[index]
#         next_element = list_to_sort[index + 1]

#         print(f'--Iteración {index}. elemento actual: {current_element}, siguiente elemento {next_element}')

#         if current_element > next_element:
#             print('El elemento actual es mayor al siguiente, intercambiandolos...')
#             list_to_sort[index] = next_element
#             list_to_sort[index + 1] = current_element

# my_list = [18, -11, 68, 6, 32, 53, -2]
# bubble_sort(my_list)

# print(my_list)

# ----------------------------------------------------------------------------------------------------------------
# Algoritmo 
# ----------------------------------------------------------------------------------------------------------------

# def bubble_sort(list_to_sort):

# 	for outer_index in range(0, len(list_to_sort) - 1 ):

# 		for index in range(0, len(list_to_sort) - 1 ):

# 			current_element = list_to_sort[index]

# 			next_element = list_to_sort[index + 1]

# 			print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, siguiente elemento: {next_element}')

# 			if current_element > next_element:
# 				print('El elemento actual es mayor al siguiente. Intercambiandolos...')
# 				list_to_sort[index] = next_element
# 				list_to_sort[index + 1] = current_element

# my_list_to_sort = [18, -11, 68, 6, 32, 53, -2]
# bubble_sort(my_list_to_sort)

# print(my_list_to_sort)

# ---------------------------------------------------------
# 
# ---------------------------------------------------------

def bubble_sort(list_to_sort):

	for outer_index in range(0, len(list_to_sort) - 1 ):

		has_made_changes = False

		for index in range(0, len(list_to_sort) - 1 - outer_index ):

			current_element = list_to_sort[index]

			next_element = list_to_sort[index + 1]

			print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, siguiente elemento: {next_element}')

			if current_element > next_element:

				print('El elemento actual es mayor al siguiente. Intercambiandolos...')

				list_to_sort[index] = next_element

				list_to_sort[index + 1] = current_element

				has_made_changes = True

		if not has_made_changes:
			return

my_list_to_sort = [18, -11, 68, 6, 32, 53, -2]

bubble_sort(my_list_to_sort)

print(my_list_to_sort)
