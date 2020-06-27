#!/usr/local/bin/python3



def robot_grid(grid):
	n, m = len(grid), len(grid[0])
	ways = []
	for i in range(n):
		ways.append([0]*m)
	ways[0][0] = 1
	for x in range(n):
		for y in range(m):
			if grid[x][y]:
				if x == 0 and y == 0:
					continue
				elif x == 0 and y != 0:
					ways[x][y] = ways[0][y-1]
				elif x != 0 and y == 0:
					ways[x][y] = ways[x-1][0]
				else:
					ways[x][y] = ways[x-1][y-1]
	return ways[n-1][m-1]




def find_path_recursive_no_memo(grid):
	q = []
	def fp(r,c):
		if r == 0 and c == 0:
			q.append((r,c))
			return True
		if grid[r][c]:
			p = False
			if r != 0:
				p = p or fp(r-1, c)
			if c != 0:
				p = p or fp(r, c-1)
			if p:
				q.append((r,c))
			return p
		else:
			return False
	n,m = len(grid), len(grid[0])
	fp(n-1,m-1)
	return q



def find_path_recursive(grid):
	n,m = len(grid), len(grid[0])
	q = []
	mask = []
	for _ in range(n):
		mask.append([-1]*m)
	def fp(r,c):
		if mask[r][c] != -1:
			return mask[r][c] == 1
		if r == 0 and c == 0:
			q.append((r,c))
			return True
		if grid[r][c]:
			p = False
			if r != 0: p = p or fp(r-1, c)
			if c != 0: p = p or fp(r, c-1)
			if p: q.append((r,c))
			mask[r][c] = 1 if p else 0
			return p
		else:
			mask[r][c] = 0
			return False
	fp(n-1,m-1)
	return q


def find_path(grid):
	n,m = len(grid), len(grid[0])
	path, mask = [], []
	for _ in range(n):
		mask.append([-1]*m)
	mask[0][0] = 1
	print_grid(mask)
	q = [(n-1,m-1)]
	while 0 < len(q):
		c = q.pop()
		print(c)
		print(path)
		r, c = c[0], c[1]

		if r == 0 and c == 0:
			path.append((0,0))
		elif r != 0 and c == 0:
			if grid[r-1][c]:
				R = mask[r-1][c]
				if R == 1:
					path.append(r,c)
				elif R == -1:
					q.append((r,c))
					q.append((r-1,c))
		elif r == 0 and c != 0:
			if grid[r][c-1]:
				C = mask[r][c-1]
				if C == 1:
					path.append(r,c)
				elif C == -1:
					q.append((r,c))
					q.append((r,c-1))
		else:
			R, C = mask[r-1][c], mask[r][c-1]
			if R == 1 or C == 1:
				path.append(r,c)
			elif R == -1 and C == -1:
				if grid[r-1][c] and grid[r][c-1]:
					q.append((r,c))
					q.append((r-1,c))
					q.append((r,c-1))
			elif R == -1 and C == 0:
				if grid[r-1][c]: 
					q.append((r,c))
					q.append((r-1,c))
			elif R == 0 and C == -1:
				if grid[r][c-1]: 
					q.append((r,c))
					q.append((r,c-1))

		

	return path
		# if r != 0 and c != 0:
		# 	bols = (mask[r-1][c] == -1, mask[r][c-1] == -1)
		# 	if bols[0] or bols[1]:
		# 		if bols[0]:
		# 			q.append((r-1,c))
		# 		if bols[1]:
		# 			q.append((r,c-1))
		# 		q.append(c)
		# 	else:
		# 		mask[r][c] = mask[r-1][c] == 1 or mask[r][c-1] == 1
		# elif r == 0 and c != 0:
		# 	bols = (mask[r-1][c] == -1, mask[r][c-1] == -1)
		# elif r != 0 and c == 0:









 

from random import randint

def generate_grid():
	n, m = 5, 5
	grid = []
	for _ in range(n):
		grid.append([True]*m)
	loc = [0,0]
	for y in range(n):
		for x in range(m):
			if randint(1,100) < 15:
				grid[y][x] = False
	return grid

def printGrid(g):
	n,m = len(g), len(g[0])
	for y in range(n):
		for x in range(m):
			print(1 if g[y][x] else 0, end=" ")
		print()

def print_grid(g):
	n,m = len(g), len(g[0])
	for y in range(n):
		for x in range(m):
			print(g[y][x], end=" ")
		print()



g = generate_grid()
printGrid(g)
print(find_path_recursive_no_memo(g))
print()
print(find_path_recursive(g))
print()
print(find_path(g))

