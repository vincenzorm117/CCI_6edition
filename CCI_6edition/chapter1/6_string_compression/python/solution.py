#!/usr/local/bin/python3

	

def string_compression_with_look_ahead(s):
	def compressed_length(s):
		count = 0
		curr = s[0]
		L = 0

		for c in s:
			if curr != c:
				L += 1 + len(str(count))
				curr = c
				count = 0
			count += 1
		L += 1 + len(str(count))
		return L

	L = len(s)
	if L <= 0:
		return s

	L2 = compressed_length(s)
	if L <= L2:
		return s

	count = 0
	curr = s[0]
	buff = ''

	for c in s:
		if curr != c:
			buff += str(curr) + str(count)
			curr = c
			count = 0
		count += 1
	buff += str(curr) + str(count)

	if len(buff) < L:
		return buff
	return s



def string_compression(s):
	L = len(s)
	if L <= 0:
		return L

	count = 0
	curr = s[0]
	buff = ''

	for c in s:
		if curr != c:
			buff += str(curr) + str(count)
			curr = c
			count = 0
		count += 1
	buff += str(curr) + str(count)

	if len(buff) < L:
		return buff
	return s

while True:
	print(string_compression_with_look_ahead(input()))


