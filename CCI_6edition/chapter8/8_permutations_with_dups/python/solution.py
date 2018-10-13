#!/usr/local/bin/python3



def permuteNoDups(alphabet):
    if alphabet == '':
        print('')
        return
    freq = {}
    for letter in alphabet:
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1
    def recurse(word, k, freq, size):
        if k == size:
            print(''.join(word))
            return
        for letter in freq:
            if freq[letter] <= 0:
                continue
            freq[letter] -= 1
            word.append(letter)
            recurse(word, k+1, freq, size)
            word.pop()
            freq[letter] += 1
    return recurse([], 0, freq, len(alphabet))



testcases = [
    'a',
    'ab',
    'abc',
    'aab',
    'aabc'
]

for i in range(len(testcases)):
    print('Test (%s): %s' % (i+1, testcases[i]))
    permuteNoDups(testcases[i])
