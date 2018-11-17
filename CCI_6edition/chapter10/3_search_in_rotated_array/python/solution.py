#!/usr/local/bin/python3


def search(array, value):
    # Do binary search to find offset)
    low, high = 0, len(array) - 1
    if array[low] > array[high]:
        while low < high:
            mid = int((low + high)/2)
            if array[low] > array[mid]:
                high = mid
            else:
                low = mid+1
        offset = (low) % len(array)
    else:
        offset = 0
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
    ([15,16,19,20,25,1,3,4,5,7,10,14], 5, 8),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 7, 9),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 10, 10),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 14, 11),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 15, 0),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 16, 1),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 19, 2),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 20, 3),
    ([15,16,19,20,25,1,3,4,5,7,10,14], 25, 4),
    

    ([1,3,4,5,7,10,14,15,16,19,20,25], 1, 0),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 3, 1),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 4, 2),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 5, 3),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 7, 4),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 10, 5),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 14, 6),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 15, 7),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 16, 8),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 19, 9),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 20, 10),
    ([1,3,4,5,7,10,14,15,16,19,20,25], 25, 11),
    
]


for case, value, solution in testcases:
    print('Case: %s' % case)
    answer = search(case, value)
    print(answer, solution)
    assert(solution == answer)
