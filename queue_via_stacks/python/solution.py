#!/usr/local/bin/python3

def rick(x,y):
	print(x,y,x == y)
	assert x == y


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


class MyQueue:
	def __init__(self):
		self.stacks = [Stack(), Stack()]

	def enqueue(self, item):
		stack = self.stacks[0]
		stack.push(item)

	def dequeue(self):
		if self.isEmpty():
			return None
		main  = self.stacks[0]
		other = self.stacks[1]
		while not main.isEmpty():
			other.push(main.pop())
		ret = other.pop()
		while not other.isEmpty():
			main.push(other.pop())
		return ret


	def peek(self):
		if self.isEmpty():
			return None
		main  = self.stacks[0]
		other = self.stacks[1]
		while not main.isEmpty():
			other.push(main.pop())
		ret = other.peek()
		while not other.isEmpty():
			main.push(other.pop())
		return ret


	def isEmpty(self):
		return self.stacks[0].isEmpty()

	def print(self):
		print("0: ", end="")
		self.stacks[0].print()
		print()
		print("1: ", end="")
		self.stacks[1].print()

print("Test 1")
x = MyQueue()

for i in range(6):
	x.enqueue(i)

rick(x.peek(), 0)

for i in range(3):
	rick(x.dequeue(), i)

x.print()
print()



class MyQueue2:
	def __init__(self):
		self.stacks = [Stack(), Stack()]
		self.main = 0

	def __flip(self):
		main  = self.stacks[self.main]
		other = self.stacks[1 - self.main]
		while not main.isEmpty():
				other.push(main.pop())
		self.main = 1 - self.main

	def enqueue(self, item):
		if self.main == 1:
			self.__flip()			
		stack = self.stacks[self.main]
		stack.push(item)

	def dequeue(self):
		if self.isEmpty():
			return None
		if self.main == 0:
			self.__flip()	
		main = self.stacks[self.main]
		return main.pop()


	def peek(self):
		if self.isEmpty():
			return None
		if self.main == 0:
			self.__flip()	
		main = self.stacks[self.main]
		return main.peek()


	def isEmpty(self):
		return self.stacks[self.main].isEmpty()

	def print(self):
		print("0: ", end="")
		self.stacks[0].print()
		print()
		print("1: ", end="")
		self.stacks[1].print()


print("Test 2")
x2 = MyQueue2()

for i in range(6):
	x2.enqueue(i)

rick(x2.peek(), 0)

for i in range(3):
	rick(x2.dequeue(), i)

x2.print()
print()



