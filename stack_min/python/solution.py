#!/usr/local/bin/python3



class Stack:
	def __init__(self, N = 16):
		if N is not int or N <= 0:
			N = 16
		self.items = [None] * N
		self.N = N
		self.top = 0

	def size(self):
		return self.N

	def isEmpty(self):
		return self.top == 0

	def push(self, item):
		m = item
		if not self.isEmpty():
			print(self.top)
			m = self.items[self.top - 1][1]
		self.items[self.top] = [item, min(item, m)]
		self.top += 1

	def pop(self):
		if self.isEmpty():
			return None
		self.top -= 1
		return self.items[self.top][0]

	def peek(self):
		if self.isEmpty():
			return None
		return self.items[self.top - 1][0]

	def min(self):
		if self.isEmpty():
			return None
		return self.items[self.top - 1][1]

import random


x = Stack()
for i in range(x.size()):
	x.push(random.randint(0,100))

print(x.items)


