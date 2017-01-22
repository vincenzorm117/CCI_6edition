#!/usr/local/bin/python3


def number_swapper(a,b):
	a ^= b
	b ^= a
	a ^= b
	return (a,b)

def number_swapper_ints_only(a,b):
	a = a + b
	b = a - b
	a = a - b
	return (a,b)

print((1,2), number_swapper(1,2))
print((1,2), number_swapper_ints_only(1,2))