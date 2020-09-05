#!/usr/local/bin/python3

from math import floor

def log(b,x):
	c = 0
	while b <= x:
		x /= b
		c += 1
	return c

def factorial_zeros3(N):
    # if N is not int:
    #     return None
    if N < 0:
        return 0
    return floor(N/5)


def factorial_zeros2(N):
    if N < 0:
        return None
    sum = 0
    for i in range(1,N+1):
        sum += log(5,i)
    return sum

def factorial_zeros(N):
	if N < 0:
		return -1
	count, i = 0, 5
	while 0 < (N/i):
		count += int(N / i)
		i *= 5
	return count

def countZeros(num):
	numAsString = str(num)
	count = 0
	for i in range(len(numAsString)-1, -1, -1):
		if numAsString[i] != '0':
			break
		count += 1
	return count


N = 1
for i in range(1,10000):
	N *= i
	print(i, end=" ")
	sol = (factorial_zeros(i), countZeros(N))
	print(sol, end=" ")
	assert(sol[0] == sol[1])
	print("PASSED")