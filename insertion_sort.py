def insertion_sort(arr):
    for j in range(1,len(arr)):
        for i in range(j,0,-1):
            while arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]             
    return arr
arr=[3,4,6,7,2,1,8,9,5]
print(insertion_sort(arr))