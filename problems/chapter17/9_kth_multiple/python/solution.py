

def swap(array, index0, index1):
    array[index0], array[index1] = array[index1], array[index0]


def partition(array, low, high):
    if low >= high:
        return high
    # Partition all elements in range except pivot
    pivot = array[low]
    left = low+1
    right = high
    while left < right:
        if array[left] < pivot:
            left += 1
        else:
            swap(array, left, right)
            right -= 1
    # Move pivot into place
    if array[left] < pivot:
        swap(array, low, left)
        return left
    else:
        swap(array, low, left-1)
        return left-1


def h_smallest_k(array, K):
    if K == 0:
        return None
    stack = [(0, len(array)-1)]
    while len(stack) > 0:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = partition(array, low, high)
        if pivot > K:
            stack.append((low, pivot-1))
        else:
            stack.append((pivot+1, high))
    return array[0:K]


# Solution

def kth_multiple(K):
    if K == 0:
        return 0

    array = []

    q3 = [1] # Queue for nums multiplied by 3 only
    q5 = []  # Queue for nums multiplied by 5
    q7 = []  # Queue for nums multiplied by 7


    for _ in range(K+1):
        num = q3.pop(0)
        array.append(num)
        q3.append(num*3)
        q5.append(num*5)
        q7.append(num*7)

    for _ in range(2*(K+1)):
        num = q5.pop(0)
        array.append(num)
        q5.append(num*5)
        q7.append(num*7)

    for _ in range(3*(K+1)):
        num = q7.pop(0)
        array.append(num)
        q7.append(num*7)

    return max(h_smallest_k(array, K))



for K in range(1000):
    print(K, kth_multiple(K))