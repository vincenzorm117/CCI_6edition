

def twosCountBrute(num):
    count = 0
    for i in range(num+1):
        count += str(i).count('2')
    return count


# 2 Formulas
# For a power N of 10 we have:
# Sn = (9n + 1) * 10^(n-2) = 9 * sum(S[1], S[2], ..., S[n-1]) + 10^n
# So that we get:
# S1 = 1
# S2 = 19
# S3 = 280
# S4 = 3700
# S5 = 46000

A[1] = A[1e0] = 0
A[10] = A[1e1] = 1
A[100] = A[1e2] = 20
A[1000] = A[1e3] = 300
A[n] = n * 10^(n-1), for n s.t. some integer 0 <= m exists where 10^m = n




def twosCount(num):
    originalNum = num

    count = 0
    iteration = 0

    powerOf10_0 = 0
    powerOf10_1 = 1

    while num > 0:
        currDigit = int((num % (powerOf10_1*10)) / powerOf10_1)
        offset = num % (powerOf10_1*10)

        count += currDigit * iteration * powerOf10_0

        if currDigit == 2:
            count += (originalNum % powerOf10_1) + 1
        elif currDigit > 1:
            count += powerOf10_1

        iteration += 1
        num = num - offset
        powerOf10_0 = powerOf10_1
        powerOf10_1 *= 10

    return count



for num in range(10000):
    answer, solution = twosCountBrute(num), twosCount(num)
    assert(answer == solution)
