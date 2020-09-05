


def GenerateMap(length):
    allWords = open('../wordsUpperCase.txt', 'r')
    wordMap = {}
    wordSet = set()
    # Traverse all words in dictionary
    for line in allWords:
         # Trim newline
        word = line[0:-1]
        # Skip words that don't match length
        if len(word) != length:
            continue
        # Add word to wordSet
        wordSet.add(word)
        # Add word map mappings
        for index in range(length):
            underScoredWord = word[0:index] + '_' + word[index+1:len(word)]
            if underScoredWord not in wordMap:
                wordMap[underScoredWord] = [word]
            else:
                wordMap[underScoredWord].append(word)
    allWords.close()
    return (wordMap, wordSet)




def solution(start, end, wordMap, wordSet):
    if len(start) != len(end):
        return None
    if start == end:
        return [start]

    L = len(start)
    path = [start]
    checkedWords = set()
    checkedWords.add(start)

    if start not in wordSet or end not in wordSet:
        return None

    def recurse(word):
        nonlocal wordMap, wordSet, path, checkedWords, end
        # print(path)
        if word == end:
            return path

        for index in range(L):
            nextWord = word[0:index] + end[index] + word[index+1:len(word)]
            # Check if word is valid or already visited
            if nextWord not in wordSet or nextWord in checkedWords:
                continue
            # Mark word as visisted
            checkedWords.add(nextWord)
            # Add word as part of path
            path.append(nextWord)
            # Traverse word
            if recurse(nextWord) == None:
                path.pop()
            else:
                return path

        for index in range(L):
            underScoredWord = word[0:index] + '_' + word[index+1:len(word)]
            if underScoredWord not in wordMap:
                continue
            #  Get neighboring words
            words = wordMap[underScoredWord]
            # Loop through all neighboring words
            for nextWord in words:
                # Check if word already visited
                if nextWord in checkedWords:
                    continue
                # Mark word as visisted
                checkedWords.add(nextWord)
                # Add word as part of path
                path.append(nextWord)
                # Traverse word
                if recurse(nextWord) == None:
                    path.pop()
                else:
                    return path
        return None
    return recurse(start)



testcases = [
    ('DAMP','DAMP'),
    ('DAMP','LAMP'),
    ('DAMP','LIMP'),
    ('DAMP','LIKE'),
    ('TRI','FOO'),
    ('AANI','ANNO'),
    ('FIGHTS','JUNGLE'),
]

wordSizeToMap = {}

for start,end in testcases:
    # Get wordMap and wordSet for word size
    if len(start) not in wordSizeToMap:
        wordSizeToMap[len(start)] = GenerateMap(len(start))
    wordMap, wordSet = wordSizeToMap[len(start)]

    print(solution(start, end, wordMap, wordSet))
