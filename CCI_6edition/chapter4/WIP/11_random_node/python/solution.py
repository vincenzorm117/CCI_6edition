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

	def getRandomNode():
		if self.root == None:
			return None
	

class BST_RAND():
	class Node:
		def __init__(self, data):
			self.data = data
			self.children = [None,None]
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.root = None
		self.height = 0
		self.nodes = []

	def insert(self, data):
	def find(self, data):
	def empty(self):
	def print(self):
	def getRandomNode():

testcases = [
	([2,1,3],[1], True),
	([9,5,15,2,7,12,17],[2], True),
	([2,1,3],[2,3,1], True),
	([9,5,15,2,7,12,17],[5,2,7], True),
	([2,1,3],[0],False),
	([9,5,15,2,7,12,17],[],False),
	([9,5,15,2,7,12,17],[5,2,7,1],False),
	([9,5,15,2,7,12,17],[9,15,12,17], False),
]

for t in testcases:
	T1, T2 = BST(), BST()
	for i in t[0]:
		T1.insert(i)
	for i in t[1]:
		T2.insert(i)
	print("Test Case: ", t, check_subtree(T1,T2), t[2])




