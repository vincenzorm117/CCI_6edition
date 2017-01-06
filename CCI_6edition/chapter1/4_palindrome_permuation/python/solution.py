#!/usr/local/bin/python3

def palindrome_permutation(str):
	freq = [int(0)] * 256
	odd_occurrence = 0

	for c in str:
		freq[ord(c)] += 1
		if freq[ord(c)] % 2 == 1:
			odd_occurrence += 1
		else:
			odd_occurrence -= 1
	return odd_occurrence <= 1


def palindrome_permutation_with_dictionary(str):
	freq = {}
	odd_occurrence = 0

	for c in str:
		if not c in freq:
			freq[c] = 0
		freq[c] += 1
		if freq[c] % 2 == 1:
			odd_occurrence += 1
		else:
			odd_occurrence -= 1
	return odd_occurrence <= 1


def palindrome_permutation_with_bitvector(str):
	str = str.lower()
	def toggle(bitvector, index):
		mask = 1 << index
		if (bitvector & mask) == 0:
			bitvector |= mask
		else:
			bitvector &= ~mask
		return bitvector

	used = 0
	odd_occurrence = 0
	alphaOffset = ord('a')
	for c in str:
		used = toggle(used,ord(c) - alphaOffset)

	for i in range(32):
		disp = 0 if (used & (1 << i)) == 0 else 1
		print(disp, end="")
	print()

	return used == 0 or (used & (used - 1)) == 0


print(palindrome_permutation_with_bitvector(input()))

