


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
    for a_0 in range(len(value)-1):
        for a_1 in range(a_0, len(value)-1):
            for b_0 in range(a_1+1, len(value)):
                for b_1 in range(b_0, len(value)):
                    if pattern[0] == 'a':
                        if matchesPattern(pattern, value, (a_0, a_1), (b_0, b_1)):
                            # print('a: %s' % (value[a_0:a_1+1]))
                            # print('b: %s' % (value[b_0:b_1+1]))
                            return True
                    else:
                        if matchesPattern(pattern, value, (b_0, b_1), (a_0, a_1)):
                            # print('a: %s' % (value[b_0:b_1+1]))
                            # print('b: %s' % (value[a_0:a_1+1]))
                            return True
    return False


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
    assert(answer == solution)

