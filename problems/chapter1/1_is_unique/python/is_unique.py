#!/usr/local/bin/python3


def all_unique_chars_with_boolean_map(str):
	L = len(str)
	if 256 < L:
		return False
	str = str.lower()
	used = [False] * 256
	for c in str:
		if used[ord(c)]:
			return False
		used[ord(c)] = True
	return True



print(all_unique_chars_with_boolean_map(input()))

