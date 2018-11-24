#!/usr/local/bin/python3

import re


# def wordFrequencies(word, freq):
#     return freq[word] if word in freq else 0



book = open('./book.txt', 'r')

freq = {}

for line in book:
    for word in line.split():
        # Remove punctuation marks
        word = re.sub(r'[^0-9a-z]', '', word.lower())
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1


def wordFrequencies(word, freq):
    return freq[word] if word in freq else 0


testcases = ['not','the']

for word in testcases:
    print(word, wordFrequencies(word, freq))
    