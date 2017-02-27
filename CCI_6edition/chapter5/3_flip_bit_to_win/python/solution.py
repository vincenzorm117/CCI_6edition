#!/usr/local/bin/python3

# First solution
def flip_bit_to_win0(x):
	if x == 2^33 - 1:
		return 32
	elif x == 0:
		return 1
	def find_longest_length(x):
		longest = 0
		i = 0
		while i < 32:
			if (1 << i) & x != 0:
				count = 0
				j = i
				while (1 << j) & x != 0:
					count += 1
					j += 1
				if longest < count:
					longest = count
				i = j
			i += 1
		return longest
	ac = 0
	for i in range(32):
		if (1 << i) & x == 0:
			l = find_longest_length((1 << i) | x)
			if ac < l:
				ac = l
	return ac


def flip_bit_to_win(x):
	if x == 2**32 - 1:
		return 32

	currLength = 0
	previousLength = 0
	maxLength = 1
	while 0 < x:
		if x & 1 == 1:
			currLength += 1
		else:
			previousLength = 0 if (x & 2) == 0 else currLength
			currLength = 0
		maxLength = max(previousLength + currLength + 1, maxLength)
		x = x >> 1
	return maxLength

testcases = [
	(1775, 8),
	(0b1110111100011, 8),
	(0, 1),
	(16,2),
	(0b0011100,4),
]

def test(x):
	L = flip_bit_to_win(x[0])
	print(x[0], L)
	assert(L == x[1])

for t in testcases:
	test(t)

