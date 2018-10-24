#!/usr/local/bin/python3



class BST:
	class Node:
		def __init__(self, data):
			self.data = data
			self.child = [None,None]
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
			if curr.child[index] is None:
				curr.child[index] = self.Node(data)
				height += 1
				break
			else:
				curr = curr.child[index]
		self.height = max(self.height, height)

	def find(self, data):
		curr = self.root
		while curr is not None and curr.data != data:
			curr = curr.child[0] if data <= curr.data else curr.child[1]
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
			if c.child[0] is not None:
				q.append(c.child[0])
			if c.child[1] is not None:
				q.append(c.child[1])
		print()

	# def parent(self, node):
	# def remove(self, data):
		

def paths_with_sum(B, sum):
	if B is None or B.empty():
		return []
	def countSumPaths(root, sum):
		if root is None:
			return 0
		pathCount = 0
		q = [(root, root.data)]
		while 0 < len(q):
			c = q.pop(0)
			if c[1] == sum:
				pathCount += 1
			if c[0].child[0] is not None:
				q.append((c[0].child[0], c[0].data + c[1]))
			if c[0].child[1] is not None:
				q.append((c[0].child[1], c[0].data + c[1]))
		return pathCount

	count = 0
	q = [B.root]
	while 0 < len(q):
		c = q.pop(0)
		count += countSumPaths(c, sum)
		if c.child[0] is not None:
			q.append(c.child[0])
		if c.child[1] is not None:
			q.append(c.child[1])
	return count



testcases = [
	# [5,2,7,1,3,6,8],
	[7,3,10,2,5,8,1,4,6,9]
]

for t in testcases:
	a = BST()
	for i in t:
		a.insert(i)
	print(paths_with_sum(a, 1))





