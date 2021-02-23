def selection_sort(a):
    for i in range(len(a)-1,0,-1):
        max_position = 0
        for j in range(1, i+1):
            if a[j]>a[max_position]:
                max_position = j
        a[i], a[max_position] = a[max_position], a[i]



array = [84,21,96,15,47]
print(array)
selection_sort(array)
print(array)