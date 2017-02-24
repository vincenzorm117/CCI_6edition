#!/usr/local/bin/python3


def urlify_better(s):
	return s.replace(' ', '%20')


def urlify(s):
	print(s)
	s = list(s) + ([' '] * (s.count(' ') * 2))
	L = len(s)
	last = L - 1

	# Find first non-white-space character from the right
	c = last
	while s[c] == ' ' and 0 <= c:
		c -= 1

	while 0 <= c:
		if s[c] == ' ':
			s[last] = '0'
			s[last - 1] = '2'
			s[last - 2] = '%'
			last -= 3
		else:
			s[last] = s[c]
			last -= 1
		c -= 1
	return ''.join(s)



print(urlify(input()))