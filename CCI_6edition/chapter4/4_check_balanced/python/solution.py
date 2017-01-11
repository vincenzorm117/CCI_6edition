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
	def check_balanced_recursive(self):
		if self.root is None:
			return True
		def _is_balanced(root):
			if root is None:
				return (0,True)
			L = _is_balanced(root.left)
			R = _is_balanced(root.right)
			return (max(L[0],R[0]) + 1, abs(L[0] - R[0]) <= 1 and L[1] and R[1])

		return _is_balanced(self.root)[1]


	def check_balanced(self):
		if self.root is None:
			return True
		q = [self.root.left, self.root.right]
		heights = {}
		d = { 	self.root: None, 
				self.root.left: self.root, 
				self.root.right: self.root }
		leaves = []
		while 0 < len(q):
			c = q.pop(0)
			if c is None:
				continue
			L = c.left is None
			R = c.right is None
			if not L:
				q.append(c.left)
				d[c.left] = c
			if not R:
				q.append(c.right)
				d[c.right] = c
			if L and R:
				leaves.append(c)
		while 0 < len(leaves):
			c = leaves.pop(0)
			L = R = 0
			if c.left is not None:
				L = heights.get(c.left)
			if c.right is not None:
				R = heights.get(c.right)
			if L is None:
				L = 0
			if R is None:
				R = 0
			if 1 < abs(L - R):
				return False
			g = max(L,R) + 1
			heights[c] = g
			parent = d[c]
			if parent is not None:
				leaves.append(parent)
		return True
 


testcases = [
	([], True),
	([1], True),
	([1,2], True),
	([2,1], True),
	([2,1,3], True),
	([5,2,1,4], False),
	([3,2,4,1], True),
	([5,3,6,1,4], True),
	([7,5,8,3,9], True),
	([9,7,15,3,11], True),
	([9,7,20,3,8,15,22,1,4], True),
	([9,7,20,3,15,22,1,4], False),
	([9,7,20,3,1,4], False),
	([5,3,2], False),
	([9,7,4,1,2], False),
	([20,15,10,17,5,12], False),
	([30,20,40,10,28,1,16,5], False),
]

for t in testcases:
	b = BST2()
	for i in t[0]:
		b.insert(i)
	print(t[0])
	assert b.check_balanced() == t[1]


# a = BST2()
# for i in [5,2,1,4]:
# 	a.insert(i)
# print(a.check_balanced())


