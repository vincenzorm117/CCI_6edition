#!/usr/local/bin/python3


# Moves letters around (space efficient)
def permute(l):
	if not isinstance(l, (list)):
		return None
	if len(l) <= 0:
		return []
	L = len(l)
	stack = [(l,0)]
	sols = []
	while 0 < len(stack):
		c = stack.pop()
		if c[1] == L:
			sol = []
			for i in c[0]:
				sol.append(i)
			sols.append(sol)
		else:
			for i in range(c[1],L):
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
				stack.append((c[0][:], c[1]+1))
				c[0][c[1]], c[0][i] = c[0][i], c[0][c[1]]
	return sols

# Uses DP
def permute2(l):
	if not isinstance(l, (list)):
		return None
	L = len(l)
	if L <= 0:
		return []
	curr = [[]]
	for k in range(L):
		print(curr)
		nxt, K = [], k+1
		for p in range(K):
			for c in curr:
				nxt.append(c[0:p] + [l[k]] + c[p:K])
		curr = nxt
	return curr


ts = [
	([], []),
	([1], [[1]]),
	([1,2], [[1,2],[2,1]]),
	([1,2,3], [[1,2,3],[2,1,3],[1,3,2],[2,3,1],[3,1,2],[3,2,1]])
]


for t in ts:
	q, a = t
	sol = permute2(q)
	print(q)
	print(sol)
	correct = True
	if len(sol) == len(a):
		for x in sol:
			if x not in a:
				correct = False
				break
	else:
		correct = False

	print(correct)

