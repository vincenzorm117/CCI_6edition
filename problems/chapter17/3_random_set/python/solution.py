
from random import randint


def randomSetWithRePicking(array, m):
    newArray = []
    for i in range(m):
        newArray.append(array[randint(0,m-1)])
    return newArray

def shuffleSubArray(array, start, end):
    for i in range(start, end+1):
        j = randint(i, end)
        array[i], array[j] = array[j], array[i]
    return array

def shuffle(array):
    for i in range(0, len(array)):
        j = randint(i, len(array)-1)
        array[i], array[j] = array[j], array[i]
    return array


def randomSetWithoutDups(array, M):
    if len(array) == 0:
        return []
    currM = M
    newArray = []
    while True:
        if currM <= len(array):
            for i in range(currM):
                j = randint(i, currM-1)
                array[i], array[j] = array[j], array[i]
                newArray.append(array[i])
            return newArray
        else:
            newArray += shuffle(array)
            currM -= len(array)
    return newArray


for M in range(10):
    for L in range(1, 10):
        print('\nM=%s L=%s' % (M,L))
        for loop in range(100):
            array = [randint(-50,50) for r in range(L)]
            newArray = randomSetWithoutDups(array, M)
            print(newArray)
            assert(len(newArray) == M)




def randomSubSet(array, M):
    if M > len(array):
        raise Exception('M must be less than the length of array')

    subArray = []
    for i in range(M):
        j = randint(i, M)
        array[i], array[j] = array[j], array[i]
        subArray.append(array[i])
    return subArray
