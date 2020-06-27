#!/usr/local/bin/python3

import sys


class BitVector:
	def __init__(self, size=1):
		if not isinstance(size, int):
			size = 1
		self.vector = [0] * size

	def __getitem__(self, i):
		if not isinstance(i, int):
			return False
		chunkIndex = int(i / 64)
		if chunkIndex < 0 or len(self.vector) <= chunkIndex:
			return False
		chunk = self.vector[chunkIndex]
		index = int(i % 64)
		return ((1 << index & chunk) >> index) == 1

	def __setitem__(self, i, val):
		if not isinstance(i, int):
			return None
		if isinstance(val, bool):
			val = bool(val)
		chunkIndex = int(i / 64)
		if chunkIndex < 0 or len(self.vector) <= chunkIndex:
			self.vector.extend([0] * (1 + (chunkIndex - len(self.vector))))
		chunk = self.vector[chunkIndex]
		index = int(i % 64)
		if val:
			chunk |= (1 << index)
		else:
			chunk &= ~(1 << index)
		self.vector[chunkIndex] = chunk

	def __len__(self):
		return len(self.vector)*64    

	def print(self):
		for v in self.vector:
			for i in range(64):
				print(((1 << i & v) >> i), end="")
		print()


class MissingInt:

    def __init__(self, array):
        self.index = 0
        self.max = -sys.maxsize - 1
        self.array = array
        self.used = BitVector()
        for value in array:
            # mark value as used
            self.used[value] = 1
            # Save max
            if self.max < value:
                self.max = value
    def nextInt(self):
        while self.used[self.index] == 1:
            self.index += 1
        return self.index


def missing_int(array):
    used = BitVector()
    for value in array:
        used[value] = 1
    i = 0
    while used[i] == 1:
        i += 1
    return i



testcases = [
    ([4,1,2,100])
]

for t in testcases:
    m = MissingInt(t)
    print(m.nextInt())