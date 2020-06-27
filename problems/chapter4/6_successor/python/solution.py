#!/usr/local/bin/python3


class BST:
	class Node:
		def __init__(self, data, parent=None):
			self.data = data
			self.children = [None,None]
			self.parent = parent
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
				curr.children[index] = self.Node(data, curr)
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

	def __Calcheight(self):
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


class BST2(BST):
	def successor(self, node):
		if self.root is None:
			return None
		if node.children[1] is None:
			c = node
			while True:
				if c.parent is None:
					return None
				if c.parent.children[0] == c:
					return c.parent
				c = c.parent
		c = node.children[1]
		while c.children[0] is not None:
			c = c.children[0]
		return c


x = BST2()
testcase = [15,7,30,4,10,22,32,8,16,26,37,23,29]
for i in testcase:
	x.insert(i)

for i in testcase:
	print(i, x.successor(x.find(i)))





