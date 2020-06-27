#!/usr/local/bin/python3

class S1:
	def __init__(self, N = 100):
		self.items = [None] * N
		self.top = [0,1,2]
		self.N = N

	def push(self, item, s):
		if s in [0,1,2] and self.top[s] < self.N:
			self.items[self.top[s]] = item
			self.top[s] += 3
		return None

	def pop(self, s):
		if s in [0,1,2] and 2 < self.top[s]:
			self.top[s] -= 3
			return self.items[self.top[s]]
		return None

	def peek(self, s):
		if s in [0,1,2] and 2 < self.top[s]:
			return self.items[self.top[s] - 3]
		return None

	def isEmpty(self, s):
		if s in [0,1,2]:
			return self.top[s] < 3
		return None


# x = S1()
# x.push(6,0)
# x.push(48,1)
# x.push(54,2)
# print(x.pop(2))
# print(x.pop(0))
# print(x.pop(1))



class S2:
	def __init__(self, N = 100):
		self.items = [None] * N
		self.top = [0, int(N / 3), int(N * 2 / 3), N]
		self.base = self.top[:]
		self.N = N

	def push(self, item, s):
		if s in [0,1,2] and self.top[s] < self.base[s+1]:
			self.items[self.top[s]] = item
			self.top[s] += 1
		return None

	def pop(self, s):
		if s in [0,1,2] and self.base[s] < self.top[s]:
			self.top[s] -= 1
			return self.items[self.top[s]]
		return None

	def peek(self, s):
		if s in [0,1,2] and self.base[s] < self.top[s]:
			return self.items[self.top[s]-1]
		return None


	def isEmpty(self, s):
		if s in [0,1,2]:
			return self.top[s] != self.base[s]
		return None


# x = S2()
# x.push(7,0)
# x.push(4,1)
# x.push(5,2)
# print(x.pop(2))
# print(x.pop(0))
# print(x.pop(1))



class S3:
	def __init__(self, N = 100):
		self.items = [None] * N
		self.top = [0, int(N / 3), N-1]
		self.base = int(N / 3)
		self.N = N

	def push(self, item, s):
		if s == 0 and self.top[0] < self.base:
			self.items[self.top[0]] = item
			self.top[s] += 1
		elif s == 1 and self.top[1] < self.top[2]:
			self.items[self.top[s]] = item
			self.top[s] += 1
		elif s == 2 and self.top[1] < self.top[2]:
			self.items[self.top[s]] = item
			self.top[s] -= 1
		print(self.items)
		return None

	def pop(self, s):
		if not self.isEmpty(s):
			if s == 0 or s == 1:
				self.top[s] -= 1
				return self.items[self.top[s]]
			elif s == 2:
				self.top[s] += 1
				return self.items[self.top[s]]
		return None

	def peek(self, s):
		if not self.isEmpty(s):
			if s == 0 or s == 1:
				return self.items[self.top[s] - 1]
			elif s == 2:
				return self.items[self.top[s] + 1]
		return None


	def isEmpty(self, s):
		if s == 0 and self.top[s] == 0:
			return True
		elif s == 1 and self.top[s] == self.base:
			return True
		elif s == 2 and self.top[s] == self.N-1:
			return True
		return False


x = S3(20)
# for i in range(10):
# 	x.push(0,0)

import random

for i in range(15):
	x.push(i,random.randint(1,2))

