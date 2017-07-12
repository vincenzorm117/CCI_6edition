#!/usr/local/bin/python3



def permute_long(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	stack = [(l,0)]
	sols = set()
	while 0 < len(stack):
		c = stack.pop()
		if c[1] == L:
			sol = []
			for i in c[0]:
				sol.append(i)
			sols.add(tuple(sol))
		else:
			for i in range(c[1],L):
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
				stack.append((c[0][:], c[1]+1))
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
	return sols


def permute_recursive(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	mp = {}
	for c in l:
		if c not in mp:
			mp[c] = 0
		mp[c] += 1
	res = []
	keys = mp.keys()
	def foo(prefix, remaining):
		if( remaining == 0 ):
			res.append(prefix[:])
			return
		for c in keys:
			count = mp[c]
			if 0 < count:
				mp[c] = count - 1
				foo(prefix + [c], remaining - 1)
				mp[c] = count
	foo([], L)
	return res

def permute(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	mp = {}
	for c in l:
		if c not in mp:
			mp[c] = 0
		mp[c] += 1
	res = []
	keys = mp.keys()
	q = [([], L, mp)]
	while 0 < len(q):
		pre, k, mp = q.pop()
		if k == 0:
			res.append(pre)
			continue
		for c in keys:
			count = mp[c]
			if 0 < count:
				mp[c] = count - 1
				q.append((pre + [c], k - 1, mp.copy()))
				mp[c] = count
	return res



ts = [
	([], []),
	([1,2], [[1,2],[2,1]]),
	([1,2,3], [[1,2,3],[2,1,3],[1,3,2],[2,3,1],[3,1,2],[3,2,1]]),
	([1,1], [[1,1]]),
	([1,1,2], [[1,1,2],[1,2,1],[2,1,1]]),
	([1], [[1]])
]

for t in ts:
	q, a = t
	sol = permute(q)
	print(q)
	print(sol)
	correct = True
	if len(sol) == len(a):
		for x in a:
			if x not in sol:
				correct = False
				break
	else:
		correct = False
	assert(correct)

