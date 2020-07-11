
# Helpers

def hMaxIndex(array, start, end):
    if start > end:
        start, end = end, start
    currMaxIndex = start
    for i in range(start+1, min(end+1, len(array))):
        if array[i] > array[currMaxIndex]:
            currMaxIndex = i
    return currMaxIndex

def hSubSum(array, start, end):
    subSum = 0
    if start > end:
        start, end = end, start
    for i in range(start+1, end):
        subSum += array[i]
    return subSum

# Solutions

def solution_optimal_with_memory(array):
    if len(array) <= 0:
        return 0

    waterLevel = []
    # Calculate left tallest bar for each index
    #  left to right
    runningMax = array[0]
    for item in array:
        runningMax = max(item, runningMax)
        waterLevel.append(runningMax)

    # Calculate right tallest bar for each index
    #  right to left, then calculate the min of
    #  the two tallest bars of the left and right
    runningMax = array[-1]
    for i in range(len(array)-1, -1, -1):
        runningMax = max(array[i], runningMax)
        waterLevel[i] = min(waterLevel[i], runningMax)

    # Knowing the left tallest and the right tallest bars
    #  calculate the volume of water at each spot
    totalVolume = 0
    for i in range(len(array)):
        totalVolume += (waterLevel[i] - array[i])
    return totalVolume


def solution_iterative(array):
    totalVolume = 0
    currMaxIndex = hMaxIndex(array, 0, len(array)-1)
    stack = [(currMaxIndex, -1, 0), (currMaxIndex, 1, len(array)-1)]

    while len(stack) > 0:
        currMaxIndex, delta, end = stack.pop()
        # print(currMaxIndex, delta, end)
        nextMaxIndex = hMaxIndex(array, currMaxIndex + delta, end)

        if currMaxIndex != nextMaxIndex and 0 <= nextMaxIndex and (nextMaxIndex+1) < len(array) and array[nextMaxIndex] > 0:
            stack.append((nextMaxIndex, delta, end))

        volume = min(array[currMaxIndex], array[nextMaxIndex]) * max(abs(currMaxIndex - nextMaxIndex) - 1, 0)
        volume -= hSubSum(array, currMaxIndex, nextMaxIndex)
        totalVolume += volume
    return totalVolume


testcases = [
    ([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0], 26),
    ([0, 0], 0),
    ([0, 1, 0], 0),
    ([0, 1, 1, 0], 0),
    ([1], 0),
    ([1, 1], 0),
    ([1, 1, 1], 0),
    ([1, 1, 1, 1], 0),
    ([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 5),
    ([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6], 15),
    ([6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1], 15),
    ([0, 0, 100, 0, 0, 0, 24, 0, 0, 7, 0, 0, 31, 0, 49, 52, 0, 0, 10, 0, 0, 0, 0, 70, 0, 0, 0], 1227),
]

for array, answer in testcases:
    print(array)
    # solution = solution_iterative(array)
    solution = solution_optimal_with_memory(array)
    print(solution, answer)
    assert(solution == answer)
