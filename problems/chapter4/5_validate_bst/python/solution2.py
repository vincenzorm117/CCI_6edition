#!/usr/local/bin/python3


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



def validate_bst(B):
	def minMax(a,b, isMin):
		isNone = (a is None, b is None)
		if isNone[0] and isNone[1]:
			return None
		elif isNone[0]:
			return b
		elif isNone[1]:
			return a
		return min(a,b) if isMin else max(a,b)
	if B is None:
		return True
	if B.root is None:
		return True
	q = [(B.root, None, None)]
	while 0 < len(q):
		c = q.pop()
		if c[1] is not None:
			if c[0].data < c[1]:
				return False
		if c[2] is not None:
			if c[2] < c[0].data:
				return False
		if c[0].left is not None:
			q.append((c[0].left, c[1], minMax(c[0].data, c[2], True)))
		if c[0].right is not None:
			q.append((c[0].right, minMax(c[0].data, c[1], False), c[2]))
	return True
		

testcases = [
	[(10,[]), (5,[1]), (20,[0]), (4,[1,1]), (8,[1,0]), (1,[0,0])],
	[(10,[]), (5,[1]), (20,[0]), (4,[1,1]), (8,[1,0])],
	[(10,[]), (5,[1]), (20,[0])],
	[],
	[(10,[]),(5,[1]),(20,[0]),(25,[1,0])],
	[(1,[]),(2,[0]),(3,[0,0]),(4,[0,0,0])]
]

for t in testcases:
	b = BinaryTree()
	for n in t:
		b.insert(n[0],n[1])
	print(t)
	print(validate_bst(b))


