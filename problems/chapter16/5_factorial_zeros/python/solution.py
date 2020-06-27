#!/usr/local/bin/python3

def log(b,x):
	c = 0
	while b <= x:
		x /= b
		c += 1
	return c


def factorial_zeros(x):
	if x < 0:
		return -1
	count, i = 0, 5
	while 0 < (x/i):
		count += int(x / i)
		i *= 5
	return count

def countZeros(x):
	s = str(x)
	count = 0
	for c in range(len(s)-1,0, -1):
		if s[c] != '0':
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