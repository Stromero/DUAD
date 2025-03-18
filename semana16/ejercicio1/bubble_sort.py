def bubble_sort_list(list_to_sort):
        if isinstance(list_to_sort,list):
            for external_index in range(0,len(list_to_sort)-1):
                for index in range(0,len(list_to_sort)-1):

                    current_element = list_to_sort[index]
                    next_element = list_to_sort[index+1]

                    if(current_element > next_element):
                        list_to_sort[index] = next_element
                        list_to_sort[index+1] = current_element
        
            return list_to_sort
    
        raise ValueError('Sort method is not working because input is not a list')

