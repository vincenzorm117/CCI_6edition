#!/usr/local/bin/python3

def rick(x,y, cond):
	print(x,y,cond)
	assert cond


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.isEmpty():
			return None
		return self.items.pop()

	def peek(self):
		if( 0 < len(self.items) ):
			return self.items[len(self.items) - 1]
		return None

	def size(self):
		return len(self.items)

	def print(self):
		print(self.items, end=" ")
		print()


class SortStack:
	def __init__(self):
		self.s = Stack()

	def push(self, item):
		print(item)
		other = Stack()
		while not self.s.isEmpty() and self.s.peek() < item:
			other.push(self.s.pop())
		self.s.push(item)
		while not other.isEmpty():
			self.s.push(other.pop())

	def pop(self):
		return self.s.pop()

	def peek(self):
		return self.s.peek()

	def isEmpty(self):
		return self.s.isEmpty()
	
	def print(self):
		self.s.print()

import random

x = SortStack()
for i in range(10):
	x.push(random.randint(0,20))
	# x.push(10 - i)

x.print()

x0 = x.pop()
for i in range(9):
	x1 = x.pop()
	rick(x0,x1, x0 <= x1)
	x0 = x1





