#!/usr/local/bin/python3


# Book solution
def flip(a):
    return 1 ^ a

def sign(a):
    # return ((a >> 31) & 1) # Use 31, assuming its a 32 bit system
    return 1 if a > 0 else 0

def getMaxNaive(a, b):
    k = sign(a - b) # <-- This is the problem with this solution. This can cause integer overflow in certain languages.
    q = flip(k)
    return (a * k) + (b * q)


def getMaxFinal(a, b):
    sa = sign(a)
    sb = sign(b)

    differentSigns = sa ^ sb
    sameSigns = flip(differentSigns)

    k = differentSigns * sa + sameSigns * sign(a - b)

    q = flip(k)

    return (a * k) + (b * q)


# My solution
#   The issue with this solution is that in other languages there can be an integer overflow from a + b + (a-b)
#   Dividing by two is not an issue as a + b + |a-b| is always either 2a or 2b depending on which is bigger.
def vAbs(x):
    # return x & ~(1 << 32) <-- this is the conventional way but in python this is not possible
    return -x if x < 0 else x

def vMax(a,b):
    return ((a+b) + vAbs(a-b)) / 2



for i in range(-1000,1000):
    for j in range(-1000,1000):
        assert(max(i,j) == getMaxFinal(i,j))