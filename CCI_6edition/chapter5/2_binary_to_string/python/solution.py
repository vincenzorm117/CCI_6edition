#!/usr/local/bin/python3

# Number is between 0 and 1
 
def binary_to_string(x):
	binary = [0] * 32
	mantissaIndex = 0
	c = x
	while c != 1 and mantissaIndex < 32:
		c *= 2
		if 1 < c:
			binary[mantissaIndex] = 1
			c -= 1
		mantissaIndex += 1
	if c != 1:
		return "ERROR"
	else:
		binary[mantissaIndex] = 1
	return '.'+''.join(str(x) for x in binary)

testcases = [
	0.15625
] + [1/2**x for x in range(32)]
for t in testcases:
	print(binary_to_string(t))