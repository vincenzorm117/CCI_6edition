#!/usr/local/bin/python3



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


class BST2(BST):
	def first_common_ancestor(self, a, b):
		if self.root is None:
			return None
		def pathToNode(root, data, height):
			if root is None or height <= 0:
				return []
			path = [None] * height
			q = [(root, 0)]
			while 0 < len(q):
				c = q.pop()
				path[c[1]] = c[0]
				if c[0].data == data:
					return path[:c[1]+1]
				if c[0].left is not None:
					q.append((c[0].left, c[1]+1))
				if c[0].right is not None:
					q.append((c[0].right, c[1]+1))
			return None

		height = self.height()
		pathA = pathToNode(self.root, a, height)
		pathB = pathToNode(self.root, b, height)
		L = min(len(pathA),len(pathB))
		c = self.root
		for i in range(L):
			if pathA[i] == pathB[i]:
				c = pathA[i]
			else:
				break
		return c

	


x = BST2()
testcase = [7,5,6,2,3,1,8,9]
for i in testcase:
	x.insert(i)
x.print()
print(x.first_common_ancestor(9,1))
