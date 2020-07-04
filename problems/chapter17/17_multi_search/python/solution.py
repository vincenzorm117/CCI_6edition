

def multi_search_bruteForce(b,T):
    hasWords = []
    for smallWord in T:
        for startIndex in range(len(b)):
            if b[startIndex] == smallWord[0]:
                count = 0
                for i in range(len(smallWord)):
                    if b[startIndex+i] != smallWord[i]:
                        break
                    else:
                        count += 1
                if count == len(smallWord):
                    hasWords.append(smallWord)
                    break
    return hasWords


############################################################
############################################################
# Solution helper classes

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


############################################################
############################################################
# Solution

def multi_search(b,T):
    hasWords = []

    words = Trie()
    for word in T:
        words.add(word)

    for startIndex in range(len(b)):
        if words.root.hasNext(b[startIndex]):
            currNode = words.root
            endIndex = startIndex
            while True:
                if currNode.isWord:
                    hasWords.append(b[startIndex:endIndex])
                if endIndex >= len(b) or not currNode.hasNext(b[startIndex + endIndex]):
                    break
                endIndex += 1
                currNode = currNode.next(b[startIndex + endIndex])

    return hasWords






############################################################
############################################################
# Testcase helper functions

def arrayToSet(array):
    mySet = set()
    for item in array:
        mySet.add(item)
    return mySet

def arrayMatchesSet(myArray, mySet):
    if len(myArray) != len(mySet):
        return False
    for item in myArray:
        if not item in mySet:
            return False
    return True


############################################################
############################################################
# Custom Testcases
testcases = [
    (
        'my computer rocks',
        ['foo', 'bar', 'rock', 'my'],
        ['rock', 'my']
    ),
    (
        'i love watermelon',
        ['foo1', 'love', 'foo2', 'water', 'foo3', 'melon', 'foo4', 'watermelon'],
        ['love', 'water', 'melon', 'watermelon']
    ),
    (
        'abcdefghijklmnopqrstuvwxyz',
        ['a', 'ab', 'abc', 'b', 'bc', 'c', 'hij', 'lmnoa', 'wxyz', 'xyz', 'yz', 'z', 'abcdefghijklmnopqrstuvwxyz'],
        []
    ),
    (
        'for county boundary hover show county name on hover',
        ['hover', 'or'],
        []
    ),
    (
        'for',
        ['hover', 'or'],
        []
    ),
    (
        'for',
        [],
        []
    ),
]

for b, T, answer in testcases:
    answer = arrayToSet(answer)
    solution1 = multi_search_bruteForce(b, T)
    solution2 = multi_search_bruteForce(b, T)
    print(solution1)
    print(solution2)
