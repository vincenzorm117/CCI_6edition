#!/usr/local/bin/python3


def one_away(a,b):
	al, bl = len(a), len(b)
	if (al - 1) == bl : 
		large = a
		small = b
		L = bl
	elif al == (bl - 1):
		small = a
		large = b
		L = al
	else:
		return False

	offset = 0
	i = 0
	while(i < L):
		if small[i] != large[i+offset]:
			offset += 1
			if 2 <= offset:
				return False
		else:
			i += 1
	return True


def one_or_zero_away(a,b):
	al, bl = len(a), len(b)
	if al == bl:
		different = False
		for i in range(al):
			if a[i] != b[i]:
				if different:
					return False
				else:
					different = True
		return True
	elif abs(al - bl) == 1:
		return one_away(a,b)
	else:
		return False


print(one_or_zero_away(input(),input()))


