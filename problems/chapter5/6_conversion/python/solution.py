#!/usr/local/bin/python3


def hamming_distance_slow(N):
	if not isinstance(N, int):
		return 0
	count = 0
	while 0 < N:
		if (1 & N) == 1:
			count += 1
		N = N >> 1
	return count

def hamming_distance(N):
	if not isinstance(N, int):
		return 0
	count = 0
	while 0 < N:
		count += 1
		N = N & (N - 1)
	return count

def conversion(A,B):
	if not isinstance(A, int) or not isinstance(B, int):
		return None
	if A == B: 
		return 0
	return hamming_distance(A^B)

tests = [
	(3,4,3),
	(1,1,0),
	(2,2,0),
	(5,3,2),
	(15,7,1)
]

for test in tests:
	c = conversion(test[0],test[1])
	print(test, 'RESULT:', c)
	assert c == test[2]



