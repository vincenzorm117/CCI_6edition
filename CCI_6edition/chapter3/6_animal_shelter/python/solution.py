#!/usr/local/bin/python3

def rick(x,y, cond):
	print(x,y,cond)
	assert cond



# class AnimalStack:

# 	def __init__(self):
# 		self.catHead = None
# 		self.dogHead = None
# 		self.head = None

# 	def enqueue(self, item, isCatNotDog=True):
# 		s = Node(item, isCatNotDog)
# 		if self.isEmpty():
# 			self.head = s
# 			if isCatNotDog:
# 				self.catHead = s
# 			else:
# 				self.dogHead = s
# 		else:
# 			self.head.prev = s
# 			s.next = self.head
# 			self.head = s
# 			if isCatNotDog:
# 				s.nextOfType = self.catHead
# 				self.catHead = s
# 			else:
# 				s.nextOfType = self.dogHead
# 				self.dogHead = s

# 	def dequeueAny(self):
# 		if self.isEmpty():
# 			return None
# 		s = self.head
# 		if s.next is None:
# 			self.head = self.catHead = self.dogHead = None
# 		else:
# 			s.next.prev = None
# 			self.head = s.next
# 			if s.isCatNotDog:
# 				self.catHead = self.catHead.nextOfType
# 			else:
# 				self.dogHead = self.catHead.nextOfType
# 		s.clear()
# 		return str(s)


# 	def dequeueDog(self):
# 		if self.isEmpty():
# 			return None
# 		if self.dogHead.prev is None:
# 			return self.dequeueAny()
# 		else:
# 			dog = self.dogHead
# 			self.dogHead = dog.nextOfType
# 			dog.next.prev = dog.prev
# 			dog.prev.next = dog.next
# 			dog.clear()
# 			return str(dog)

# 	def dequeueCat(self):
# 		if self.isEmpty():
# 			return None
# 		if self.catHead.prev is None:
# 			return self.dequeueAny()
# 		else:
# 			cat = self.catHead
# 			self.catHead = cat.nextOfType
# 			cat.next.prev = cat.prev
# 			cat.prev.next = cat.next
# 			cat.clear()
# 			return str(cat)

# 	def peek(self):
# 		return self.head

# 	def isEmpty(self):
# 		return self.head is None

# 	def print(self):
# 		s = self.head
# 		print("(Head) --> ", end="")
# 		while s is not None:
# 			print(s, end=" ")
# 			s = s.next
# 		print()




class Node():
	def __init__(self, data=None, isCatNotDog=True):
		self.data = data
		self.isCatNotDog = isCatNotDog
		self.nextOfType = None
		self.next = None
		self.prev = None

	def clear(self):
		self.nextOfType = None
		self.next = None
		self.prev = None
    
	def __str__(self):
		return ("Cat" if self.isCatNotDog else "Dog") + "(" + str(self.data) + ")"


class AnimalQueue:

	def __init__(self):
		# First index is head and second is tail
		self.cat = [None, None]
		self.dog = [None, None]
		self.any = [None, None]

	def clear(self):
		self.cat = [None, None]
		self.dog = [None, None]
		self.any = [None, None]

	def enqueue(self, item, isCatNotDog=True):
		s = Node(item, isCatNotDog)
		type = self.cat if isCatNotDog else self.dog
		if self.isEmpty():
			self.any[0] = self.any[1] = s
			type[0] = type[1] = s
		else:
			self.any[1].next = s
			s.prev = self.any[1]
			self.any[1] = s
			if type[1] is not None:
				type[1].nextOfType = s
				type[1] = s
			else:
				type[0] = type[1] = s


	def dequeueAny(self):
		if self.isEmpty():
			return None
		head = self.any[0]
		type = self.cat if head.isCatNotDog else self.dog
		type[0] = type[0].nextOfType
		if head.next is not None:
			head.next.prev = None
			self.any[0] = head.next
		else:
			self.clear()
		head.clear()
		return str(head)

	def __dequeueType(self, isCatNotDog):
		if self.isEmpty():
			return None
		type = self.cat if isCatNotDog else self.dog
		if type[0] is None:
			return None
		head = type[0]
		if head.prev is None:
			return self.dequeueAny()
		else:
			head.prev.next = head.next
			type[0] = head.nextOfType
			if head.next is not None:
				head.next.prev = head.prev
			head.clear()
			return str(head)

	def dequeueDog(self):
		return self.__dequeueType(False)
				
	def dequeueCat(self):
		return self.__dequeueType(True)

	def peek(self):
		return self.head

	def isEmpty(self):
		return self.any[0] is None

	def print(self):
		s = self.any[0]
		print("(Head) --> ", end="")
		while s is not None:
			print(s, end=",")
			s = s.next
		print("X")


def unittest(values, dequeueTypes):
	x = AnimalQueue()
	for i in range(len(values)):
		x.enqueue(i,values[i])
	# x.print()
	for i in dequeueTypes:
		if i == 0:
			print(x.dequeueDog(), end=" ")
		elif i == 1:
			print(x.dequeueCat(), end=" ")
		else:
			print(x.dequeueAny(), end=" ")
	print()
	x.print()




def genvals(N, alpha):
	if N <= 0:
		return []
	alpha = vals = [[s] for s in alpha]
	if N <= 1:
		return alpha
	for i in range(N-1):
		n = []
		for l in vals:
			for a in alpha:
				n.append(l + a)
		vals = n
	return n

def numToType(x):
	if x == 0 or x == False:
		return "Dog"
	elif x == 1 or x == True:
		return "Cat"
	else:
		return "Any"

N = 3
# types = genvals(N, [True,False])
dequeueTypes = genvals(N, [0,1,2])
types = [[True, False,True]]
i = 0
for x in types:
	i += 1
	j = 0
	for y in dequeueTypes:
		j += 1
		print("==================")
		print("Test[{}][{}]".format(i,j))
		print(list(map(numToType,x)))
		print(list(map(numToType,y)))
		print("------------------")
		unittest(x, y)


# x = AnimalQueue()
# x.enqueue(6, True)
# x.enqueue(7, False)
# x.enqueue(8, True)
# x.print()
# print(x.dequeueAny())
# print(x.dequeueAny())
# print(x.dequeueAny())
# print(x.dequeueAny())


