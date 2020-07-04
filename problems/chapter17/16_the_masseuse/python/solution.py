from random import randint

#######################################################
# Brute Force solutions
def the_masseuse_bruteForce_recursive(appointments):
    def recur(appointments, index, currMax):
        if index >= len(appointments):
            return currMax

        return max(
            recur(appointments, index+1, currMax),
            recur(appointments, index+2, currMax + appointments[index])
        )
    return recur(appointments, 0, 0)


def the_masseuse_bruteForce_iterative(appointments):
    globalMax = 0
    stack = [(0,0)]
    while len(stack) > 0:
        index, currMax = stack.pop()
        if index >= len(appointments):
            if globalMax < currMax:
                globalMax = currMax
            continue
        stack.append((index+1, currMax))
        stack.append((index+2, currMax + appointments[index]))
    return globalMax



#######################################################
# Memoized solutions

def the_masseuse_recursive(appointments):
    def recur(index):
        nonlocal appointments, memo
        if index >= len(appointments):
            return 0

        if index in memo:
            return memo[index]

        memo[index] = max(
            recur(index+1),
            recur(index+2) + appointments[index]
        )
        return memo[index]
    memo = {}
    return recur(0)


def the_masseuse_iterative(appointments):
    if len(appointments) < 3:
        return max(appointments)

    memo = {}
    memo[len(appointments)-1] = appointments[len(appointments)-1]
    memo[len(appointments)-2] = max(appointments[len(appointments)-2], appointments[len(appointments)-1])

    for i in range(len(appointments)-3, -1, -1):
        memo[i] = max(
            appointments[i] + memo[i+2],
            memo[i+1]
        )
    return memo[0]


def the_masseuse_iterative_optimized(appointments):
    if len(appointments) < 3:
        return max(appointments)

    memo0 = 0
    memo1 = max(appointments[len(appointments)-2], appointments[len(appointments)-1])
    memo2 = appointments[len(appointments)-1]

    for i in range(len(appointments)-3, -1, -1):
        memo0 = max(
            appointments[i] + memo2,
            memo1
        )
        memo2 = memo1
        memo1 = memo0
    return memo1



#######################################################
# Used for testing
def permute_no_dups(l):
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

#######################################################
# Testing
testcases = [
    ([30,70], 70),
    ([30,15,60,75,45,15,15,45], 180),
    ([100,15,100], 200),
    ([10,20,30], 200),
]


for testcase, answer in testcases:
    permutations = permute_no_dups(testcase)
    for permutation in permutations:
        solutions = (
            the_masseuse_bruteForce_iterative(permutation),
            the_masseuse_recursive(permutation),
            the_masseuse_iterative_optimized(permutation)
        )
        assert(solutions[0] == solutions[2])

for i in range(1,10):
    for _ in range(10000):
        array = [randint(5,100) for j in range(i)]
        answer = the_masseuse_bruteForce_iterative(array)
        solution1 = the_masseuse_recursive(array)
        solution2 = the_masseuse_iterative_optimized(array)
        if solution1 != answer or solution2 != answer:
            print(answer, solution1, solution2, array)
        assert(solution1 == answer and solution2 == answer)

