
from random import shuffle

########################################
# Helpers

def generatePosibilities(largestSize, alphabet):
    for size in range(largestSize + 1):
        stack = [([], 0)]
        while len(stack) > 0:
            array, index = stack.pop()
            if len(array) >= size:
                yield array
            else:
                for item in alphabet:
                    stack.append((array+[item], index+1))

def permute_no_dups(l):
    if not isinstance(l, (list)):
        return None
    if len(l) <= 0:
        return []
    L = len(l)
    mp = {}
    for c in l:
        if c not in mp:
            mp[c] = 0
        mp[c] += 1
    keys = mp.keys()
    q = [([], L, mp)]
    while 0 < len(q):
        pre, k, mp = q.pop()
        if k == 0:
            yield pre
            continue
        for c in keys:
            count = mp[c]
            if 0 < count:
                mp[c] = count - 1
                q.append((pre + [c], k - 1, mp.copy()))
                mp[c] = count

def swap(array, index0, index1):
    array[index0], array[index1] = array[index1], array[index0]


def partition(array, low, high):
    if low >= high:
        return high
    # Partition all elements in range except pivot
    pivot = array[low]
    left = low+1
    right = high
    while left < right:
        if array[left] < pivot:
            left += 1
        else:
            swap(array, left, right)
            right -= 1
    # Move pivot into place
    if array[left] < pivot:
        swap(array, low, left)
        return left
    else:
        swap(array, low, left-1)
        return left-1



def quicksort(array):
    stack = [(0, len(array)-1)]
    while len(stack) > 0:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = partition(array, low, high)
        stack.append((low, pivot-1))
        stack.append((pivot+1, high))
    return array

########################################
# Solutions

def solution_brute_force(array, K):
    if K == 0:
        return None
    for i in range(K):
        indexSmallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[indexSmallest]:
                indexSmallest = j
        swap(array, i, indexSmallest);
    return array[0:K]


def solution_optimized(array, K):
    if K == 0:
        return None
    stack = [(0, len(array)-1)]
    while len(stack) > 0:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = partition(array, low, high)
        if pivot > K:
            stack.append((low, pivot-1))
        else:
            stack.append((pivot+1, high))
    return array[0:K]


########################################
# Manual Testcases

testcases = [
    [4, 19, 10, 6, 20, 11, 16, 3, 15, 13, 5, 1, 2, 12, 14, 9, 21, 17, 0, 22, 7, 18, 8],
    [4, 4, 4, 19, 10, 6, 20, 11, 16, 3, 15, 13, 5, 1, 2, 12, 14, 9, 21, 17, 0, 22, 7, 18, 8],
    [1,1,1,1,1,1],
    [1,1,1,1,2,3,4,5,8,10,27,56]
]

for array in testcases:
    for k in range(1, len(array)):
        answer = solution_brute_force(array, k)
        solution = solution_optimized(array, k)
        solution.sort()
        assert(answer == solution)



for array in permute_no_dups([1,1,1,2,3,4,5,8,10,27,56]):
    for i in range(1, len(array)):
        answer = solution_brute_force(array, k)
        solution = solution_optimized(array, k)
        solution.sort()
        assert(answer == solution)


########################################
# Generate Testcases


for array in generatePosibilities(7, [1,2,3,6,20,52]):
    for k in range(1, len(array)):
        answer = solution_brute_force(array, k)
        solution = solution_optimized(array, k)
        solution.sort()
        assert(answer == solution)