def selection_sort(arr):
    x = 0
    for j in range(0, len(arr)):
        min = arr[j]
        for i in range(0+j, len(arr)):
            if arr[i] < min:
                min = arr[i]
                x = i
        arr[j], arr[x] = arr[x], arr[j]
    return arr
                

arr=[3,4,6,7,2,1,8,9,5]
print(selection_sort(arr))
