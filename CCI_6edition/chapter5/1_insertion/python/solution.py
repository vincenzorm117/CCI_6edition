#!/usr/local/bin/python3



def insertion(N, M, i, j):
	count = j - i + 1
	mask = ~(((1 << (count + 1)) - 1) << i)
	return (N & mask) | (M << i)


testcases = [
	(0b10000000000, 0b10011, 2, 6, 0b10001001100),
	(0b0, 0b1110001110, 0, 10, 0b1110001110),
	(2**32-1, 0b1010101, 25, 31, 0b10101011111111111111111111111111),
	(2**64-1, 0b1010101, 57, 63, 0b1010101111111111111111111111111111111111111111111111111111111111),
]

c = 0
for t in testcases:
	c += 1
	solution = insertion(t[0], t[1], t[2], t[3])
	print("Test #" + str(c))
	print(bin(solution))
	print(bin(t[4]))
	assert(solution == t[4])