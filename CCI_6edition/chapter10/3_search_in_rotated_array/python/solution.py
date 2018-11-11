#!/usr/local/bin/python3


def search(array, value):
    # Do binary search to find offset
    low, high = 0, len(array) - 1
    while low < high:
        mid = int((low + high)/2)
        if array[low] > array[mid]:
            high = mid
        else:
            low = mid+1
    offset = low
    # Do binary search to find index of input
    low, high = 0, len(array)
    while low < high:
        mid = int((low + high)/2)
        shiftedMid = (mid + offset) % len(array)
        if value < array[shiftedMid]:
            high = mid
        else: 
            low = mid+1
    return (low + offset - 1) % len(array)





testcases = [
    ([15,16,19,20,25,1,3,4,5,7,10,14], 5, 8)
]

array, value, solution = ([15,16,19,20,25,1,3,4,5,7,10,14], 5, 8)
for a in array:
    print('Case: %s' % a)
    print(search(array, a))

# for case, value, solution in testcases:
#     print('Case: %s' % case)
#     print(search(case, value), solution)
