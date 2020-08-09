from math import inf
from random import randint



def submatrixSum(matrix, x0, y0, x1, y1):
    subSum = 0
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            subSum += matrix[y][x]
    return subSum

def solution_brute_force(matrix):
    N = len(matrix)
    if N == 0:
        return 0

    subMatrixMaxSum = -inf
    subMatrixMaxVector = None

    for x0 in range(N):
        for y0 in range(N):
            for x1 in range(x0,N):
                for y1 in range(y0,N):
                    currSum = submatrixSum(matrix, x0, y0, x1, y1)
                    if currSum > subMatrixMaxSum:
                        subMatrixMaxSum = currSum
                        subMatrixMaxVector = (x0,x1,y0,y1)
    return (subMatrixMaxSum, subMatrixMaxVector)


def generateSumsMatrix(matrix):
    N = len(matrix)
    sums = [[0 for _ in range(N)] for _ in range(N)]
    # Calculate top and left border sums
    sums[0][0] = matrix[0][0]
    for i in range(1,N):
        sums[i][0] = sums[i-1][0] + matrix[i][0]
        sums[0][i] = sums[0][i-1] + matrix[0][i]
    # Calculate other sums
    for x in range(1,N):
        for y in range(1,N):
            sums[y][x] = sums[y-1][x] + sums[y][x-1] - sums[y-1][x-1] + matrix[y][x]
    return sums



def solution_brute_force_optimized_sum(matrix):
    N = len(matrix)

    sums = generateSumsMatrix(matrix)
    subMatrixMaxSum = -inf

    for x0 in range(N):
        for y0 in range(N):
            for x1 in range(x0,N):
                for y1 in range(y0,N):
                    currSum = sums[y1][x1]
                    if x0 > 0:
                        currSum -= sums[y1][x0-1]
                    if y0 > 0:
                        currSum -= sums[y0-1][x1]
                    if x0 > 0 and y0 > 0:
                        currSum += sums[y0-1][x0-1]

                    if currSum > subMatrixMaxSum:
                        subMatrixMaxSum = currSum
    return subMatrixMaxSum




def solution_optimized(matrix):
    N = len(matrix)

    sums = generateSumsMatrix(matrix)
    subMatrixMaxSum = -inf
    printSquare(sums)

    for x0 in range(N):
        for x1 in range(x0,N):
            maxSum = -inf
            currSum = 0
            for y in range(N):
                currValue = sums[y][x1]
                if y > 0:
                    currValue -= sums[y-1][x1]
                if x0 > 0:
                    currValue -= sums[y][x0-1]
                if y > 0 and x0 > 0:
                    currValue += sums[y-1][x0-1]

                currSum += currValue

                if currSum > maxSum:
                    maxSum = currSum
                if currSum < 0:
                    currSum = 0

            if maxSum > subMatrixMaxSum:
                subMatrixMaxSum = maxSum

    return subMatrixMaxSum



def generateTestcases(count, maxSize, start, end):
    for _ in range(count):
        N = randint(1,maxSize)
        matrix = [[randint(start, end) for _ in range(N)] for _ in range(N)]
        yield matrix


def printSquare(matrix):
    N = len(matrix)
    for x in range(N):
        for y in range(N):
            print('%4s'  % (matrix[x][y]), end=' ')
        print()
    print()

for matrix in generateTestcases(10000000, 50, -20, 20):
    print('======================')
    printSquare(matrix)
    sol1, sol1Vector = solution_brute_force(matrix)
    # sol2 = solution_brute_force_optimized_sum(matrix)
    sol2 = solution_optimized(matrix)
    print(sol1Vector)
    print(sol1, sol2)
    assert(sol1 == sol2)
