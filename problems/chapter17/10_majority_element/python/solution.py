
# O(n)
def solution_brute_force(array):
    items = set(array)
    for item in items:
        if array.count(item) > int(len(array)/2):
            return item
    return -1




def solution_optimized(array):
    if len(array) <= 0:
        return -1

    index = 1
    num = array[0]
    countMatch = 1
    countNoMatch = 0

    while index < len(array):
        # Update counts
        if array[index] == num:
            countMatch += 1
        else:
            countNoMatch += 1
        # Update num if matches are less than no matches
        if countMatch <= countNoMatch:
            # if index < len(array):
            num = array[index]
            countMatch = 1
            countNoMatch = 0
        # Update index
        index += 1

    if array.count(num) > int(len(array)/2):
        return num
    return -1



testcases = [
    [3],
    [3,1,3],
    [3,1,3,1,3],
    [3,1,3,1,3,1,3],
    [3,1,3,1,3,1,3,1,3],
    [3,1,3,1,3,1,3,1,3,1,3],
    [3,1,3,1,3,1,3,1,3,1,3,1,3],
    [3,1,3,1,3,1,3,1,3,1,3,1,3,1,3],
    [3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3],

    [3,3,3,3,3,     3,3,3,3,3],
    [3,3,3,3,3,  5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,5,5,5,5,5,  3,3,3,3,3],
    [3,3,3,3,3,  5,5,5,5,5,5,5,5,5,5,5,  3,3,3,3,3],
]

for curr in testcases:
    sol1 = solution_brute_force(curr)
    sol2 = solution_optimized(curr)

    print('%2s %2s' % (sol1, sol2), end=' ')
    print(curr)

    assert(sol1 == sol2)



queue = [[]]
while len(queue) > 0:
    curr = queue.pop(0)

    if len(curr) > 20:
        continue

    sol1 = solution_brute_force(curr)
    sol2 = solution_optimized(curr)

    print('%2s %2s %2s' % (len(curr), sol1, sol2), end=' ')
    print(curr)

    assert(sol1 == sol2)

    for i in [1, 3, 5]:
        queue.append(curr + [i])

