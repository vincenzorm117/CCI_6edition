#!/usr/local/bin/python3


def sorted_matrix_search(matrix, M, N, el):
	if not isinstance(matrix, list):
		return None
	if len(matrix) <= 0 or len(matrix[0]) <= 0:
		return None
	row = [0, M-1]
	while row[0] < row[1]:
		mid = int((row[0] + row[1])/2) + 1
		if matrix[mid][0] <= el:
			row[0] = mid
		else:
			row[1] = mid-1
	row = row[0]
	col = [0, N-1]
	while col[0] < col[1]:
		mid = int((col[0] + col[1])/2) + 1
		if matrix[row][mid] <= el:
			col[0] = mid
		else:
			col[1] = mid-1
	col = col[0]
	return (row, col)


from random import randint

def genMatrix(M=None, N=None):
	if M is None:
		M = randint(4,10)
	if N is None:
		N = randint(4,10)
	L = M * N
	m = [0] * L
	for i in range(L):
		m[i] = randint(0,200)
	m.sort()
	matrix = []
	for i in range(M):
		matrix.append([])
		for j in range(N):
			matrix[i].append(m[N*i+ j])
	return (matrix, M, N)

def printMatrix(matrix, M, N):
	for x in range(M):
		for y in range(N):
			print("%3d" % matrix[x][y], end=" ")
		print()
	print()


for w in range(1,10):
	for h in range(1,10):
		m = genMatrix(w,h)
		for i in range(m[1]):
			for ii in range(m[2]):
				print("%d x %d (%d)" % (m[1], m[2], m[0][i][ii]))
				printMatrix(m[0], m[1], m[2])
				solution = sorted_matrix_search(m[0], m[1], m[2], m[0][i][ii])
				print(m[0][i][ii], m[0][solution[0]][solution[1]], solution)
				assert(m[0][i][ii] == m[0][solution[0]][solution[1]])

# for t in range(10000):
# 	m = genMatrix(4,4)
# 	for i in range(m[1]):
# 		for ii in range(m[2]):
# 			print("%d x %d (%d)" % (m[1], m[2], m[0][i][ii]))
# 			printMatrix(m[0], m[1], m[2])
# 			solution = sorted_matrix_search(m[0], m[1], m[2], m[0][i][ii])
# 			print(solution)
# 			assert(m[0][i][ii] == m[0][solution[0]][solution[1]])
# 			print("\n\n")

testcases = [
	([[1]], 1, 1),
	([[15,20,70,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]], 4, 4)
]

for m in testcases:
	for i in range(m[1]):
		for ii in range(m[2]):
			print("%d x %d (%d)" % (m[1], m[2], m[0][i][ii]))
			printMatrix(m[0], m[1], m[2])
			solution = sorted_matrix_search(m[0], m[1], m[2], m[0][i][ii])
			print(solution)
			assert(m[0][i][ii] == m[0][solution[0]][solution[1]])
			print("\n\n")

