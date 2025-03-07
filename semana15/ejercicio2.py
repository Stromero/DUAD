def reverse_bubble_sort(list_to_sort):
    
    for external_index in range(len(list_to_sort) - 1):
        #print(f'External index: {external_index}')
        for index in range(len(list_to_sort) - 1, 0, -1):
           #print(f'Index is: {index}')
            if(list_to_sort[index] < list_to_sort[index-1]):
                temp = list_to_sort[index-1]
                list_to_sort[index-1] = list_to_sort[index]
                #print(list_to_sort)
                list_to_sort[index] = temp
                #print(list_to_sort)
            
my_list = [10,9,8,7,6]
reverse_bubble_sort(my_list)
print(my_list)


