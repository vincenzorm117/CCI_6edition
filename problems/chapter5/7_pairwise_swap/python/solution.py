#!/usr/local/bin/python3

# Copy bin(10) and bin(01) with bin(11) (or int(3))

# My solution
def pairwise_swap2(N):
	c = N
	buff = i = 0
	while 0 < c:
		curr = c & 3
		if curr == 1 or curr == 2:
			buff = buff | 3 << i
		i += 2
		c >>= 2
	return N ^ buff

def pairwise_swap(N):
	return ( ((N & 0xaaaaaaaaaaaaaaaaa) >> 1)  | ((N & 0x55555555555555555) << 1))

testcases = [
	0b111111111111,
	0b000000000000,
	0b111011101001,
	0b101010101010,
	0b000001000000,
]
for t in testcases:
	print(bin(t))
	print(bin(pairwise_swap(t)))
	print()

