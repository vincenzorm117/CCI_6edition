
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



def GenerateWordsTrie(words):
    wordsTrie = Trie()
    for word in words:
        wordsTrie.add(word)
    return wordsTrie




def is_longest_word_brute_force_iterative(word, wordsSet):

    stack = [[word]]

    while len(stack) > 0:
        subwords = stack.pop()

        # Return if all words in subwords are existing words
        if len(subwords) > 1 and wordsSet.issuperset(subwords):
            return subwords

        # Breakup
        for index in range(len(subwords)):
            subword = subwords[index]

            for i in range(1,len(subword)):
                array = subwords[0:index]

                array.append(subword[0:i])
                array.append(subword[i:len(subword)])

                array.extend(subwords[index+1:len(subwords)])
                stack.append(array)



def is_longest_word_brute_force_recursive(word, wordsSet):

    def getSubWords(subwords, subword):
        nonlocal wordsSet
        # Return if the end is reached
        if len(subword) <= 0 and len(subwords) > 1:
            return subwords
        # Check all possible spots to break the current subword
        for i in range(len(subword)+1):
            # Create prefix substring of subword
            newWord = subword[0:i]
            # Skip this loop if it's not one of the existing words
            if newWord not in wordsSet:
                continue
            # If it is a matching word add it to the subwords, and
            #  check the rest of the subwords that can be found after it.
            subwords.append(newWord)
            nextSubwords = getSubWords(subwords, subword[i:len(subword)])
            if nextSubwords != None:
                return nextSubwords
            # If runtime reaches this point, the subword and next subwords don't
            #  match any of the current words so we skip it
            subwords.pop()
        # If nothing is found return None
        return None

    return getSubWords([], word)




def is_longest_word_optimized(word, wordsTrie):
    # Simulate recursion with stack
    stack = [(0, [])]
    # Run until a match is found or there are no more subwords to try
    while len(stack) > 0:
        i, subwords = stack.pop()

        # Check if word can't be split anymore and check if it has
        #  more than one subword. If both are true a match is found.
        if i >= len(word) and len(subwords) > 1:
            return subwords

        # Setup Trie node iterator
        currNode = wordsTrie.root

        # Loop from i to the end of the word
        for j in range(i, len(word)):
            # Check if the next letter is in the trie iterator. If
            #  it isn't break the loop otherwise move the iterator.
            if not currNode.hasNext(word[j]):
                break
            currNode = currNode.next(word[j])
            # Check if the current node is a word. If so, then we've
            #  found a subword. We mark the spot by adding the find
            #  to the stack and continuouing.
            if currNode.isWord:
                stack.append((j+1, subwords + [word[i:j+1]]))
    # If nothing is found return None.
    return None




def longest_word_brute_force(words):
    words = sorted(words, key=lambda x : len(x), reverse=True)
    wordsSet = set(words)

    for word in words:
        subwords = is_longest_word_brute_force_recursive(word, wordsSet)
        if subwords != None:
            return (word, subwords)
    return None



def longest_word_optimized(words):
    words = sorted(words, key=lambda x : len(x), reverse=True)
    wordsTrie = GenerateWordsTrie(words)

    for word in words:
        subwords = is_longest_word_optimized(word, wordsTrie)
        if subwords != None:
            return (word, subwords)
    return None




testcases = [
    ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker'],
    ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'ba', 'na'],
    ['banananananananana', 'babanananananana', 'na', 'ba'],
    ['mubanananananananana', 'babanananananana', 'na', 'ba'],
    ['akfljasjdfkjasdjflkjsdkfjklsdjfjsouvmnmxcviuiuwehrmnxizioympouwierjk', 'babanananananana', 'computer', 'foobar'],
    ['computer', 'walrus', 'fatman', 'freeman', 'man', 'gumbo', 'pizza', 'fruitlover', 'lover', 'gum', 'fat'],
    ['EDGREW','EDGY','EDH','EDIBILITY','EDIBLE','EDIBLENESS','EDICT','EDICTAL','EDICTALLY','EDICULE','EDIFICABLE','EDIFICATION','EDIFICATOR','EDIFICATORY','EDIFICE','EDIFICIAL','EDIFIER','EDIFY','EDIFYING','EDIFYINGLY','EDIFYINGNESS','EDINGTONITE','EDIT','EDITAL','EDITH','EDITION','EDITOR','EDITORIAL','EDITORIALIZE','EDITORIALLY','EDITORSHIP','EDITRESS','EDIYA','EDMOND','EDMUND','EDNA','EDO','EDOMITE','EDOMITISH','EDONI','EDRIASTEROIDEA','EDRIOASTEROID','EDRIOASTEROIDEA','EDRIOPHTHALMA','EDRIOPHTHALMATOUS','EDRIOPHTHALMIAN','EDRIOPHTHALMIC','EDRIOPHTHALMOUS','EDUARDO','EDUCABILIA','EDUCABILIAN','EDUCABILITY','EDUCABLE','EDUCAND','EDUCATABLE','EDUCATE','EDUCATED','EDUCATEE','EDUCATION','EDUCATIONABLE','EDUCATIONAL','EDUCATIONALISM','EDUCATIONALIST','EDUCATIONALLY','EDUCATIONARY','EDUCATIONIST','EDUCATIVE','EDUCATOR','EDUCATORY','EDUCATRESS','EDUCE','EDUCEMENT','EDUCIBLE','EDUCIVE','EDUCT','EDUCTION','EDUCTIVE','EDUCTOR','EDULCORATE','EDULCORATION','EDULCORATIVE','EDULCORATOR','EDUSKUNTA','EDWARD','EDWARDEAN','EDWARDEANISM','EDWARDIAN','EDWARDINE','EDWARDSIA','EDWARDSIIDAE','EDWIN','EDWINA','EEGRASS','EEL', 'E', 'DUCT'],
]


for words in testcases:
    print('======== Testcase')
    print(words)
    print(longest_word_brute_force(words))
    print(longest_word_optimized(words))
