#!/usr/local/bin/python3


class LL:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
		def __str__(self):
			return str(self.data)

	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, data):
		if self.head is None:
			self.head = self.Node(data)
			self.tail = self.head
			return
		self.tail.next = self.Node(data)
		self.tail = self.tail.next

	def print(self):
		c = self.head
		while c is not None:
			print(c,end=" => ")
			c = c.next
		print("X")





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

	def list_of_depths(self):
		if self.root == None:
			return []
		q = [(0,self.root)]
		L = b.height()
		a = []
		for i in range(L):
			a.append(LL())
		while 0 < len(q):
			c = q.pop(0)
			a[c[0]].insert(c[1])
			if c[1].left is not None:
				q.append((c[0]+1, c[1].left))
			if c[1].right is not None:
				q.append((c[0]+1, c[1].right))
		return a


b = BST()
for i in [5,2,8,1,4,7,9,0,3,6]:
	b.insert(i)

c = b.list_of_depths()
for l in c:
	l.print()



