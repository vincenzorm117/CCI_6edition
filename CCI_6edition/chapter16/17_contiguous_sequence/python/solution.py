#!/usr/local/bin/python3



def largest_contiguous_subsequence(sequence):
    if len(sequence) <= 0:
        return 0
    sum = 0
    max_sum = sequence[0] 
    for value in sequence:
        sum += value
        if max_sum < sum:
            max_sum = sum
        elif sum < 0:
            sum = 0
    return max_sum


testcases = [
    ([5,-2,1,-3,100], 101),
    ([5,6,0,-10,-2,11,-5,-6,15], 15),
    ([5,-9,6,-2,3], 7),
    ([-1,-2,-3,-4], -1)
]

for sequence, solution in testcases:
    value = largest_contiguous_subsequence(sequence)
    print(sequence)
    print(solution, value)
    assert(solution == value)


