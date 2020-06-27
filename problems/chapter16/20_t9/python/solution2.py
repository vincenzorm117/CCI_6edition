from os import path

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



def t9ToWord(t9):
    if t9 == '2': return ['a','b','c']
    if t9 == '3': return ['d','e','f']
    if t9 == '4': return ['g','h','i']
    if t9 == '5': return ['j','k','l']
    if t9 == '6': return ['m','n','o']
    if t9 == '7': return ['p','q','r','s']
    if t9 == '8': return ['t','u','v']
    if t9 == '9': return ['p','q','r','s']
    else: return None

# Preparation
wordsFilePath = path.dirname(path.abspath(__file__))+'/../words.txt'
lines = open(wordsFilePath, 'r')
words = Trie()

for line in lines:
    word = line[0:-1] # Trim newline
    words.add(word.lower())


def getT9Words(num, wordsTrie):
    if num == '0' or num == '1':
        return None
    t9Letters = [t9ToWord(x) for x in num]
    wordLength = len(t9Letters)
    if wordLength <= 0:
        return []

    words, stack = [], [(0, wordsTrie.root, '')]

    while len(stack) > 0:
        index, trieNode, word = stack.pop()

        if index == wordLength:
            words.append(word)
            continue

        for letter in t9Letters[index]:
            if trieNode.hasNext(letter):
                stack.append((index+1, trieNode.next(letter), word+letter))
    return words




for num in range(10000):
    num = str(num)
    if '0' in num or '1' in num:
        continue
    print(num, end=': ')
    solution = getT9Words(num, words)
    if solution != None and len(solution) > 0:
        print(solution)
    else:
        print()




