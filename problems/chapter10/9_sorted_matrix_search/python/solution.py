#!/usr/local/bin/python3

from random import randint




def sorted_matrix_search(matrix, el):
    stack = [( (0,0), (len(matrix)-1, len(matrix[0])-1) )]

    while 0 < len(stack):
        origin, dest = stack.pop(0)
        print(origin, dest)
        # Check if element found
        if origin[0] == dest[0] and origin[1] == dest[1] and matrix[origin[0]][origin[1]] == el:
            return origin
        # Calculate mid coordinate
        smallerMid = (int((origin[0]+dest[0])/2), int((origin[1]+dest[1])/2))
        biggerMid = (min(smallerMid[0]+1, dest[0]), min(smallerMid[0]+1, dest[1]))
        print('MID:', smallerMid, biggerMid)

        # Check top left quadrant
        if matrix[origin[0]][origin[1]] <= el and el <= matrix[smallerMid[0]][smallerMid[1]]:
            stack.append( (origin, smallerMid) )
        # Check bottom left quadrant
        if matrix[origin[0]][biggerMid[1]] <= el and el <= matrix[smallerMid[0]][dest[1]]:
            stack.append( ((origin[0], biggerMid[1]), (smallerMid[0], dest[1])) )
        # Check top right quadrant
        if matrix[biggerMid[0]][origin[1]] <= el and el <= matrix[dest[0]][smallerMid[1]]:
            stack.append( ((biggerMid[0], origin[1]), (dest[0], smallerMid[1])) )
        # Check bottom right quadrant
        if matrix[biggerMid[0]][biggerMid[1]] <= el and el <= matrix[dest[0]][dest[1]]:
            stack.append( (biggerMid, dest) )

    # def recurse(matrix, origin, dest, el):
    #     if origin[0] == dest[0] and origin[1] == dest[1] and matrix[origin[0]][origin[1]] == el:
    #         return origin

    #     mid = (int((origin[0]+dest[0])/2), int((origin[1]+dest[1])/2))

    #     # Check top left quadrant
    #     if matrix[origin[0]][origin[1]] <= el and el <= matrix[mid[0]][mid[1]]:
    #         coordinate = recurse(matrix, origin, mid, el)
    #         if isinstance(coordinate, tuple):
    #             return coordinate
    #     # Check bottom left quadrant
    #     if matrix[origin[0]][mid[1]] <= el and el <= matrix[mid[0]][dest[1]]:
    #         coordinate = recurse(matrix, (origin[0], mid[1]), (mid[0], dest[1]), el)
    #         if isinstance(coordinate, tuple):
    #             return coordinate
    #     # Check top right quadrant
    #     if matrix[mid[0]][origin[1]] <= el and el <= matrix[dest[0]][mid[1]]:
    #         coordinate = recurse(matrix, (mid[0], origin[1]), (dest[0], mid[1]), el)
    #         if isinstance(coordinate, tuple):
    #             return coordinate
    #     # Check bottom right quadrant
    #     if matrix[mid[0]][mid[1]] <= el and el <= matrix[dest[0]][dest[1]]:
    #         coordinate = recurse(matrix, mid, dest, el)
    #         if isinstance(coordinate, tuple):
    #             return coordinate
    # return recurse(matrix, (0,0), (len(matrix)-1, len(matrix[0])-1), el)


# def sorted_matrix_search(matrix, M, N, el):
# 	if not isinstance(matrix, list):
# 		return None
# 	if len(matrix) <= 0 or len(matrix[0]) <= 0:
# 		return None
# 	row = [0, M-1]
# 	while row[0] < row[1]:
# 		mid = int((row[0] + row[1])/2) + 1
# 		if matrix[mid][0] <= el:
# 			row[0] = mid
# 		else:
# 			row[1] = mid-1
# 	row = row[0]
# 	col = [0, N-1]
# 	while col[0] < col[1]:
# 		mid = int((col[0] + col[1])/2) + 1
# 		if matrix[row][mid] <= el:
# 			col[0] = mid
# 		else:
# 			col[1] = mid-1
# 	col = col[0]
# 	return (row, col)




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


# for w in range(1,10):
# 	for h in range(1,10):
# 		m = genMatrix(w,h)
# 		for i in range(m[1]):
# 			for ii in range(m[2]):
# 				print("%d x %d (%d)" % (m[1], m[2], m[0][i][ii]))
# 				printMatrix(m[0], m[1], m[2])
# 				solution = sorted_matrix_search(m[0], m[0][i][ii])
# 				print(m[0][i][ii], m[0][solution[0]][solution[1]], solution)
# 				assert(m[0][i][ii] == m[0][solution[0]][solution[1]])

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
	([[15,20,70,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]], 4, 4),
	([[1]], 1, 1),
]

for m in testcases:
	for i in range(m[1]):
		for ii in range(m[2]):
			print("%d x %d (%d)" % (m[1], m[2], m[0][i][ii]))
			printMatrix(m[0], m[1], m[2])
			solution = sorted_matrix_search(m[0], m[0][i][ii])
			print(solution)
			assert(m[0][i][ii] == m[0][solution[0]][solution[1]])
			print("\n\n")

