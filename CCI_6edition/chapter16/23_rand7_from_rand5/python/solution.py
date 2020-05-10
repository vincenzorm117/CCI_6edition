#!/usr/local/bin/python3

from random import randint

def rand5():
    return randint(0,4)


def rand7():
    while True:
        value = 5 * rand5() + rand5()
        if value < 21:
            return value % 7


x = {}
for i in range(100000):
    r = rand7()
    if r in x:
        x[r] += 1
    else:
        x[r] = 1

print(x)