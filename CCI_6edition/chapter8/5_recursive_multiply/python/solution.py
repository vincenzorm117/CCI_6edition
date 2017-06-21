#!/usr/local/bin/python3


def mult_rescursive(n,m):
	def mult(n,m):
		if n == 0 or m ==0:
			return 0
		if n == 1:
			return m
		if m == 1: 
			return n

		n1 = n2 = n >> 1
		if n & 1 == 1:
			n2 += 1

		m1 = m2 = m >> 1
		if m & 1 == 1:
			m2 += 1

		return mult(n1, m1) + mult(n1, m2) + mult(n2, m1) + mult(n2, m2)
	return mult(n,m)


def mult_rescursive_dp(n,m):
	D = { (0,0): 0, (0,1): 1, (1,0): 1, (1,1): 2 }
	def mult(n,m,D):
		if n == 0 or m == 0: return 0
		if n == 1: return m
		if m == 1: return n
		c = (n,m)
		if c in D: return D[c]

		n1 = n2 = n >> 1
		if n & 1 == 1:
			n2 += 1

		m1 = m2 = m >> 1
		if m & 1 == 1:
			m2 += 1

		val = mult(n1, m1, D) + mult(n1, m2, D) + mult(n2, m1, D) + mult(n2, m2, D)
		D[c] = val
		D[(c[1],c[0])] = val
		return val
	return mult(n,m, D)


def mult(N,M):
	q = [(N,M)]
	D = { (0,0): 0, (0,1): 1, (1,0): 1, (1,1): 1 }
	while 0 < len(q):
		n, m = q.pop()
		if (n,m) in D:
			continue
		if n == 0 or m == 0:
			D[(n,m)] = D[(m,n)] = 0
			continue
		elif n == 1:
			D[(n,m)] = D[(m,n)] = m
			continue
		elif m == 1:
			D[(n,m)] = D[(m,n)] = n
			continue

		n1 = n2 = n >> 1
		if n & 1 == 1:
			n2 += 1

		m1 = m2 = m >> 1
		if m & 1 == 1:
			m2 += 1

		val = [(n1,m1), (n1,m2), (n2,m1), (n2,m2)]
		checked = [val[0] in D, val[1] in D, val[2] in D, val[3] in D]
		if checked[0] and checked[1] and checked[2] and checked[3]:
			D[(n,m)] = D[(m,n)] = D[(n1,m1)] + D[(n1,m2)] + D[(n2,m1)] + D[(n2,m2)]
		else:
			q.append((n,m))
			for i in range(4):
				if not checked[i]:
					q.append(val[i])
	return D[(N,M)]


testcases = [
	(1,1),
	(1,10000),
	(3,65),
	(53,67),
	(57577575757575,1312423423423423423) # The performance killer
]

for t in testcases:
	sol = mult(t[0],t[1])
	ans = t[0]*t[1]
	print(ans, sol)
	assert(sol == ans)





