#!/usr/local/bin/python3

from math import inf


def binSearchClosestIndeces(array, start, end, value):

    # swap start and end if they
    #    are in opposite order
    if start > end:
        temp = start
        start = end
        end = temp

    if start == end:
        if array[start] < value:
            return (start, None)
        else:
            return (None, start)


    if value < array[start]:
        return (None, start)

    if value > array[end]:
        return (end, None)


    while True:
        mid = int( (start + end) / 2)

        if value < array[mid]:
            end = mid
        else:
            start = mid

        if start+1 == end:
            return (start, end)

def subSort(array):
    index = 0
    for i in range(1,len(array)):
        if array[i-1] > array[i]:
            index = i-1
            break

    indexRangeLeftEnd = index

    index = 0
    for i in range(len(array)-2,-1,-1):
        if array[i] > array[i+1]:
            index = i+1
            break

    indexRangeRightStart = index

    # Check if the array is already sorted
    if indexRangeRightStart == 0:
        return (0,0)

    midMin, midMax = inf, -inf

    indexStart = indexRangeLeftEnd+1
    indexEnd = indexRangeRightStart-1

    print( array[0:(indexRangeLeftEnd+1)], array[indexStart: (indexEnd+1)], array[indexRangeRightStart: len(array)])

    if indexStart < indexEnd:
        for i in range(indexStart, indexEnd+1):
            if array[i] < midMin:
                midMin = array[i]
            if array[i] > midMax:
                midMax = array[i]

    rangeMin = min(midMin, array[indexRangeRightStart])
    rangeMax = max(array[indexRangeLeftEnd], midMax)

    currIndex = indexRangeLeftEnd-1
    while 0 <= currIndex and rangeMin < array[currIndex]:
        currIndex -= 1
    indexStart = currIndex+1

    currIndex = indexRangeRightStart+1
    while currIndex < len(array) and rangeMax > array[currIndex]:
        currIndex += 1
    indexEnd = currIndex-1

    return (indexStart, indexEnd)





# Testcases V1

# testcases = [
#     [1,2,4,7,10,11,7,12,6,7,16,18,19],
#     [1,2,6,5,9,10]
# ]



# for t in testcases:
#     print(t)
#     print('SOLUTION: %s' % str(subSort(t)))

# print('====================================')

# Testcases V2

def permute(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	stack = [(l,0)]
	permutations = []
	while 0 < len(stack):
		currList, currIndex = stack.pop()
		if currIndex == L:
			sol = []
			for i in currList:
				sol.append(i)
			permutations.append(sol)
		else:
			for i in range(currIndex,L):
				currList[currIndex], currList[i] = currList[i], currList[currIndex]
				stack.append((currList[:], currIndex+1))
				currList[currIndex], currList[i] = currList[i], currList[currIndex]
	return permutations


testcases = permute([1,2,3,4])
# testcases = [
#     [3, 4, 2, 1]
# ]


for t in testcases:
    print('==============')
    # print(list(range(len(t))))
    print(t)
    print('SOLUTION: %s' % str(subSort(t)))

