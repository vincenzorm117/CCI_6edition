from math import inf


def isRangeEqualLettersNumsCount(array, start, end):
    letterCount, numberCount = 0,0
    for i in range(start, end+1):
        if array[i].isalpha():
            letterCount += 1
        else:
            numberCount += 1
    return letterCount == numberCount


def letters_and_numbers_bruteForce(array):
    for length in range(len(array), -1, -1):
        for j in range(0, len(array) - length + 1):
            if isRangeEqualLettersNumsCount(array, j, j + length - 1):
                return (j, j + length - 1)
    return None


def letters_and_numbers(array):
    plot = [(0,0)]
    letterCount = 0
    numberCount = 0

    # Generate plot array
    for item in array:
        if item.isalpha():
            letterCount += 1
        else:
            numberCount += 1
        plot.append((letterCount, numberCount))

    # Check for empty array, only letters or only numbers
    if letterCount <= 0 or numberCount <= 0:
        return None
    # Check if entire array is
    if letterCount == numberCount:
        return (0, len(array)-1)

    subarrays = {}
    maxSubArrayStart = -1
    maxSubArrayEnd = -1

    for i in range(len(plot)):
        letterCount, numberCount = plot[i]
        diffToStore = numberCount - letterCount

        if diffToStore not in subarrays:
            subarrays[diffToStore] = i
            continue

        startIndex = subarrays[diffToStore]
        endIndex = i
        if maxSubArrayEnd - maxSubArrayStart < endIndex - startIndex:
            maxSubArrayStart = startIndex
            maxSubArrayEnd = endIndex

    return (maxSubArrayStart+1, maxSubArrayEnd)




def distance(pair):
    if pair == None:
        return 0
    if pair[0] < 0 or pair[1] < 0:
        return 0
    return pair[1] - pair[0] + 1



# testcases = [
#     'aaaa1a1a1a1a1aaaaaaaaaaaaaa1a11aaaaaaaaaa11aaaaa',
#     'aa1a1a1a1a1aaaa1a11aaaaa11',
#     'aaaaaa111111',
#     'a1a1a1a1a1a1a1a1a11'
# ]



# for testcase in testcases:
#     sol1 = letters_and_numbers_bruteForce(testcase)
#     sol2 = letters_and_numbers(testcase)
#     print(sol1, sol2, distance(sol1), distance(sol2), len(testcase), testcase)
#     assert(distance(sol1) == distance(sol2))



testcases = [[]]


# Alphabet of words
alphabet = 'a1'
# testcases is used as a queue to generate testcases efficiently. Here are the all possibilities of size 2
testcases = ['']

for currLength in range(50):
    while not(len(testcases[0]) == currLength+1):
        # Pop first testcase
        t = testcases.pop(0)
        # Test case
        sol1 = letters_and_numbers_bruteForce(t)
        sol2 = letters_and_numbers(t)
        print(currLength, sol1, sol2, len(t), t)
        assert(distance(sol1) == distance(sol2))
        # Append next possible values
        for word in alphabet:
            testcases.append(t + word)




# for totalCount in range(10):
#     for letterCount in range(totalCount+1):
#         numberCount = totalCount - letterCount
#         testcase = 'a'*letterCount + '1'*numberCount
#         print(testcase)

#         testcasePermutations = permute_no_dups(list(testcase))
#         for testcasePermutation in testcasePermutations:
#             print(letters_and_numbers_bruteForce(testcasePermutation)[0], testcasePermutation)
#             letters_and_numbers(testcasePermutation)
#             print()
