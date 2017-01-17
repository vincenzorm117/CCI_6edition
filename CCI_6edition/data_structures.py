#!/usr/local/bin/python3


####################################################################################
####################################################################################
####################################################################################
####################################################################################

class BitVector:
	def __init__(self, size=1):
		if not isinstance(size, int):
			size = 1
		self.vector = [0] * size

	def __getitem__(self, i):
		if not isinstance(i, int):
			return False
		chunkIndex = int(i / 64)
		if chunkIndex < 0 or len(self.vector) <= chunkIndex:
			return False
		chunk = self.vector[chunkIndex]
		index = int(i % 64)
		return ((1 << index & chunk) >> index) == 1

	def __setitem__(self, i, val):
		if not isinstance(i, int):
			return None
		if isinstance(val, bool):
			val = bool(val)
		chunkIndex = int(i / 64)
		if chunkIndex < 0 or len(self.vector) <= chunkIndex:
			self.vector.extend([0] * (1 + (chunkIndex - len(self.vector))))
		chunk = self.vector[chunkIndex]
		index = int(i % 64)
		if val:
			chunk |= (1 << index)
		else:
			chunk &= ~(1 << index)
		self.vector[chunkIndex] = chunk

	def print(self):
		for v in self.vector:
			for i in range(64):
				print(((1 << i & v) >> i), end="")
		print()



####################################################################################
####################################################################################
####################################################################################
####################################################################################


class Stack:
	def __init__(self, size = 16):
		if not isinstance(size, int) or size <= 0:
			size = 16
		self.items = [None] * size
		self.size = size
		self.top = 0
		self.count = 0

	def isEmpty(self):
		return self.top == 0
	
	def isFull(self):
		return self.top == self.size
	
	def push(self, item):
		if self.isFull():
			self.items = self.items + [None] * self.size
			self.size *= 2
		self.items[self.top] = item
		self.top += 1
		self.count += 1
	
	def pop(self):
		if self.isEmpty():
			return None
		self.top -= 1
		self.count -= 1
		return self.items[self.top]
	
	def peek(self):
		if self.isEmpty():
			return None
		return self.items[self.top - 1]


####################################################################################
####################################################################################
####################################################################################
####################################################################################

# class Queue:
	# TODO


####################################################################################
####################################################################################
####################################################################################
####################################################################################


class BinaryTree:
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None

	def insert(self, data, path):
		if self.root is None:
			self.root = self.Node(data)
			return
		curr = self.root
		for isLeft in path:
			if isLeft:
				if curr.left is not None:
					curr = curr.left
				else:
					curr.left = self.Node(data)
					continue
			else:
				if curr.right is not None:
					curr = curr.right
				else:
					curr.right = self.Node(data)
					continue


	def find(self, data):
		if self.root is None:
			print()
			return
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			if c.data == data:
				return c
			if c.left is not None:
				q.append(c.left)
			if c.right is not None:
				q.append(c.right)

	def empty(self):
		return self.root == None

	def print(self):
		if self.root is None:
			print()
			return
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			print(c)
			if c.left is not None:
				q.append(c.left)
			if c.right is not None:
				q.append(c.right)
		print()

	def height(self):
		if self.root is None:
			return 0
		q = [(0,self.root)]
		max = 0
		while 0 < len(q):
			c = q.pop(0)
			if max < c[0]:
				max = c[0]
			if c[1].left is not None:
				q.append((c[0]+1, c[1].left))
			if c[1].right is not None:
				q.append((c[0]+1, c[1].right))
		return max+1



####################################################################################
####################################################################################
####################################################################################
####################################################################################



class BST:
	class Node:
		def __init__(self, data):
			self.data = data
			self.children = [None,None]
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None
		self.height = 0

	def insert(self, data):
		if self.root is None:
			self.height = 1
			self.root = self.Node(data)
			return
		curr = self.root
		height = 0
		while curr is not None:
			height += 1
			index = 0 if data <= curr.data else 1
			if curr.children[index] is None:
				curr.children[index] = self.Node(data)
				height += 1
				break
			else:
				curr = curr.children[index]
		self.height = max(self.height, height)

	def find(self, data):
		curr = self.root
		while curr is not None and curr.data != data:
			curr = curr.children[0] if data <= curr.data else curr.children[1]
		return curr

	def pathToNode(self, data):
		if self.root is None or self.height <= 0:
			return []
		path = [None] * self.height
		q = [(self.root, 0)]
		while 0 < len(q):
			c = q.pop()
			path[c[1]] = c[0]
			if c[0].data == data:
				return path[:c[1]+1]
			if c[0].left is not None:
				q.append((c[0].left, c[1]+1))
			if c[0].right is not None:
				q.append((c[0].right, c[1]+1))
		return []

	def empty(self):
		return self.root == None

	def print(self):
		if self.root is None:
			print()
			return
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			print(c)
			if c.children[0] is not None:
				q.append(c.children[0])
			if c.children[1] is not None:
				q.append(c.children[1])
		print()

	def parent(self, node):
		if node is None or self.root is None:
			return None
		if node.data == self.root.data:
			return None
		q = [self.root]
		while 0 < len(q):
			c = q.pop(0)
			if c.children[0] is not None:
				if c.children[0].data == node.data:
					return c
				q.append(c.children[0])
			if c.children[1] is not None:
				if c.children[1].data == node.data:
					return c
				q.append(c.children[0])
		return None
		
	# def remove(self, data):
		


####################################################################################
####################################################################################
####################################################################################
####################################################################################



class Graph():
	def __init__(self, data=[]):
		if not isinstance(data, list):
			data = []
		self.V = data[:]
		self.count = len(self.V)
		self.E = []
		for i in range(self.count):
			self.E.append([None] * self.count)

	def add(self, data):
		self.V.append(data)
		self.count += 1
		for E in self.E:
			E.append(None)
		self.E.append([None] * self.count)

	def remove(self, index):
		if not isinstance(index, int):
			return None
		if index < 0 or index <= self.count:
			return None
		ret = self.V[index]
		del self.V[index]
		del self.E[index]
		for e in self.E:
			del e[index]
		return ret

	def print(self):
		for e in self.E:
			print(e)

	def edge(self, a, b, val=None):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				return self.E[a][b]
		return None

	def connect(self, a, b, v = True):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				self.E[a][b] = v

	def size(self):
		return len(self.V)

	def empty(self):
		return len(self.V) == 0


####################################################################################
####################################################################################

def top_sort(G):
	if not isinstance(G, Graph) or G.count <= 0:
		return None
	visited = [False] * G.count
	q = []
	for i in range(G.count):
		noOutEdges = True
		for j in range(G.count):
			if G.E[i][j]:
				noOutEdges = False
				break
		if noOutEdges:
			q.append(i)
	order = []
	for n in q:
		order.append(G.V[n])
		p = [n]
		visited[n] = True
		while 0 < len(p):
			c = p.pop(0)
			for i in range(G.count):
				if G.E[i][c] and not visited[i]:
					p.append(i)
					visited[i] = True
					order.append(G.V[i])
	order.reverse()
	return order
	


####################################################################################
####################################################################################
####################################################################################
####################################################################################
# Nice Functions

def possibilities(bags):
		if not isinstance(bags, list) or len(bags) <= 0:
			return None
		s = [None] * len(bags)
		stack = []
		for n in bags[0]:
			stack.append((n,0))
		while 0 < len(stack):
			c = stack.pop()
			s[c[1]] = c[0]
			nxt = c[1]+1
			if len(s) <= nxt:
				print(s)
			else:
				for c in bags[nxt]:
					stack.append((c,nxt))


def permute(l):
	if not isinstance(l, (list)) or len(l) <= 0:
		return None
	L = len(l)
	stack = [(l,0)]
	while 0 < len(stack):
		c = stack.pop()
		if c[1] == L:
			for i in c[0]:
				print(i,end="")
			print()
		else:
			for i in range(c[1],L):
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
				stack.append((c[0][:], c[1]+1))
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]



def genvals(N, alpha):
	if N <= 0:
		return []
	alpha = vals = [[s] for s in alpha]
	if N <= 1:
		return alpha
	for i in range(N-1):
		n = []
		for l in vals:
			for a in alpha:
				n.append(l + a)
		vals = n
	return n

