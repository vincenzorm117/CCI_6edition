


def pairs_with_sum__SORTED(array, sum):
    if len(array) <= 0 or type(sum) != int:
        return None

    pairs = []
    array.sort()

    start, end = 0, len(array)-1
    while start < end:
        testSum = array[start] + array[end]
        if testSum == sum:
            pairs.append((array[start], array[end]))
            start += 1
            end -= 1
        else:
            if testSum < sum:
                start += 1
            else:
                end -= 1
    return pairs



def pairs_with_sum(array, sum):
    if len(array) <= 0 or type(sum) != int:
        return None

    pairs = []
    complementFrequency = {}

    for num in array:
        complement = sum - num

        if num in complementFrequency and 0 < complementFrequency[num]:
            pairs.append((complement, num))
            complementFrequency[num] -= 1
        else:
            if complement in complementFrequency:
                complementFrequency[complement] += 1
            else:
                complementFrequency[complement] = 1

    return pairs

# Tescases(1)
testcases = [
    ([1, 5, 7, 1], [4, 6]),
    ([1, 1, 1, 1], [4, 2]),
]

for nums, sums in testcases:
    print('\nTestcase:')
    print(nums)
    for sum in sums:
        print('Sum(%s)' % (sum))
        print(pairs_with_sum(nums, sum))
        print(pairs_with_sum__SORTED(nums, sum))


# Tescases(2)
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


def verifyAnswer(array, pairs):
    freq = {}
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, complement in pairs:
        if num in freq and complement in freq:
            freq[num] -= 1
            freq[complement] -= 1
            if freq[num] < 0 or freq[complement] < 0:
                return False
        else:
            return False
    return True


A = [1,1,2,2,3,3,4,4,5,5]

for i in range(1, len(A)+1):
    for sumValue in range(max(A)*2):
        for array in nCk(A, i):
            pairs1 = pairs_with_sum__SORTED(array, sumValue)
            pairs2 = pairs_with_sum(array, sumValue)
            print(array, sumValue)
            assert(verifyAnswer(array, pairs1))
            assert(verifyAnswer(array, pairs2))