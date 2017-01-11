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

class BST:
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = self.Node(data)
			return
		curr = self.root
		while True:
			if data <= curr.data:
				if curr.left is None:
					curr.left = self.Node(data)
					break
				else:
					curr = curr.left
			else:
				if curr.right is None:
					curr.right = self.Node(data)
					break
				else:
					curr = curr.right

	def find(self, data):
		curr = self.root
		while curr is not None and curr.data != data:
			curr = curr.left if data <= curr.data else curr.right
		return curr.data

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


