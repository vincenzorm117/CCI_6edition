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



def bst_sequences(B):
	if not isinstance(B, BST):
		return
	root = B.root
	if root is None:
		print()
		return
	def permute(l):
		if not isinstance(l, (list)):
			return None
		if len(l) <= 0:
			return []
		perms = []
		L = len(l)
		stack = [(l,0)]
		while 0 < len(stack):
			c = stack.pop()
			if c[1] == L:
				perms.append(c[0])
			else:
				for i in range(c[1],L):
					c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
					stack.append((c[0][:], c[1]+1))
					c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
		return perms

	bag = [None] * B.height
	for i in range(B.height):
		bag[i] = list()
	q = [(root, 0)]
	while 0 < len(q):
		c = q.pop(0)
		bag[c[1]].append(c[0].data)
		if c[0].children[0] is not None:
			q.append((c[0].children[0], c[1]+1))
		if c[0].children[1] is not None:
			q.append((c[0].children[1], c[1]+1))

	permsBag = []
	for ls in bag:
		permsBag.append(permute(ls))

	def possibilities(bag):
		if not isinstance(bag, list) or len(bag) <= 0:
			return None
		s = [None] * len(bag)
		stack = []
		cnt = 0
		for n in bag[0]:
			stack.append((n,0))
		while 0 < len(stack):
			c = stack.pop()
			s[c[1]] = c[0]
			nxt = c[1]+1
			if len(s) <= nxt:
				# print(s)
				cnt += 1
				print([inner for outer in s for inner in outer])
			else:
				for c in bag[nxt]:
					stack.append((c,nxt))
	possibilities(permsBag)


testcases = [
	# [2,1,3],
	[9,5,15,2,7,12,17]
]

for t in testcases:
	b = BST()
	for i in t:
		b.insert(i)
	print("Test Case: ", t)
	bst_sequences(b)



