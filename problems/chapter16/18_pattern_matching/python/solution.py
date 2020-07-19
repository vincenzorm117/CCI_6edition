


def indexOfNext(pattern):
    nextLetter = 'b' if pattern[0] == 'a' else 'a'
    for index in range(1, len(pattern)):
        if pattern[index] == nextLetter:
            return index
    return None



def matchesPattern(pattern, value, charRangeA, charRangeB):
    valueIndex = 0
    for letter in pattern:
        charRange = charRangeA if letter == 'a' else charRangeB
        for charIndex in range(charRange[0], charRange[1]+1):
            if valueIndex >= len(value) or value[charIndex] != value[valueIndex]:
                return False
            valueIndex += 1
    return valueIndex == len(value)


def patternMatching(pattern, value):
    if pattern == 'ab' or pattern == 'ba' or len(pattern) < 2 or len(value) <= 0:
        return True

    aCount = pattern.count('a')
    bCount = pattern.count('b')
    patternNextLetterIndex = indexOfNext(pattern)

    if patternNextLetterIndex == None:
        letter = pattern[0]
        letterCount = aCount if letter == 'a' else bCount
        for letterSize in range(1,len(value)):
            if letterCount * letterSize == len(value):
                if letter == 'a':
                    if matchesPattern(pattern, value, (0, letterSize-1), (0,0)):
                        return True
                else:
                    if matchesPattern(pattern, value, (0,0), (0, letterSize-1)):
                        return True

    for aSize in range(1,len(value)):
        if (len(value) - aCount * aSize) % bCount != 0:
            continue
        bSize = int((len(value) - aCount * aSize) / bCount)
        if pattern[0] == 'a':
            nextLetterIndex = patternNextLetterIndex * aSize
            if matchesPattern(pattern, value, (0, aSize-1), (nextLetterIndex, nextLetterIndex + bSize - 1)):
                return True
        else:
            nextLetterIndex = patternNextLetterIndex * bSize
            if matchesPattern(pattern, value, (nextLetterIndex, nextLetterIndex + aSize - 1), (0, bSize-1)):
                return True
    return False

########################################
# Testcases

testcases = [
    ('aa', 'catcat', True),
    ('bb', 'gogo', True),
    ('aab', 'catcatgo', True),
    ('aabab', 'catcatgocatgo', True),
    ('aabbbbab', 'catcatgogogogocatgo', True),
    ('baa', 'gocatcat', True),
    ('aba', 'catgocat', True),
]


for pattern, value, answer in testcases:
    print(pattern, value)
    solution = patternMatching(pattern, value)
    # print(solution)
    assert(answer == solution)

########################################
# Positive Generated Testcases


def possibilities(bags):
    if not isinstance(bags, list) or len(bags) <= 0:
        return None
    s = [None] * len(bags)
    stack = []
    for n in bags[0]:
        stack.append((n,0))
    while 0 < len(stack):
        c = stack.pop()
        s[c[1]] = c[0]
        nxt = c[1]+1
        if len(s) <= nxt:
            yield s
        else:
            for c in bags[nxt]:
                stack.append((c,nxt))

for size in range(1, 40):
    for pattern in possibilities(['ab'] * size):
        strPattern = ''.join(pattern)
        value = strPattern.replace('a', 'cat').replace('b','go')
        print(strPattern, value)
        assert(patternMatching(strPattern, value))
