#!/usr/local/bin/python3



def steps_no_memo(n):
	if not isinstance(n, int) or n < 0:
		return 0
	if n == 0 or n == 1:
		return 1
	return steps_no_memo(n-1) + steps_no_memo(n-2) + steps_no_memo(n-3)



def steps(n):
	if not isinstance(n, int) or n < 0:
		return None
	if n == 0 or n == 1:
		return 1
	ways = [0] * n
	ways[0], ways[1], ways[2] = 1, 2, 4
	for i in range(3, n):
		ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
	return ways[n-1]



for n in range(3,30):
	sol = (steps_no_memo(n), steps(n))
	print(n, sol)
	assert(sol[0] == sol[1])