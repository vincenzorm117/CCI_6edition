#!/usr/local/bin/python3




def parensBookSolutionIterative(count):
    parenList = []
    stack = [(count, count, '', 0)]
    while 0 < len(stack):
        leftRem, rightRem, currStr, index = stack.pop()

        if leftRem < 0 or rightRem < 0 or leftRem > rightRem:
            continue
        elif leftRem == 0 and rightRem == 0:
            parenList.append(currStr)
        else:
            stack.append((leftRem - 1, rightRem, currStr + '(', index+1))
            stack.append((leftRem, rightRem - 1, currStr + ')', index+1))

    return (count, len(parenList), parenList)



def parensBookSolutionRecursive(count):

    def recurse(leftRem, rightRem, currStr, index):
        if leftRem < 0 or rightRem < 0 or leftRem > rightRem:
            return
        elif leftRem == 0 and rightRem == 0:
            parenList.append(''.join(currStr))
        else:
            currStr[index] = '('
            recurse(leftRem - 1, rightRem, currStr, index+1)
            currStr[index] = ')'
            recurse(leftRem, rightRem - 1, currStr, index+1)

    parenList = []
    recurse(count, count, [None]*(count*2), 0)
    return (count, len(parenList), parenList)




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



for i in range(50):
    solIter = parensBookSolutionIterative(i)
    solRecur = parensBookSolutionRecursive(i)

    print((solIter[0], solRecur[0]), (solIter[1], solRecur[1]))
    assert(parenAnswersAreEqual(solRecur, solIter))
