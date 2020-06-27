#!/usr/local/bin/python3




def centsRepresentationsRecursiveDP(n, denominations):
    def recurse(n, denominations, level, memoize):
        if n == 0: return 1
        if n < 0 or level < 0 or len(denominations) <= level: return 0
        if (n,level) in memoize:
            return memoize[(n,level)]
        currDenom = denominations[level]
        accumulator = 0
        for i in range(int(n/currDenom)+1):
            next_n = n - currDenom*i
            if 0 <= next_n:
                accumulator += recurse(next_n, denominations, level-1, memoize)
        memoize[(n,level)] = accumulator
        return accumulator
    memoize = {}
    return recurse(n, denominations, len(denominations) - 1, memoize)



def centsRepresentationsRecursive(n, denominations):
    def recurse(n, denominations, level):
        if n == 0: return 1
        if n < 0 or level < 0 or len(denominations) <= level: return 0
        currDenom = denominations[level]
        accumulator = 0
        for i in range(int(n/currDenom)+1):
            next_n = n - currDenom*i
            if 0 <= next_n:
                accumulator += recurse(next_n, denominations, level-1)
        return accumulator
    return recurse(n, denominations, len(denominations) - 1)



for s in range(1,40):
    print(s, centsRepresentationsRecursive(s, [1,5,10,25]), centsRepresentationsRecursiveDP(s, [1,5,10,25]))



# def centsRepresentationsIterative(n, denominations):
#     level = len(denominations) - 1
#     total = 0


# testcases = [
#     (11, [1,5,10,25]),
#     (1, [1,5,10,25]),
#     (5, [1,5,10,25]),
#     (10, [1,5,10,25]),
#     (25, [1,5,10,25]),
#     (0, [1,5,10,25]),
#     (24, [1,5,10,25]),
#     (13, [1,5,10,25]),
#     (31, [1,5,10,25]),
#     (100, [1,5,10,25]),
#     (123, [1,5,10,25]),
#     (500, [1,5,10,25]),
#     # (1023413, [1,5,10,25])
# ]

# for n, denominations in testcases:
#     sol1 = centsRepresentationsRecursive(n, denominations)
#     sol2 = centsRepresentationsRecursiveDP(n, denominations)
#     print(n, sol1, sol2)


# denominations = [25,10,5,1]
# for n in range(50):
#     start = time.time()
#     sol1 = representCents(n, denominations)
#     time1 = time.time() - start

#     start = time.time()
#     sol2 = representCentsLong(n, denominations)
#     time2 = time.time() - start

#     print(n, sol1, sol2, time1, time2)
#     assert(sol1 == sol2)

# for n, denominations in testcases:
#     print(n, representCents(n, denominations), representCentsLong(n, denominations))

# 1,5,10,25

# 0
# 1,5,10,25












# def centsRepresentationsRecursiveDP(n, denominations):
#     mem = [[0] * (n+1)] * len(denominations)
#     def recurse(n, denominations, level):
#         if n < 0 or level < 0 or len(denominations) <= level: return 0
#         if 0 < mem[level][n]: return mem[level][n]
#         if n == 0: return 1
#         currDenom = denominations[level]
#         accumulator = 0
#         for i in range(int(n/currDenom)+1):
#             next_n = n - currDenom*i
#             if 0 <= next_n:
#                 accumulator += recurse(next_n, denominations, level-1)
#         mem[level][n] = accumulator
#         return accumulator

#     temp = recurse(n, denominations, len(denominations) - 1)
#     # for i in range(len(denominations)):
#     #     print(mem[i])
#     return temp


