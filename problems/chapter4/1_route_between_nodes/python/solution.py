#!/usr/local/bin/python3

class Graph():
	def __init__(self, data=[]):
		if not isinstance(data, list):
			data = []
		self.V = data[:]
		self.count = len(self.V)
		self.E = []
		for i in range(self.count):
			self.E.append([None] * self.count)

	def add(self, data):
		self.V.append(data)
		self.count += 1
		for E in self.E:
			E.append(None)
		self.E.append([None] * self.count)

	def remove(self, index):
		if not isinstance(index, int):
			return None
		if index < 0 or index <= self.count:
			return None
		ret = self.V[index]
		del self.V[index]
		del self.E[index]
		for e in self.E:
			del e[index]
		return ret

	def print(self):
		for e in self.E:
			print(e)

	def get(self, a, b):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				return self.E[a][b]
		return None

	def connect(self, a, b, v = True):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				self.E[a][b] = v

	def size(self):
		return len(self.V)

	def empty(self):
		return len(self.V) == 0



def route_between_nodes(G,a,b):
	if not isinstance(G, Graph):
		return False
	if G.empty():
		return False
	count = G.size()
	visited = [False] * count
	visited[a] = True
	stack = []
	stack.append(a)
	while 0 < len(stack):
		c = stack.pop()
		if c == b:
			return True
		for i in range(count):
			if G.get(c,i) and not visited[i]:
				stack.append(i)
				visited[i] = True
	return False

size = 10
a = Graph(list(range(size)))
for i in range(size-1):
	a.connect(i, i+1)
a.connect(int(size / 2), 0)

print(route_between_nodes(a,0,size-1))

