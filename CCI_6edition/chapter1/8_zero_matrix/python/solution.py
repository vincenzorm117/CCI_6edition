#!/usr/local/bin/python3


def zero_matrix_with_data_structure(matrix):
	M = matrix.GetLength(0)
	N = matrix.GetLength(1)
	row = [False] * M
	col = [False] * N
	for x in range(M):
		for y in range(N):
			if matrix[x][y] == 0:
				row[x] = True
				col[y] = True
	for x in range(M):
		if row[x]:
			for i in range(N): 
				matrix[x][i] = 0
	for y in range(N):
		if col[y]:
			for i in range(M): 
				matrix[i][y] = 0
	return matrix


def zero_matrix(matrix):
	M = len(matrix)
	N = len(matrix[0])
	
	for x in range(M):
		for y in range(N):
			if matrix[x][y] == 0:
				matrix[0][y] = 0
				matrix[x][0] = 0

	for x in range(M):
		if matrix[x][0] == 0:
			for i in range(N):
				matrix[x][i] = 0

	for y in range(N):
		if matrix[0][y] == 0:
			for i in range(M):
				matrix[i][y] = 0
				
	return matrix



m = zero_matrix(input())
M = len(matrix)
N = len(matrix[0])

for x in range(M):
	for y in range(N):
		print(m[x][y], end="")
	print()


	
	

