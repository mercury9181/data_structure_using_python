def linearSearch(item_list, searching_value):
    index_of_current_item = 0
    flag = False
    while index_of_current_item<len(item_list) and not flag:
        if item_list[index_of_current_item] == searching_value:
            flag= True
        else:
            index_of_current_item = index_of_current_item + 1
    return flag


item_list= [31,54,23,54,667,43,56,22]
key=666
decision = linearSearch(item_list,key)
if decision:
    print(str(key)+" was found ")
else:
    print(str(key)+" Not found ")