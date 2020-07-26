


def compare(array, A, B):
    return array[A] < array[B]

def longest_increasing_subsequence(array):
    def recurse(index):
        global R
        nonlocal array, memo
        R += 1
        maxHeight = 0
        for i in range(index+1, len(array)):
            if compare(array, index, i):
                value = memo[i] if i in memo else recurse(i)
                maxHeight = max(maxHeight, value)
        maxHeight += 1
        memo[index] = maxHeight
        return maxHeight
    maxHeight = 0
    memo = {}
    for i in range(len(array)):
        maxHeight = max(maxHeight, recurse(i))
    print(memo)
    return maxHeight


def longest_increasing_subsequence2(array):
    def recurse(index):
        nonlocal array, memo
        maxHeight = 0
        for i in range(index-1, -1, -1):
            if array[index] > array[i]:
                value = memo[i] if i in memo else recurse(i)
                maxHeight = max(maxHeight, value)
        maxHeight += 1
        memo[index] = maxHeight
        return maxHeight
    maxHeight = 0
    memo = {}
    for i in range(len(array)-1,-1,-1):
        maxHeight = max(maxHeight, recurse(i))
    print(memo)
    return maxHeight

def longest_increasing_subsequence_iterative(array):
    memo = [0] * len(array)
    for i in range(len(array)-1, -1, -1):
        maxHeight = 0
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                maxHeight = max(maxHeight, memo[j])
        memo[i] = maxHeight + 1
    return max(memo)

def maxFirstIndex(array):
    maxIndex = 0
    for i in range(1, len(array)):
        if array[maxIndex][0] < array[i][0]:
            maxIndex = i
    return maxIndex


def longest_increasing_subsequence_iterative_vector(array):
    memo =  [[0,0] for x in range(len(array))]
    for i in range(len(array)-1, -1, -1):
        maxHeightIndex = i
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                if memo[maxHeightIndex][0] < memo[j][0]:
                    maxHeightIndex = j
        memo[i][0] = memo[maxHeightIndex][0] + 1
        memo[i][1] = maxHeightIndex

    maxIndex = maxFirstIndex(memo)
    lisArray = []
    stack = [maxIndex]
    while len(stack) > 0:
        currIndex = stack.pop()
        lisArray.append((currIndex, array[currIndex]))
        if memo[currIndex][1] != currIndex:
            stack.append(memo[currIndex][1])
    return lisArray



[1, 2, 3, 1, 43, 10, 330, 5, 6, 7, 8, 9, 10, 0, 100, 23]

testcases = [
    [1,2,3,1,43,10,330,5,6,7,8,9,10,0,100,23],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

for testcase in testcases:
    print(testcase)
    print(longest_increasing_subsequence_iterative_vector(testcase))


