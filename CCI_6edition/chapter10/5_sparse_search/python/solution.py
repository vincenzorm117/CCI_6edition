#!/usr/local/bin/python3


def sparseSearch(array, term):
    low, high = 0, len(array)
    count = 0
    while low < high:
        count += 1
        mid = int((low + high) / 2)
        # Find valid mid if current mid is empty
        if array[mid] == '':
            bottom, top = mid-1, mid+1
            while 0 < bottom and top < len(array)-1:
                count += 1
                bottom -= 1
                if array[bottom] != '':
                    mid = bottom
                    break
                top += 1
                if array[top] != '':
                    mid = top
                    break
        if array[mid] == term:
            print('Stats: %s' % count)
            return mid
        if term < array[mid]:
            high = mid
        else:
            low = mid+1
    print('Stats: %s' % count)
    return None




testcases = [
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'at', 0),
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'ball', 4),
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'car', 7),
    (['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'dad', 10),

    (['for', 'geeks', '', '', '', '', 'ide', 'practice', '', '', '', 'quiz'], 'for', 0),
    (['for', 'geeks', '', '', '', '', 'ide', 'practice', '', '', '', 'quiz'], 'geeks', 1),
    (['for', 'geeks', '', '', '', '', 'ide', 'practice', '', '', '', 'quiz'], 'ide', 6),
    (['for', 'geeks', '', '', '', '', 'ide', 'practice', '', '', '', 'quiz'], 'practice', 7),
    (['for', 'geeks', '', '', '', '', 'ide', 'practice', '', '', '', 'quiz'], 'quiz', 11),
]



for i in range(len(testcases)):
    array, term, solution = testcases[i]
    print('Case #%s: %s' % (i, term))
    answer = sparseSearch(array, term)
    print('Answer: %s' % answer, end="\n\n")
    assert(answer == solution)