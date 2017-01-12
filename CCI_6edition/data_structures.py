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

#!/usr/local/bin/python3


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

	def remove(self, data):
		# TODO




