#!/usr/local/bin/python3




# def combinations(bag):
	
def power_set_recursive(alpha):
	powerSet = []
	def nCk_recursive(bag, k, pos, str):
		if k <= 0:
			powerSet.append(str)
			return
		for i in range(pos, len(bag)):
			nCk_recursive(bag, k-1, i+1, str+bag[i])
	for i in range(0, len(alpha)):
		nCk_recursive(alpha, i, 0, '')
	return powerSet

# print(power_set_recursive(['a','b','c','d']))


def nCk(bag, k):
	L = len(bag)
	if k < 0 or L < k:
		return None
	chosen = []
	q = [([], k, 0)]
	while 0 < len(q):
		c = q.pop()
		if c[1] == 0:
			chosen.append(c[0])
			continue
		for i in range(c[2], L):
			N = c[0][:]
			N.append(bag[i])
			q.append((N, c[1]-1, i+1))
	return chosen


def powerset(bag):
	L = len(bag)
	chosen = []
	for k in range(L+1):
		q = [([], k, 0)]
		while 0 < len(q):
			c = q.pop()
			if c[1] == 0:
				chosen.append(c[0])
				continue
			for i in range(c[2], L):
				N = c[0][:]
				N.append(bag[i])
				q.append((N, c[1]-1, i+1))
	return chosen


for l in range(5):
	print(powerset(list(range(l))))

