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



class BinaryTree2(BinaryTree):
	
	# def validate_bst2(self):
		# validate by taking root and checking 
		# 	that it is greater than all elements in
		# 	left subtree and same idea for right subtree

	def validate_bst(self):
		def BSTPlaced(root, target):
			c = root
			while c is not None:
				if c.data == target:
					return True
				if target < c.data:
					c = c.left
				else:
					c = c.right
			return False

		if self.root is None:
			return True
		q = []
		if self.root.left is not None:
			q.append(self.root.left)
		if self.root.right is not None:
			q.append(self.root.right)
		while 0 < len(q):
			c = q.pop(0)
			if not BSTPlaced(self.root, c.data):
				return False
			if c.left is not None:
				q.append(c.left)
			if c.right is not None:
				q.append(c.right)
		return True

t = [
	(10,[]),
	(5,[1]),
	(20,[0]),
	(4,[1,1]),
	(8,[1,0]),
	(1,[0,0]),
]

b = BinaryTree2()
for n in t:
	b.insert(n[0],n[1])
print(b.validate_bst())

