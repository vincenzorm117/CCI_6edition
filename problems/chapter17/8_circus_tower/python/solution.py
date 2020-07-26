
def isInOrder(personA, personB):
    return personA[0] < personB[0] and personA[1] < personB[1]


def solution_brute_force(people):
    people.sort()

    largest = []
    stack = [([], 0)]

    while len(stack) > 0:
        currArray, index = stack.pop()
        # Check if reached end
        if index >= len(people):
            if len(largest) < len(currArray):
                largest = currArray
            continue

        if len(currArray) <= 0 or isInOrder(currArray[-1], people[index]):
            stack.append((currArray, index+1))
            stack.append((currArray + [people[index]], index+1))
        else:
            stack.append((currArray, index+1))

    return largest


# def solution_optimized(people):
#     people.sort()

#     largest = []
#     stack = [([], 0)]

#     while len(stack) > 0:
#         currArray, index = stack.pop()

#         # Check if reached end
#         if index >= len(people):
#             if len(largest) < len(currArray):
#                 largest = currArray
#             continue

#         if len(currArray) <= 0 or isInOrder(currArray[-1], people[index]):
#             stack.append((currArray, index+1))
#             stack.append((currArray + [people[index]], index+1))
#         else:
#             stack.append((currArray, index+1))

#     return largest


def findIndexMaxFirst(array):
    maxIndex = 0
    for i in range(1, len(array)):
        if array[maxIndex][0] < array[i][0]:
            maxIndex = i
    return maxIndex

def solution_optimized(people):
    if len(people) <= 0:
        return people
    people.sort(reverse=True)
    memo =  [[0,0] for x in range(len(people))]
    for i in range(len(people)-1, -1, -1):
        maxHeightIndex = i
        for j in range(i+1, len(people)):
            if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
                if memo[maxHeightIndex][0] < memo[j][0]:
                    maxHeightIndex = j
        memo[i][0] = memo[maxHeightIndex][0] + 1
        memo[i][1] = maxHeightIndex

    maxIndex = findIndexMaxFirst(memo)
    lisArray = []
    stack = [maxIndex]
    while len(stack) > 0:
        currIndex = stack.pop()
        lisArray.append(people[currIndex])
        if memo[currIndex][1] != currIndex:
            stack.append(memo[currIndex][1])
    return lisArray




testcases = [
    [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)],
    [(75,190), (71, 192), (67, 187), (66, 191)],
]


def generateTestcase(largestSize):
    for size in range(largestSize + 1):
        stack = [([], 0)]
        while len(stack) > 0:
            array, index = stack.pop()
            if len(array) >= size:
                yield array
            else:
                for i in range(1,11):
                    stack.append((array+[(index,i)], index+1))




for people in testcases:
    print('======================')
    print(people)
    answer = solution_brute_force(people)
    print(answer)
    solution = solution_optimized(people)
    print(solution)
    assert(len(answer) == len(solution))



for people in generateTestcase(10):
    print('======================')
    print(people)
    answer = solution_brute_force(people)
    # print(answer)
    solution = solution_optimized(people)
    # print(solution)
    assert(len(answer) == len(solution))