#!/usr/local/bin/python3

def sortChars(s):
    s = list(s)
    s.sort()
    return ''.join(s)



def group_anagrams(array):
    strToSortedStr = {}
    for str in array:
        # Sort str
        sortedStr = sortChars(str)
        # Add str to hashmap grouped by anagrams
        if sortedStr not in strToSortedStr:
            strToSortedStr[sortedStr] = []
        strToSortedStr[sortedStr].append(str)
    for value in strToSortedStr.values():
        for str in value:
            print(str)
        




array = ['asdf','len','fdd','fdsa','nel','f','computer','noon','nel','ff','fdd']
group_anagrams(array)


