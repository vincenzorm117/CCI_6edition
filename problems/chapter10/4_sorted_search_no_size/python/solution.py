#!/usr/local/bin/python3

from random import randint


def GenerateRandomList(length):
    listy = [randint(1,100)]
    for i in range(1,length-1):
        listy.append(listy[i-1] + randint(0,10))
    return listy

class Listy:
    def __init__(self, size):
        self.array = GenerateRandomList(size)

    def elementAt(self, index):
        if index < 0 or len(self.array) <= index:
            return -1
        return self.array[index]


def searchListy(listy, value):
    count = [0,0]
    index = 1
    while listy.elementAt(index) != -1:
        count[0] += 1
        index *= 2
    low, high = 0, index
    while low < high:
        count[1] += 1
        # print(low, high)
        mid = int((low + high) / 2)
        arrayValue = listy.elementAt(mid)
        if arrayValue == value:
            print('Loop Iterations: %s.' % count, end=" ")
            return mid
        if arrayValue == -1:
            high = mid
        else:
            if value < arrayValue:
                high = mid
            else:
                low = mid+1
    print('Loop Iterations: %s.' % count, end=" ")
    return None

            



listy = Listy(1000)
print(listy.array)
for x in listy.array:
    print('Search: %s.' % x, end=" ")
    index = searchListy(listy, x)
    print(index)
    assert(listy.elementAt(index) == x)