#!/usr/local/bin/python3


def GetMaxIndex(array, index):
    maxIndex = index
    if array[maxIndex] < array[index+1]:
        maxIndex = index+1
    if array[maxIndex] < array[index+2]:
        maxIndex = index+2
    return maxIndex


def peaks_and_valleys(array):
    for i in range(0,len(array)-2, 2):
        # Grab index of largest element in triplet
        maxIndex = GetMaxIndex(array, i)
        # Swap max index with middle element of triplet
        temp = array[maxIndex]
        array[maxIndex] = array[i+1]
        array[i+1] = temp
    
    if len(array) % 2 == 0:
        lastIndex = len(array) - 1
        if array[lastIndex] < array[lastIndex-1]:
            temp = array[lastIndex]
            array[lastIndex] = array[lastIndex-1]
            array[lastIndex-1] = temp
    return array









testcases = [
    [5, 3, 1, 2, 3],
    [5, 3, 1, 1, 2, 3],
    [5, 3, 1, 1, 2, 0]
]

for t in testcases:
    print(t)
    print(peaks_and_valleys(t))