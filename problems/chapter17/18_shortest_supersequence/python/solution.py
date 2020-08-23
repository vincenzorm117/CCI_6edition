from random import randint
import heapq
from math import inf

def solution_brute_force(short, long):
    for length in range(len(short), len(long)+1):
        for startIndex in range(len(long) - length+1):
            currNums = set()
            endIndex = startIndex + length
            for i in range(startIndex, endIndex):
                currNums.add(long[i])
            hasAllNums = True
            for item in short:
                if item not in currNums:
                    hasAllNums = False
                    break
            if hasAllNums:
                return (startIndex, endIndex-1)

def hGetSize(tup):
    if tup == None:
        return None
    start, end = tup
    return end - start + 1

def hGetMin(startA, endA, startB, endB):
    if endA - startA < endB - startB:
        return (startA, endA)
    else:
        return (startB, endB)

def solution_optimized(short, long):
    # Create heaps to track the numbers from short in long
    heaps = {}
    for item in short:
        heaps[item] = []

    # Loop through long and save each index of all items in short
    for i in range(len(long)):
        item = long[i]
        if item in heaps:
            heap = heaps[item]
            heapq.heappush(heap, i)

    # Use currIndecesHeap as a Heap to track the startIndex and use endIndex to track the end
    currIndecesHeap = []
    endIndex = -inf
    # Retrieve the startIndex and endIndex of the first subsequence of long
    #  containing all values from short.
    for item in heaps:
        # Get the first instance of each item
        index = heapq.heappop(heaps[item])
        # Add item to currIndecesHeap to track it
        heapq.heappush(currIndecesHeap, index)
        # Updat/set endIndex to the largest index
        endIndex = max(endIndex, index)

    # Calculate max
    minSizeIndeces = (currIndecesHeap[0], endIndex)

    while True:
        # Get next number to remove
        indexToRemove = heapq.heappop(currIndecesHeap)
        currNum = long[indexToRemove]
        # Check if number is the last instance in long
        if len(heaps[currNum]) == 0:
            break
        # Pop from currIndecesHeap
        nextIndex = heapq.heappop(heaps[currNum])
        # Add nextIndex to our currently tracked indeces
        heapq.heappush(currIndecesHeap, nextIndex)
        # Update endIndex
        endIndex = max(endIndex, nextIndex)
        # Update min
        minSizeIndeces = hGetMin(minSizeIndeces[0], minSizeIndeces[1], currIndecesHeap[0], endIndex)

    return minSizeIndeces


testcases = [
    (
        [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7],
        set([1, 5, 9])
    )
]

for long, short in testcases:
    sol1 = solution_brute_force(short, long)
    sol2 = solution_optimized(short, long)
    # print('short: ', len(short), short)
    # print('long: ', len(long), long)
    # print('sol1', hGetSize(sol1), sol1)
    # print('sol2', hGetSize(sol2), sol2)
    assert(hGetSize(sol1) == hGetSize(sol2))


for longSize in range(10, 100, 5):
    for _ in range(100):
        long = [randint(0,20) for _ in range(longSize)]
        shortSuper = list(set(long))
        for shortSize in range(2, len(shortSuper)):
            short = set(shortSuper[0:shortSize])
            # Run testcases
            sol1 = solution_brute_force(short, long)
            sol2 = solution_optimized(short, long)
            # print('short: ', len(short), short)
            # print('long: ', len(long), long)
            # print('sol1', hGetSize(sol1), sol1)
            # print('sol2', hGetSize(sol2), sol2)
            assert(hGetSize(sol1) == hGetSize(sol2))

