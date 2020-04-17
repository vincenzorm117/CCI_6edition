#!/usr/local/bin/python3

############################################################
############################################################
# Helpers

# Based on the formula above and some algebra we
# know the following to be true
def hasSumSwap(A,B):
    # Get sum of A
    sumA = 0
    for a in A:
        sumA += a
    # Get sum of B
    sumB = 0
    for b in B:
        sumB += b
    # Get diff of sums
    return (sumA - sumB) % 2 == 0


############################################################
############################################################
# Brute force solution

def sumSwapBrute(A,B):
    sumA = 0
    for a in A:
        sumA += a
    sumB = 0
    for b in B:
        sumB += b
    for a in A:
        for b in B:
            if sumA - a + b == sumB - b + a:
                return (a,b)


############################################################
############################################################
# Solution

# By property we have for some a in A and some b in B that:
# sumA - a + b = sumB - b + a
# we do some algebra and we have:
# sumA - sumB = 2a - 2b (let: sumA - sumB = diff)
# 2a - diff = 2b
# Now we can use this formula (2a - diff = 2b) below:
def sumSwap(A,B):

    sumA = sum(A)
    sumB = sum(B)

    # If the difference of the sums are not divisible by 0
    #   there are no numbers that can be swapped
    if (sumA - sumB) % 2 != 0:
        return None

    # Get diff of sums
    diff = sumA - sumB
    # Save diffs of diff and a to check with b
    diffs = {}
    for a in A:
        diffs[2*a - diff] = a
    # See if we've seen
    for b in B:
        if (2*b) in diffs:
            return (diffs[2*b], b)
    return None



testcases = [
    (
        [4,1,2,1,1,2],
        [3,6,3,3],
        (1,3)
    ),
    (
        [1,1],
        [1,1],
        (1,1)
    ),
    (
        [1,2,3],
        [1,1,5],
        None
    ),
    (
        [0,3,4],
        [1,1,5,0],
        (0,0)
    ),
    (
        [1,1,1,1,1,1],
        [0,4],
        (1,0)
    ),
]


for i in range(len(testcases)):
    A,B,answer = testcases[i]
    print('\nCase %s' % i)
    print('Solution:', end=' ')
    print(sumSwap(A,B))
    print('Answer:', end=" ")
    print(answer)