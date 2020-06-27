#!/usr/local/bin/python3



def drawLine(screen, width, x1, x2, y):
	if len(screen) <= 0:
		return []
	def next(x):
		return min(7 - (x % 8) + x, x2)
	def index(x):
		return int(x/8)
	def mask(a,b):
		return ((2**(b - a + 1)) - 1) << (7 - b % 8)
	a = x1
	while True:
		b = next(a)
		if b == x2:
			screen[width*y + index(a)] = mask(a, b)
			break
		elif a == x1:
			screen[width*y + index(a)] = mask(a, b)
		else:
			screen[width*y + index(a)] = 0xFF
		a = b+1
	return screen

def printLineArea(screen, width):
	for i in range(width):
		for j in range(width):
			if 0 < screen[width*i + j]:
				s = str(bin(screen[width*i + j]))[2:]
				s = ('0' * (8 - len(s))) + s
				print(i,j, s)

def printScreen(screen, width):
	w = int(width/8)
	h = int(len(screen) / width)
	for j in range(h):
		print("%2d" % j, end=" ")
		for i in range(w):
			s = str(bin(screen[width*j + i]))[2:]
			s = ('0' * (8 - len(s))) + s
			print(s, end=" ")
		print()
	print()

testcases = [
	(16,0,15,8),
	(16,1,5,8),
	(16,1,1,8),
	(16,0,0,0),
	(8*4,3,16,8),
]

for t in testcases:
	print('Testcase: ', t)
	solution = drawLine([0]*(t[0]*t[0]), t[0], t[1], t[2], t[3])
	printLineArea(solution, t[0])
	printScreen(solution, t[0])
	print()


