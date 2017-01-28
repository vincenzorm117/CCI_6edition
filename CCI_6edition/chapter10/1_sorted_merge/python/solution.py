#!/usr/local/bin/python3


def sorted_merge(A,B):
	if not isinstance(A, list) or not isinstance(B, list):
		return None
	if len(A) == 0 and len(B) == 0:
		return []
	placer = len(A) - 1

	curr = [len(A) - len(B) - 1, len(B) - 1]
	while 0 <= placer:
		isDone = (curr[0] < 0, curr[1] < 0)
		if isDone[0] and isDone[1]:
			return None
		elif isDone[0] and not isDone[1]:
			arrayType = 1
		elif not isDone[0] and isDone[1]:
			arrayType = 0
		else:
			arrayType = 1 if A[curr[0]] < B[curr[1]] else 0
		if arrayType == 1:
			A[placer] = B[curr[arrayType]]
		else:
			A[placer] = A[curr[arrayType]]
		curr[arrayType] -= 1
		placer -= 1
	return A


testcases = [
	([], [], []),
	([], 4, None),
	([2,4,7,8,9, None, None, None, None], [1,3,5,6], [1,2,3,4,5,6,7,8,9]),
	([2,4,7,8,9], [], [2,4,7,8,9]),
	([1,2,3, None, None, None], [4,5,6], [1,2,3,4,5,6]),
]

for t in testcases:
	solution = sorted_merge(t[0], t[1])
	print(solution)
	assert(solution == t[2])


from random import randint

def TestCase(M=10):
	L = randint(0, M)
	pivot = randint(0, L)
	A = [0] * pivot
	B = [0] * (L - pivot)
	for i in range(0, pivot):
		A[i] = randint(0, 30)
	A.sort()
	A = A + [None] * (L - pivot)
	for i in range(0, len(B)):
		B[i] = randint(0, 30)
	B.sort()
	return (A,B)

for i in range(1000000):
	t = TestCase()
	# print("Test: #"+str(i+1))
	# print(t[0])
	# print(t[1])
	solution = sorted_merge(t[0], t[1])
	# print(solution)
	for i in range(len(solution) - 1):
		assert(solution[i] <= solution[i+1])
	# print()


