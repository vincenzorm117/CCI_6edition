#!/usr/local/bin/python3


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def sortSelection(array):
    for i in range(len(array)-1):
        minIndex = i
        # Find the minIndex
        for j in range(i+1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        # Swap minIndex and i
        swap(array, minIndex, i)
    return array



def sortBubble(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
    return array


def sortInsertion(array):
    for i in range(1, len(array)):
        temp = array[i]
        minIndex = i
        for j in range(i, -1, -1):
            minIndex = j
            if array[j - 1] < temp:
                break
            array[j] = array[j - 1]
        array[minIndex] = temp
    return array


def sortQuickSort(array):
    pass
    # def merge(array, leftLow, leftHigh, rightLow, rightHigh):
    #     while leftLow < leftHigh and rightLow < rightHigh:
    #         if array[leftLow]


def sortRadix(array):
    pass


def sortMergeSort(array):
    pass

def binarySearch(array, value):
    low, high = 0, len(array)
    while low < high:
        mid = int((low + high) / 2)
        if value == array[mid]:
            return array[mid]
        elif value < array[mid]:
            high = mid
        else:
            low = mid
    return None



print(sortSelection(list(range(55,10,-2))))
print(sortBubble(list(range(55,10,-2))))
print(sortInsertion(list(range(55,10,-2))))