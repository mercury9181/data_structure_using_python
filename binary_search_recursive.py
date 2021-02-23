def binary_search(array,searching_value,low,high):
    if low >high:
        return "Not found"
    else:
        mid = (low + high) //2
        if searching_value == array[mid]:
            return "Found"
        elif searching_value < array[mid]:
            return binary_search(array,searching_value,low,mid-1)
        else:
            return binary_search(array,searching_value,mid+1,high)



array= [2,4,6,7,99,100,111,120]
searching_value =111
result = binary_search(array,searching_value,0,len(array)-1)

print(str(searching_value) +" " + result)
