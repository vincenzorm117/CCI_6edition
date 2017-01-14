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

	def edge(self, a, b, val=None):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				return self.E[a][b]
		return None

	def connect(self, a, b, v=True):
		if isinstance(a, int) and isinstance(b, int):
			if 0 <= a and a < self.count and 0 <= b and b < self.count:
				self.E[a][b] = v

	def empty(self):
		return len(self.V) == 0


def build_order(G):
	if not isinstance(G, Graph) or G.count <= 0:
		return None
	visited = [False] * G.count
	q = []
	for i in range(G.count):
		noOutEdges = True
		for j in range(G.count):
			if G.E[i][j]:
				noOutEdges = False
				break
		if noOutEdges:
			q.append(i)
	order = []
	for n in q:
		order.append(G.V[n])
		p = [n]
		visited[n] = True
		while 0 < len(p):
			c = p.pop(0)
			for i in range(G.count):
				if G.E[i][c] and not visited[i]:
					p.append(i)
					visited[i] = True
					order.append(G.V[i])
	order.reverse()
	return order


testcases = [
	(list(range(6)), [(0,3),(5,1),(1,3),(5,0),(3,2)])
]

for t in testcases:
	g = Graph(t[0])
	for e in t[1]:
		g.connect(e[0],e[1])
	print(build_order(g))

