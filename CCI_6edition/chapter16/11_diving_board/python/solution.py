#!/usr/local/bin/python3



def printDivingBoardLengths(shorter, longer, k):
    if shorter == longer:
        return print(shorter * k)
    if shorter == 0:
        return print(longer * k)
    if longer == 0:
        return print(shorter * k)
    for i in range(k+1):
        print(shorter*i + longer*(k - i))



for shorter in range(10):
    for longer in range(10):
        for k in range(10):
            print('============')
            print(shorter, end=' ')
            print(longer, end=' ')
            print(k)
            print('============')
            printDivingBoardLengths(shorter, longer, k)