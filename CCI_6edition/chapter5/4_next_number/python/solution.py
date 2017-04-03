#!/usr/local/bin/python3

BIT_SIZE = 32

def one_bit_count(N):
	count = 0
	while N != 0:
		N = (N & (N-1))
		count += 1
	return count



def next_smallest(x):
	if x == 0:
		return 0
	c = x
	c0 = 0
	c1 = 0

	while (c & 1) == 1 and 0 < c:
		c1 += 1
		c = c >> 1

	while (c & 1) == 0 and 0 < c:
		c0 += 1
		c = c >> 1

	b = c0 + c1
	if b == 0 and b == BIT_SIZE:
		return -1

	return x - (1 << (max(c0 - 1, 0))) - (1 << c1) + 1
	
def next_largest(x):
	if x == 0:
		return 0
	c = x
	c0 = 0
	c1 = 0

	while (c & 1) == 0 and 0 < c:
		c0 += 1
		c = c >> 1

	while (c & 1) == 1 and 0 < c:
		c1 += 1
		c = c >> 1

	b = c0 + c1
	if b == 0 and b == BIT_SIZE:
		return -1

	return x + (1 << c0) + (1 << (max(c1 - 1, 0))) - 1


testcases = [[
	(0b10011110000011, 0b10011101110000),
	(1, -1),
],[
	(0b111, 0b1011),
	(0b10011, 0b10101),
	(0b1001100, 0b1010001),
	(0b01, 0b10),
	(0, 0),
	(0b101, 0b110),
]]


print('Next smallest')
for t in testcases[0]:
	sol = next_smallest(t[0])
	print(bin(t[0]), bin(t[1]), bin(sol))
	assert(sol == t[1])

print('Next largest')
for t in testcases[1]:
	sol = next_largest(t[0])
	print(bin(t[0]), bin(t[1]), bin(sol))
	assert(sol == t[1])
