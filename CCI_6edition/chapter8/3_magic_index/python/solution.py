#!/usr/local/bin/python3


def brute_force(A):
	for i in range(len(A)):
		if A[i] == i:
			return i
	return None


# def find_magic_index_with_dups(A):
# 	L = len(A)
# 	if L <= 0 or (L-1) < A[0] or A[L-1] < 0:
# 		return None
# 	curr = 0
# 	# Find first non-negative value
# 	if A[0] < 0:
# 		low, high = 0, L
# 		while low < high:
# 			curr = int((low+high)/2)
# 			if A[curr] < 0:
# 				low = int(((curr+1)+high)/2)
# 			else:
# 				high = int((low+curr)/2)
# 		curr = low
# 	else:
# 		curr = 0
# 	while curr < L:
# 		val = A[curr]
# 		if curr == val:
# 			return curr
# 		if curr < val:	
# 			curr = val
# 		else:
# 			curr = curr+1
# 	return None

def find_magic_index_with_dups(A):
	if A is None or len(A) == 0:
		return None
	L = len(A)
	q = [(0, L-1)]
	while 0 < len(q):
		c = q.pop()
		curr = int((c[0]+c[1])/2)
		if A[curr] == curr:
			return curr
		left = min(curr - 1, A[curr])
		right = max(curr + 1, A[curr])
		if 0 <= left and c[0] <= left:
			q.append( (c[0], left) )
		if right < L and right <= c[1]:
			q.append( (right, c[1]) )
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
	A[0] = randint(1,10)
	for i in range(1,L):
		A[i] = A[i-1] + randint(0,3)
	return A





testcases = [
	([1,3,3,4,5,5], 5),
	([0], 0),
	([1], None),
	([], None),
	([1,2,3,4,5], None)
]

for t in testcases:
	A = t[0]
	print(A)
	sol = find_magic_index_with_dups(A)
	assert(sol == t[1])




# for _ in range(100):
# 	A = gen_array()
# 	sol = find_magic_index_with_dups(A)
# 	if sol is not None:
# 		print(A)
# 		print(sol)

