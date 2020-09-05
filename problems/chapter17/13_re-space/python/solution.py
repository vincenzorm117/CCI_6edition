from math import inf


# Helpers

class TrieNode:
    def __init__(self, isWord):
        self.map = {}
        self.isWord = isWord

    def hasNext(self, key):
        return key in self.map

    def next(self, key):
        if self.hasNext(key):
            return self.map[key]
        else:
            return None

class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def add(self, word):
        currNode = self.root
        for letter in word:
            if letter in currNode.map:
                currNode = currNode.map[letter]
            else:
                node = TrieNode(False)
                currNode.map[letter] = node
                currNode = node
        currNode.isWord = True
        return self



def solution_brute_force(sentence, wordsSet):
    minSizeValue = inf
    minSizeWords = None
    maxSizeKnownWords = 0

    stack = [(sentence, [], 0)]

    while len(stack) > 0:
        remaining, words, unknownCount = stack.pop()

        if len(remaining) <= 0:
            if minSizeValue > unknownCount and maxSizeKnownWords < (len(words) - unknownCount):
                minSizeValue = unknownCount
                minSizeWords = words[:]
                maxSizeKnownWords = len(words) - unknownCount
            continue

        for i in range(1,len(remaining)+1):
            nextWord = remaining[0:i]
            nextRemaining = remaining[i:len(remaining)]

            if nextWord in wordsSet:
                stack.append((nextRemaining, words + [nextWord], unknownCount))
            else:
                stack.append((nextRemaining, words + [nextWord], unknownCount+1))

    return minSizeValue, minSizeWords



def solution_brute_force_recursive(word, wordsSet):

    def getMinSubwords(subword):
        nonlocal wordsSet

        if len(subword) <= 0:
            return 0, []

        if len(subword) == 1:
            if subword in wordsSet:
                return 0, [subword]
            return 1, [subword]


        minSubwords = []
        minUnknownCount = inf

        for i in range(len(subword), 0, -1):
            nextSubword = subword[0:i]

            nextUnknownCount, nextSubwords = getMinSubwords(subword[i:len(subword)])

            if nextSubword in wordsSet:
                if nextUnknownCount < minUnknownCount:
                    minUnknownCount = nextUnknownCount
                    minSubwords = [nextSubword] + nextSubwords
            else:
                if nextUnknownCount+1 < minUnknownCount:
                    minUnknownCount = nextUnknownCount+1
                    minSubwords = [nextSubword] + nextSubwords

        return minUnknownCount, minSubwords

    return getMinSubwords(word)



def solution_optimized_recursive(word, wordsSet):

    memo = {}

    def getMinSubwords(subword):
        nonlocal wordsSet, memo

        if len(subword) in memo:
            return memo[len(subword)]

        if len(subword) <= 0:
            return 0, []

        if len(subword) == 1:
            if subword in wordsSet:
                return 0, [subword]
            return 1, [subword]

        minSubwords = []
        minUnknownCount = inf

        for i in range(len(subword), 0, -1):
            nextSubword = subword[0:i]

            nextUnknownCount, nextSubwords = getMinSubwords(subword[i:len(subword)])

            if nextSubword in wordsSet:
                if nextUnknownCount < minUnknownCount:
                    minUnknownCount = nextUnknownCount
                    minSubwords = [nextSubword] + nextSubwords
            else:
                if nextUnknownCount+1 < minUnknownCount:
                    minUnknownCount = nextUnknownCount+1
                    minSubwords = [nextSubword] + nextSubwords

        memo[len(subword)] = (minUnknownCount, minSubwords)
        return minUnknownCount, minSubwords

    return getMinSubwords(word)






wordsSet = set()
# lines = open('../alpha_words.txt', 'r')
lines = open('/Users/jumper/Repos/CCI_6edition/problems/chapter17/13_re-space/alpha_words.txt', 'r')
for line in lines:
    word = line[0:-1].lower()
    wordsSet.add(word)

print('running testcases')

testcases = [
    'jesslook',
    'jess',
    'bobbylookedjustfine',
    # 'jesslookedjustliketimherbrother',
]

for testcase in testcases:
    print(testcase)
    print(solution_brute_force(testcase, wordsSet))
    print(solution_optimized_recursive(testcase, wordsSet))
