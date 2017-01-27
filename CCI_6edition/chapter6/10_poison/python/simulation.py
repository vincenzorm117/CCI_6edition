#!/usr/local/bin/python3

from random import randint

def simulation():
	def experiment(bottles):
		strips = [0] * 10
		for index in range(1000):
			if bottles[index]:
				binForm = list(map(lambda x: int(x), list(bin(index))[2:]))
				binForm.reverse()
				L = len(binForm)
				for b in range(L):
					strips[b] = strips[b] or binForm[b] == 1
				break
		return list(map(lambda x: 1 if x else 0, strips))



	bottles = [False] * 1000
	poisonedBottleNum = randint(0,999)
	bottles[poisonedBottleNum] = True
	strips = experiment(bottles)
	print(strips)

simulation()