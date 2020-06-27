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


	# def remove(self, data):



def minimal_tree(array):
	L = len(array)
	t = BST()
	queue = [(0,L)]
	while 0 < len(queue):
		c = queue.pop(0)
		if c[0] < c[1]:
			m = int((c[0] + c[1]) / 2)
			if c[0] < m:
				queue.append((c[0],m))
			if (m+1) < c[1]:
				queue.append((m+1,c[1]))
			t.insert(array[m])
	return t

a = minimal_tree(list(range(10)))
a.print()
print(a.height())



