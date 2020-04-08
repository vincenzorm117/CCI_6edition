#!/usr/local/bin/python3

import math


def negate_slow(x):
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



def divide_slow(a,b):
    if b == 0:
        return inf
    quotient = 0
    dividend = b
    while dividend <= a:
        dividend = add(dividend, b)
        quotient += 1
    return quotient

def multiply_slow(a,b):
    mul = 0
    while 0 < a:
        mul = add(mul, b)
        a += -1
    return mul


############################################################
############################################################
############################################################
# Helper functions


def add(a,b):
    return a + b

def sign(a):
    return 1 if 0 < a else -1

def abs(a):
    return negate(a) if a < 0 else a


############################################################
############################################################
############################################################
# Main functions


def negate(x):
    if x == 0:
        return 0

    c_start = 1 if 0 > x else -1
    negativeX = 0

    if x + negativeX < 0:
        while x + negativeX != 0:
            c = c_start
            while  x + negativeX + (c+c) < 0:
                c = add(c,c)
            negativeX = add(c, negativeX)
    else:
       while x + negativeX != 0:
            c = c_start
            while  x + negativeX + (c+c) > 0:
                c = add(c,c)
            negativeX = add(c, negativeX)

    return negativeX





def subtract(a,b):
    return add(a, negate(b))




def multiply(a,b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a

    argumentsHaveSameSign = sign(a) == sign(b)
    a, b = abs(a), abs(b)

    factor = 0
    product = 0

    while True:
        subFactor = 0
        subProduct = 0


        while True:

            if a < factor + add(subFactor, subFactor):
                break

            subProduct = b if subProduct == 0 else add(subProduct, subProduct)
            subFactor = 1 if subFactor == 0 else add(subFactor, subFactor)

        product = add(product, subProduct)
        factor = add(factor, subFactor)

        if a < factor + 1:
            break

    return product if argumentsHaveSameSign else negate(product)





def divide(a,b):
    if b == 0:
        return math.nan

    argumentsHaveSameSign = sign(a) == sign(b)
    a, b = abs(a), abs(b)

    if a < b:
        return 0

    quotient = 0
    multipleOfB = 0

    while True:
        subMultipleOfB = 0
        subQuotient = 0

        while True:
            if a < multipleOfB + add(subMultipleOfB, subMultipleOfB):
                break

            subMultipleOfB = b if subMultipleOfB == 0 else add(subMultipleOfB, subMultipleOfB)
            subQuotient = 1 if subQuotient == 0 else add(subQuotient, subQuotient)

        multipleOfB = add(multipleOfB, subMultipleOfB)
        quotient = add(quotient, subQuotient)


        if a < multipleOfB + b:
            break

    return quotient if argumentsHaveSameSign else negate(quotient)






for a in range(-100,100):
    for b in range(-100,100):
        assert(a - b == subtract(a, b))
        assert(a * b == multiply(a, b))

        if b == 0:
            assert(math.isnan(divide(a, b)))
        else:
            assert(int(a / b) == divide(a, b))