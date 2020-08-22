from math import inf


def word_distance_brute_force(word1, word2, words):
    for length in range(1,len(words)):
        for startIndex in range(len(words) - length):
            endIndex = startIndex + length
            if (words[startIndex] == word1 and words[endIndex] == word2) or words[startIndex] == word2 and words[endIndex] == word1:
                return (startIndex, endIndex)



def distance(a, b):
    return abs(a - b) - 1

def getMin(word2Indeces, word1Indeces, word2Index, word1Index, minSizeValue, minSizeIndeces):
    currSizeValue = distance(word2Indeces[word2Index], word1Indeces[word1Index])
    if minSizeValue > currSizeValue:
        return (currSizeValue, (word1Indeces[word1Index], word2Indeces[word2Index]))
    return (minSizeValue, minSizeIndeces)

def word_distance_one_time(word1, word2, words):
    # Find word1 and word2 in words, and save each index in
    # word1Indeces and word2Indeces respectively.
    word1Indeces = []
    word2Indeces = []
    for i in range(len(words)):
        if words[i] == word1:
            word1Indeces.append(i)
        if words[i] == word2:
            word2Indeces.append(i)

    # Prep for loop
    word1Index = 0
    word2Index = 0
    minSizeIndeces = (word1Indeces[0], word2Indeces[0])
    minSizeValue = distance(word1Indeces[0], word2Indeces[0])
    # Loop until one of the index's has reached the end. In each iteration update
    # one of word1Index or word2Index and check the distance. Compare that distance
    # to the optimal min.
    while word1Index+1 < len(word1Indeces) and word2Index+1 < len(word2Indeces):
        # Update word1 and word2 index's s.t. the next move creates the smallest gap.
        choice1 = abs(word1Indeces[word1Index+1] - word2Indeces[word2Index])
        choice2 = abs(word1Indeces[word1Index] - word2Indeces[word2Index+1])
        if choice1 < choice2:
            word1Index += 1
        else:
            word2Index += 1
        # Compare current index's size with minSizeIndex's size
        minSizeValue, minSizeIndeces = getMin(word2Indeces, word1Indeces, word2Index, word1Index, minSizeValue, minSizeIndeces)

    # Loop through the remaining indeces of word1Indeces or word2Indeces
    if word1Index+1 < len(word1Indeces):
        while word1Index+1 < len(word1Indeces):
            word1Index += 1
            minSizeValue, minSizeIndeces = getMin(word2Indeces, word1Indeces, word2Index, word1Index, minSizeValue, minSizeIndeces)
    elif word2Index+1 < len(word2Indeces):
        while word2Index+1 < len(word2Indeces):
            word2Index += 1
            minSizeValue, minSizeIndeces = getMin(word2Indeces, word1Indeces, word2Index, word1Index, minSizeValue, minSizeIndeces)
    # Return
    return minSizeIndeces


# Alphabet of words
alphabet = ['banana','foo','bar','l1t3']
# testcases is used as a queue to generate testcases efficiently. Here are the all possibilities of size 2
testcases = [['banana', 'banana'], ['banana', 'foo'], ['banana', 'bar'], ['banana', 'l1t3'], ['foo', 'banana'], ['foo', 'foo'], ['foo', 'bar'], ['foo', 'l1t3'], ['bar', 'banana'], ['bar', 'foo'], ['bar', 'bar'], ['bar', 'l1t3'], ['l1t3', 'banana'], ['l1t3', 'foo'], ['l1t3', 'bar'], ['l1t3', 'l1t3']]

for currLength in range(50):
    while not(len(testcases[0]) == currLength+1):
        # Pop first testcase
        t = testcases.pop(0)
        # Extract all unique words
        words = list(set(t))
        # Loop through all unique word pairs
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                sol1 = word_distance_brute_force(words[i], words[j], t)
                sol2 = word_distance_one_time(words[i], words[j], t)
                d1 = distance(sol1[0], sol1[1])
                d2 = distance(sol2[0], sol2[1])
                print(d1, d2, words[i], words[j], t)
                assert(d1 == d2)
        # Append next possible values
        for word in alphabet:
            testcases.append(t + [word])
