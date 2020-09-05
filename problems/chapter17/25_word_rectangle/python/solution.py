

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


def GenerateDictWordLengthToTrie(words):
    words.seek(0)
    wordLengthToTrie = {}

    for wordWithNewLine in words:
        word = wordWithNewLine[0:-1]
        if len(word) not in wordLengthToTrie:
            wordLengthToTrie[len(word)] = Trie()
        wordLengthToTrie[len(word)].add(word)

    return wordLengthToTrie

def GenerateDictWordLengthToArray(words):
    words.seek(0)
    wordsArray = {}

    for wordWithNewLine in words:
        word = wordWithNewLine[0:-1]
        if len(word) not in wordsArray:
            wordsArray[len(word)] = [word]
        else:
            wordsArray[len(word)].append(word)

    return wordsArray

def GenerateDictWordLengthToSet(words):
    words.seek(0)
    wordsArray = {}

    for wordWithNewLine in words:
        word = wordWithNewLine[0:-1]
        if len(word) not in wordsArray:
            wordsArray[len(word)] = [word]
        else:
            wordsArray[len(word)].append(word)

    return wordsArray


def printWordsRectangle(words):
    for word in words:
        print(word)
    print()



def getRectangleFromIndeces(recIndeces, N, M, wordLengthToArray, wordLengthToSet):
    wordsM = wordLengthToArray[M]
    # Get N words of length M
    words = []
    for index in recIndeces:
        words.append(wordsM[index])
    # Get words set
    wordsSet = wordLengthToSet[M]
    # Check horizontal words to see if they are valid
    for i in range(M):
        wordToCheck = ''
        for word in words:
            wordToCheck += word[i]
        if wordToCheck not in wordsSet:
            return None
    # If this point is reached the rectangle is valid and we can return
    return words




def solution_brute_force(wordLengthToArray, wordLengthToSet):
    lengths = list(wordLengthToTrie.keys())
    lengths.sort(reverse=True)

    for i in range(len(lengths)):
        N = lengths[i]
        for j in range(i, len(lengths)):
            M = lengths[j]

            wordsM = wordLengthToArray[M]
            wordsN = wordLengthToArray[N]

            print((N, len(wordsN)), (M, len(wordsM)))

            stack = [[]]

            while len(stack) > 0:
                curr = stack.pop()

                if len(curr) == N:
                    wordsRectangle = getRectangleFromIndeces(curr, N, M, wordLengthToArray, wordLengthToSet)
                    if wordsRectangle != None:
                        return wordsRectangle
                    continue

                for m in range(len(wordsM)):
                    stack.append(curr + [m])
    return []





def solution_optimized(wordLengthToArray, wordLengthToSet, wordLengthToTrie):
    # Get unique list of word sizes and sort it with the largest words in the beginning
    lengths = list(wordLengthToTrie.keys())
    lengths.sort(reverse=True)

    # Loop through all rectangles NxM such that M <= N
    for i in range(len(lengths)):
        N = lengths[i]
        for j in range(i, len(lengths)):
            M = lengths[j]

            # wordsM: Get array of words of size M
            wordsM = wordLengthToArray[M]
            # wordsN: Get array of words of size N
            wordsN = wordLengthToArray[N]
            # trieM: Get trie of words of size M
            trieM = wordLengthToTrie[M]
            # trieN: Get trie of words of size N
            trieN = wordLengthToTrie[N]

            # Print the current dimensions and the search spaces
            print((N, len(wordsN)), (M, len(wordsM)))

            # (a1, a2)
            #  a1 is an array of indeces to form rectangle. The indeces map to the words in wordLengthToArray[N]
            #  a2 is an array of size M containing tries to check the next word
            stack = [([], [trieN.root for _ in range(M)])]

            # Similar to recursion. Loop until rectangle is found or if whole solution space
            #  has been searched.
            while len(stack) > 0:
                # Pop current indeces and tries to try
                indeces, tries = stack.pop()

                # If there N indeces that means we have rectangle
                if len(indeces) == N:
                    # Build rectangle from indeces
                    return getRectangleFromIndeces(indeces, N, M, wordLengthToArray, wordLengthToSet)

                # Loop through next possible words
                for m in range(len(wordsM)):
                    # Retrieve current word
                    wordM = wordsM[m]
                    # Build next tries to try and skip the ones that don't lead to a path
                    #  with a valid word
                    nextTries = []
                    wordConstructionIsValid = True
                    for k in range(M):
                        # Get the kth letter of the next word to try
                        letter = wordM[k]
                        # Check if the kth trie has that next letter
                        if not tries[k].hasNext(letter):
                            # Quit if trie does not have the letter
                            wordConstructionIsValid = False
                            break
                        else:
                            # Move trie forward if letter exists
                            nextTries.append(tries[k].next(letter))
                    # If word is valid add it to the stack
                    if wordConstructionIsValid:
                        # Clone indeces
                        nextIndeces = indeces + [m]
                        # Add next indeces and tries to stack
                        stack.append((nextIndeces, nextTries))
    # If this point is reached, return nothing
    return []




# words = open('wordsUpperCase.txt')
fileOfWords = open('/Users/jumper/Repos/CCI_6edition/problems/chapter17/25_word_rectangle/wordsUpperCase.txt')

wordLengthToTrie = GenerateDictWordLengthToTrie(fileOfWords)
wordLengthToArray = GenerateDictWordLengthToArray(fileOfWords)
wordLengthToSet = GenerateDictWordLengthToSet(fileOfWords)

print('wordLengthToTrie created')

sol2 = solution_optimized(wordLengthToArray, wordLengthToSet, wordLengthToTrie)
printWordsRectangle(sol2)

# sol2 = solution_brute_force(wordLengthToArray, wordLengthToSet)
# printWordsRectangle(sol2)
