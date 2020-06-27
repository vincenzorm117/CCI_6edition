#!/usr/local/bin/python3




class Stack:
	def __init__(self, size = 16):
		if not isinstance(size, int) or size <= 0:
			size = 16
		self.items = [None] * size
		self.size = size
		self.top = 0
		self.count = 0

	def isEmpty(self):
		return self.top == 0
	
	def isFull(self):
		return self.top == self.size
	
	def push(self, item):
		if self.isFull():
			self.items = self.items + [None] * self.size
			self.size *= 2
		self.items[self.top] = item
		self.top += 1
		self.count += 1
	
	def pop(self):
		if self.isEmpty():
			return None
		self.top -= 1
		self.count -= 1
		return self.items[self.top]
	
	def peek(self):
		if self.isEmpty():
			return None
		return self.items[self.top - 1]


class StackMin():
	def __init__(self):
		self.stack = Stack()
		self.mins = Stack()

	def isEmpty(self):
		return self.stack.isEmpty()
	
	def isFull(self):
		return self.stack.isFull()

	def push(self, item):
		self.stack.push(item)
		currMin = self.mins.peek()
		if currMin is None or item <= currMin:
			self.mins.push(item)

	def pop(self):
		if self.isEmpty():
			return None
		m = self.stack.pop()
		if m == self.min():
			self.mins.pop()
		return m

	def peek(self):
		return self.stack.peek()

	def min(self):
		return self.mins.peek()

import random


x = StackMin()
print(x.min())
for i in range(20):
	r = random.randint(0,100)
	x.push(r)


for i in range(20):
	print(x.min(), x.pop())

