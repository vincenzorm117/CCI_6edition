#!/usr/local/bin/python3



def bruteSmallestDifference(A,B):
    sfA = A[0]
    sfB = B[0]
    diff = abs(sfA - sfB)
    for a in A:
        for b in B:
            if abs(a - b) < diff:
                sfA, sfB = a, b
                diff = abs(sfA - sfB)
    return (sfA,sfB)



def smallestDifference(A,B):
    # Sort both arrays
    A.sort()
    B.sort()
    # Init min values
    minA = A[0]
    minB = B[0]
    diff = abs(minA - minB)
    # Find smallest values
    i,j = 0,0
    while i < len(A) and j < len(B):
        if abs(A[i] - B[j]) < diff:
            minA = A[i]
            minB = B[j]
            diff = abs(minA - minB)
        if A[i] <= B[j]:
            i += 1
        else:
            j += 1
    return (minA, minB)
    

testcases = [
    ([1,3,15,11,2],
    [23,127,235,19,8]),

    ([1,2],
    [3,2]),

    ([1,2],
    [3]),

    ([2],
    [3]),

    ([1,3,5,7],
    [2,4,6,8]),

    ([1,2,3,4],
    [9,10,11,12]),
]

for i in range(len(testcases)):
    A, B = testcases[i]
    print('\nCase: %s' % i)
    print(A)
    print(B)
    answer = bruteSmallestDifference(A,B)
    solution = smallestDifference(A,B)
    print(answer, solution)
    assert(
        (answer[0] == solution[0] and answer[1] == solution[1])
        or (answer[0] == solution[1] and answer[1] == solution[0])
    )