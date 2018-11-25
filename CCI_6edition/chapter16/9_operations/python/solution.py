#!/usr/local/bin/python3

from math import nan

def negate(x):
    if x == 0:
        return x
    elif x < 0:
        count = 0
        while x < 0:
            x += 1
            count += 1
        while 0 < count:
            x += 1
            count += -1
    else:
        count = 0
        while 0 < x:
            x += -1
            count += 1
        while 0 < count:
            x += -1
            count += -1
    return x
        



def subtract(a,b):
    return a + negate(b)


def multiply(a,b):
    mul = 0
    while 0 < a:
        mul += b
        a += -1
    return mul



def divide(a,b):
    if b == 0:
        return nan
    quotient = 0
    dividend = b
    while dividend <= a:
        dividend += b
        quotient += 1
    return quotient
