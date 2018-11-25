#!/usr/local/bin/python3

def vAbs(x):
    # return x & ~(1 << 32) <-- this is the conventional way but in python this is not possible
    return -x if x < 0 else x

def vMax(a,b):
    return (a+b) - vAbs(a-b)