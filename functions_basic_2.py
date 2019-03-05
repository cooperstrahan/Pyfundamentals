def countdown(num):
    newList = []
    while num >= 0:
        newList.append(num)
        num = num -1
    return newList
print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

def first_plus_length(l):
    return len(l) + l[0]
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    newList = []
    count = 0
    for val in range(0, len(lst)):
        if lst[val] > lst[1]:
            newList.append(lst[val])
            count=count+1
    print(count)
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(a,b):
    newList = []
    for i in range(0, a):
        newList.append(b)
    return newList

print(length_and_value(4,7))
print(length_and_value(6,2))
