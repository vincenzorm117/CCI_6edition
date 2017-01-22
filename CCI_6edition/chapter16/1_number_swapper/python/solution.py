#!/usr/local/bin/python3


def number_swapper(a,b):
	a ^= b
	b ^= a
	a ^= b
	return (a,b)



print((1,2), number_swapper(1,2))