def reverse_bubble_sort(list_to_sort):
    
    for external_index in range(0, len(list_to_sort) - 1):

        position_last_element = len(list_to_sort)-1
        position_previous_element = position_last_element - 1

        for index in range(0, len(list_to_sort) - 1):

            current_element = list_to_sort[position_last_element]
            
            previous_element = list_to_sort[position_previous_element]
            
            print(f'External Iteration is: {external_index}, Internal Iteration is: {index}, current element is: {current_element} and previous element is: {previous_element}')

            if current_element < previous_element:
                list_to_sort[position_last_element] = previous_element
                list_to_sort[position_previous_element] = current_element
                position_last_element -= 1
                position_previous_element -= 1

            print(list_to_sort) 


           

my_list = [10,9,8,7,6,5,4,3,2,1]
reverse_bubble_sort(my_list)