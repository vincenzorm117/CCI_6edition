#!/usr/local/bin/python3



def find_magic_index_with_dups(A):
	L = len(A)
	if L <= 0 or (L-1) < A[0] or A[L-1] < 0:
		return None
	curr = 0
	# Find first non-negative int
	if A[0] < 0:
		low, high = 0, L
		while low < high:
			curr = int((low+high)/2)
			if A[curr] < 0:
				low = int(((curr+1)+high)/2)
			else:
				high = int((low+curr)/2)
		curr = low
	else:
		curr = 0
	while curr < L:
		val = A[curr]
		if curr == val:
			return curr
		if curr < val:	
			curr = val
		else:
			curr = curr+1
	return None


def find_magic_index(A):
	L = len(A)
	if L <= 0 or (L-1) < A[0] or A[L-1] < 0:
		return None

	low, high = 0, L
	while low < high:
		curr = int((low+high)/2)
		if curr < A[curr]:
			high = curr - 1
		elif A[curr] < curr:
			low = curr + 1
		else:
			return curr
	return None



from random import randint

def gen_array():
	L = randint(5, 20)
	A = [0] * L
	A[0] = randint(-20,0)
	for i in range(1,L):
		A[i] = A[i-1] + randint(1,10)
	return A



for _ in range(100):
	A = gen_array()
	print(A)
	print(find_magic_index(A))