#!/usr/local/bin/python3

def check_permutation_with_sort(a,b, config_lower = True):
	aL, bL = len(a), len(b)
	if aL != bL:
		return False
	if config_lower:
		a, b = a.lower(), b.lower()
	a = sorted(a)
	b = sorted(b)

	for i, c in enumerate(a):
		if a[i] != b[i]:
			return False
	return True


def check_permutation(a,b, config_lower = True):
	aL, bL = len(a), len(b)
	if aL != bL:
		return False
	if config_lower:
		a, b = a.lower(), b.lower()
	used = [int(0)] * 256
	for c in a:
		used[ord(c)] += 1
	for c in b:
		used[ord(c)] -= 1
	for i in used:
		if i != 0:
			return False
	return True



print(check_permutation(input(),input()))

