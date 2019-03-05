def biggie_size(list):
    for i in range(0, len(list)):
        if list[i] > 0:
            list[i] = 'big'
    return list
print(biggie_size([-1, 3, 5, -5]))

def count_positives(list):
    count = 0
    for i in range(0,len(list)):
        if list[i] > 0:
            count = count + 1
    list[len(list)-1] = count
    return list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(list):
    total = 0
    for i in range(0,len(list)):
        total += list[i]
    return total
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

def average(list):
    total = 0
    for i in range(0,len(list)):
        total += list[i]
    return total/len(list)
print(average([1,2,3,4]))

def length(list):
    count = 0
    for x in list:
        count += 1
    return count
print(length([37,2,1,-9]))
print(length([]))

def min(list):
    if len(list) == 0:
        return False
    min = list[0]
    for x in range(1,len(list)):
        if list[x] < min:
            min = list[x]
    return min
print(min([37,2,1,-9]))
print(min([]))

def ultimate_analysis(list):
    max = list[0]
    min = list[0]
    sum = list[0]
    for x in range(1,len(list)):
        sum += list[x]
        if list[x] > max:
            max = list[x]
        if list[x] < min:
            min = list[x]
    d = {'sumTotal':sum, 'average':sum/len(list), 'minimum':min, 'maximum':max, 'length':len(list)}
    return d
print(ultimate_analysis([37,2,1,-9]))

def reverse_list(list):
    for i in range(0,int(len(list)/2)):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
print(reverse_list([37,2,1,-9]))