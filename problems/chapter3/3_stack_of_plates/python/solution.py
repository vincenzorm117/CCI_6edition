#!/usr/local/bin/python3

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



class SetOfStacks:
	def __init__(self,threshold):
		self.threshold = threshold
		self.stacks = [Stack()]
		self.topStack = 0

	def push(self,item):
		stack = self.stacks[self.topStack]
		if self.threshold <= stack.size():
			self.stacks.append(Stack())
			self.topStack += 1
		stack = self.stacks[self.topStack]
		stack.push(item)

	def pop(self):
		stack = self.stacks[self.topStack]
		item = stack.pop()
		if stack.size() == 0:
			self.stacks.pop()
			self.topStack -= 1
		return item

	def print(self):
		for x in self.stacks:
			x.print()

	def popAt(self, index):
		if 0 <= index and index < len(self.stacks):
			stack = self.stacks[index]
			return stack.pop()
		return None



x = SetOfStacks(3)

for i in range(20):
	x.push(i)

x.print()

print()
for i in range(3):
	print(x.pop(), end=", ")
print()

x.print()
print()
print(x.popAt(2))
x.print()

print()
for i in range(3):
	print(x.pop(), end=", ")
print()

x.print()
