#!/usr/local/bin/python3


def rotate_matrix_book_solution(matrix):
	N = len(matrix)
	M = len(matrix[0])
	if N != M or N == 0:
		return matrix

	for layer in range(int(N/2)):
		first = layer
		last = N - 1 - layer
		for i in range(first,last):
			offset = i - first
			top = matrix[first][i]
			matrix[first][i] = matrix[last - offset][first]; 			
			matrix[last - offset][first] = matrix[last][last - offset]; 
			matrix[last][last - offset] = matrix[i][last]; 
			matrix[i][last] = top; 
	return matrix


def rotate_matrix(matrix, clockwise = True):
	N = len(matrix)
	M = len(matrix[0])
	if N != M or N == 0:
		return matrix
	if N == 1:
		return matrix

	if clockwise:
		for d in range(N):
			for i in range(N-d*2-1):
				matrix[N-1-d][N-1-i-d] ^= matrix[N-1-i-d][0+d]
				matrix[N-1-i-d][0+d] ^= matrix[N-1-d][N-1-i-d]
				matrix[N-1-d][N-1-i-d] ^= matrix[N-1-i-d][0+d]

				matrix[i+d][N-1-d] ^= matrix[N-1-d][N-1-i-d]
				matrix[N-1-d][N-1-i-d] ^= matrix[i+d][N-1-d]
				matrix[i+d][N-1-d] ^= matrix[N-1-d][N-1-i-d]

				matrix[0+d][i+d] ^= matrix[i+d][N-1-d]
				matrix[i+d][N-1-d] ^= matrix[0+d][i+d]
				matrix[0+d][i+d] ^= matrix[i+d][N-1-d]
	else:
		for d in range(N):
			for i in range(N-d*2-1):
				matrix[0+d][i+d] ^= matrix[i+d][N-1-d]
				matrix[i+d][N-1-d] ^= matrix[0+d][i+d]
				matrix[0+d][i+d] ^= matrix[i+d][N-1-d]

				matrix[i+d][N-1-d] ^= matrix[N-1-d][N-1-i-d]
				matrix[N-1-d][N-1-i-d] ^= matrix[i+d][N-1-d]
				matrix[i+d][N-1-d] ^= matrix[N-1-d][N-1-i-d]

				matrix[N-1-d][N-1-i-d] ^= matrix[N-1-i-d][0+d]
				matrix[N-1-i-d][0+d] ^= matrix[N-1-d][N-1-i-d]
				matrix[N-1-d][N-1-i-d] ^= matrix[N-1-i-d][0+d]
	return matrix

	


def print_matrix(m):
	N = len(m)
	for i in range(N):
		for j in range(N):
			print(m[i][j],end=" ")
		print()
	print()

def foo(matrix):
	print_matrix(matrix)
	m = rotate_matrix_book_solution(matrix)
	print_matrix(m)



m0 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
m1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
m3 = [[1,2],[3,4]]
m4 = [[1]]

m = [m0,m1,m2,m3,m4]

for e in m:
	foo(e)