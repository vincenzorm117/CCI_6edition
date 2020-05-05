#!/usr/local/bin/python3


flatten = lambda l: [item for sublist in l for item in sublist]



class ParensIteratorWithSet:

    def __init__(self):
        self.currN = -1
        self.currParens = ['']

    def hasNext(self):
        return True

    # @return (parenCount, answerCount, count)
    def next(self):
        self.currN += 1

        if self.currN < 1:
            return (self.currN, 0, [])

        newParens = set()
        for paren in self.currParens:
            newParens.add('(%s)' % (paren))
            newParens.add('()%s' % (paren))
            newParens.add('%s()' % (paren))

        self.currParens = list(newParens)
        return (self.currN, len(self.currParens), self.currParens)




class ParensIteratorWithFib:

    def __init__(self):
        self.currN = -1

        self.currParens = [
            ['((()))', '(()())'],
            ['()(())', '()()()'],
            ['(())()']
        ]

    def hasNext(self):
        return True

    # @return (parenCount, answerCount, count)
    def next(self):
        self.currN += 1

        if self.currN < 3:
            starts = [[], ['()'], ['(())', '()()']]
            return (self.currN, len(starts[self.currN]), starts[self.currN])


        if self.currN == 3:
            parens = flatten(self.currParens)
            return (self.currN, len(parens), parens)

        allLastParens = flatten(self.currParens)
        newCurrParens = [[],[],[]]
        # Outer
        for paren in allLastParens:
            newCurrParens[0].append('(%s)' % (paren))
        # Left
        for paren in allLastParens:
            newCurrParens[1].append('()%s' % (paren))
        # Right
        for paren in (self.currParens[0] + self.currParens[2]):
            newCurrParens[2].append('%s()' % (paren))

        self.currParens = newCurrParens

        parens = flatten(self.currParens)
        return (self.currN, len(parens), parens)


def parenAnswersAreEqual(solFib, solSet):
    solFibN, solFibLen, solFibArray = solFib
    solSetN, solSetLen, solSetArray = solSet

    if solFibN != solSetN or solFibLen != solSetLen:
        return False

    solSetArraySet = set(solSetArray)
    for paren in solFibArray:
        if not(paren in solSetArraySet):
            return False
        solSetArraySet.remove(paren)

    return len(solSetArraySet) == 0


iteratorWithSet = ParensIteratorWithSet()
iteratorWithFib = ParensIteratorWithFib()


for i in range(50):
    solFib = iteratorWithFib.next()
    solSet = iteratorWithSet.next()
    print(solFib[1], solSet[1])
    assert(parenAnswersAreEqual(solFib, solSet))
