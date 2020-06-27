

# A - Answer
# G - Guess
def scorePoints(A, G, options):
    optionToIndex = {}
    for index in range(len(options)):
        optionToIndex[options[index]] = index

    optionCounts = [0] * len(options)

    hitCount, pseudoHitCount = 0, 0
    for i in range(len(options)):
        if A[i] == G[i]:
            hitCount += 1
        else:
            index = optionToIndex[A[i]]
            if optionCounts[index] < 0:
                pseudoHitCount += 1
            optionCounts[index] += 1

            index = optionToIndex[G[i]]
            if optionCounts[index] > 0:
                pseudoHitCount += 1
            optionCounts[index] -= 1

    return (hitCount, pseudoHitCount)



testcases = [
    ('RGBY', 'GGRR', 'RGBY', (1,1)),
    ('RRRR', 'GGGG', 'RGBY', (0,0)),
    ('RRRR', 'RRRR', 'RGBY', (4,0)),
    ('BYBY', 'YBYB', 'RGBY', (0,4)),
]

for machineAnswer, guess, options, answer in testcases:
    print('%s %s' % (machineAnswer, guess))
    output = scorePoints(machineAnswer, guess, options)
    print('Output: %s' % (str(output)))
    print('Answer: %s' % (str(answer)))
    print()