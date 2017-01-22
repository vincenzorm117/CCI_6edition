#!/usr/local/bin/python3

from random import randint
from numpy import random as r




def randIsGirl():
	return r.binomial(1, 0.5, 1)[0] == 1
	# return randint(0,1)


def simulation(M):
	def genFamily():
		maleCount = 0
		isGirl = randIsGirl()
		while not isGirl:
			maleCount += 1
			isGirl = randIsGirl()
		return maleCount

	pop = {}
	maleCount = 0
	for _ in range(M):
		count = genFamily()
		if pop.get(count) is None:
			pop[count] = 0
		pop[count] += 1
		maleCount += count
	return maleCount

maleCounts = []
maleBuffer = 0.0
M = 10000
simCount = 100
for _ in range(simCount):
	currCount = simulation(M)
	maleCounts.append(currCount)
	maleBuffer += currCount
maleBuffer /= simCount
maleCounts.sort()

print(maleCounts[int(len(maleCounts)/2)])
print(maleBuffer)
