def binary_search(array,searching_value):
    low = 0
    high = len(array)-1
    while low<=high:
        mid = (low+high) // 2
        if searching_value== array[mid]:
            return "found"
        elif searching_value < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "not found"

array= [2,4,6,7,99,100,111,120]
searching_value =101
result = binary_search(array,searching_value)

print(str(searching_value) +" " + result)
