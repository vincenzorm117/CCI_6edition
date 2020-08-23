from math import log2, ceil
from random import randint

class Heap:
    # Public Methods
    def __init__(self, compareFn=None):
        self.array = []
        if compareFn == None:
            self.compareFn = lambda x,y : x < y
        else:
            self.compareFn = compareFn

    def Add(self, entry):
        self.array.append(entry)
        self.percolateUp()

    def Peek(self):
        if self.Length() <= 0:
            return None
        return self.array[0]

    def Pop(self):
        if self.Length() <= 0:
            return None
        if self.Length() == 1:
            return self.array.pop()
        top = self.array[0] # save top for return
        self.array[0] = self.array.pop() # Move last to top
        self.percolateDown()
        return top

    def Length(self):
        return len(self.array)

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return str(self.array)

    # Private Methods

    def getParentIndex(self, index):
        if index % 2 == 0: # right child
            return int(index / 2) - 1
        else: # left child
            return int(index / 2)

    def hasParent(self, index):
        return index > 0

    def getLeftChild(self, index):
        return index * 2 + 1

    def getRightChild(self, index):
        return index * 2 + 2

    def swap(self, index0, index1):
        self.array[index0], self.array[index1] = self.array[index1], self.array[index0]

    def percolateUp(self):
        index = self.Length() - 1
        while self.hasParent(index):
            parentIndex = self.getParentIndex(index)
            if not self.compareFn(self.array[parentIndex], self.array[index]):
                self.swap(parentIndex, index)
            index = parentIndex

    def percolateDown(self):
        index = 0
        while True:
            leftIndex = self.getLeftChild(index)
            rightIndex = self.getRightChild(index)

            if 0 < leftIndex and leftIndex < self.Length():
                if 0 < rightIndex and rightIndex < self.Length():
                    if self.compareFn(self.array[leftIndex], self.array[rightIndex]):
                        minIndex = leftIndex
                    else:
                        minIndex = rightIndex
                else:
                    minIndex = leftIndex
            else:
                minIndex = None

            if minIndex == None:
                break

            if not self.compareFn(self.array[index], self.array[minIndex]):
                self.swap(index, minIndex)
                index = minIndex
            else:
                break



def getMedian(array):
    if len(array) <= 0:
        return None
    mid = int(len(array) / 2)
    if len(array) % 2 == 0:
        return (array[mid] + array[mid-1]) / 2
    return array[mid]


class ContinuousMedian:
    def __init__(self):
        self.top = Heap(lambda a,b : a > b)
        self.bottom = Heap(lambda a,b : a < b)
        self.length = 0

    def add(self, x):
        self.bottom.Add(x)
        self.length += 1
        # Keep looping as long as the tops largest is greater than the bottom's smallest or
        while abs(self.top.Length() - self.bottom.Length()) > 1 or ((self.top.Peek() == None or self.bottom.Peek() == None or self.top.Peek() > self.bottom.Peek()) and self.top.Peek() != None and self.bottom.Peek() != None):
            # Ensure top and bottom are size diff of at most 1
            if abs(self.top.Length() - self.bottom.Length()) > 1:
                if self.top.Length() > self.bottom.Length():
                    self.bottom.Add(self.top.Pop())
                else:
                    self.top.Add(self.bottom.Pop())
            # Ensure top is less than or equal to bottom
            elif self.top.Peek() > self.bottom.Peek():
                self.bottom.Add(self.top.Pop())

    def getMedian(self):
        # Return 0 if there is nothing
        if self.top.Length() <= 0 and self.bottom.Length() <= 0:
            return None
        #  if even return average of top and bottom
        if self.length % 2 == 0:
            return (self.top.Peek() + self.bottom.Peek()) / 2
        if self.top.Length() > self.bottom.Length():
            return self.top.Peek()
        else:
            return self.bottom.Peek()


cm = ContinuousMedian()
array = []


for _ in range(100000):
    newValue = randint(-100, 100)
    # Append new value to array and sort
    array.append(newValue)
    array.sort()
    # Add new value to ContinuousMedian instance.
    cm.add(newValue)
    # Check optimized median vs actual
    assert(cm.getMedian() == getMedian(array))

