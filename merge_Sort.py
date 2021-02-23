def merge_sort(list_needs_to_be_sort):
    if len(list_needs_to_be_sort) < 2:
        return list_needs_to_be_sort

    mid_index= len(list_needs_to_be_sort)//2
    left = list_needs_to_be_sort[:mid_index]
    right = list_needs_to_be_sort[mid_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)


    sorted_list =[]
    current_left_index = 0
    current_right_index = 0


    while len(sorted_list) < len(left) + len(right):
        if ((current_left_index< len(left)) and 
                (current_right_index ==len(right) or
                sorted_left[current_left_index] < sorted_right[current_right_index])):
            sorted_list.append(sorted_left[current_left_index])
            current_left_index= current_left_index + 1 
        
        else:
            sorted_list.append(sorted_right[current_right_index])
            current_right_index += 1
    return sorted_list

a= [10,2,100,70,34]
print(a)

print("sorted list" , merge_sort(a))


