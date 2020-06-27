from math import sqrt

########################################
# Missing one
def missing_one(array):
    L = len(array)+1
    sumWithAll = int(L * (L + 1) / 2)
    return sumWithAll - sum(array)



# for N in range(1,1000):
#     for missingItem in range(1,N+1):
#         array = [x+1 for x in list(range(N))]
#         array.remove(missingItem)
#         solution = missing_one(array)
#         assert(solution == missingItem)




########################################
# Missing Two


def missing_two(array):
    # Calculate the sum of the two missing items
    L = len(array)+2
    sumOfAll = int(L * (L + 1) / 2)
    sumOfNums = sum(array)
    sumOfTwo = sumOfAll - sumOfNums

    # Calculate the product of the two missing items
    productOfAll = 1
    for i in range(1,L+1):
        productOfAll *= i
    productOfNums = 1
    for num in array:
        productOfNums *= num
    productOfTwo = int(productOfAll / productOfNums)

    a = int((sumOfTwo + sqrt(sumOfTwo*sumOfTwo - 4*productOfTwo)) / 2)
    b = int((sumOfTwo - sqrt(sumOfTwo*sumOfTwo - 4*productOfTwo)) / 2)

    return (a,b) if a < b else (b,a)


def missing_two_book_solution(array):
    # Calculate the sum of the two missing items
    L = len(array)+2
    sumOfAll = int(L * (L + 1) / 2)
    sumOfNums = sum(array)
    sumOfTwo = sumOfAll - sumOfNums

    # Calculate the product of the two missing items
    sumOfAllSeqOfSquares = 0
    for i in range(1,L+1):
        sumOfAllSeqOfSquares += i*i
    sumOfNumsSeqOfSquares = 0
    for num in array:
        sumOfNumsSeqOfSquares += num*num
    sumOfTwoSeqOfSquares = sumOfAllSeqOfSquares - sumOfNumsSeqOfSquares

    a = int((sumOfTwo - sqrt(2 * sumOfTwoSeqOfSquares - sumOfTwo*sumOfTwo)) / 2)
    b = int((sumOfTwo + sqrt(2 * sumOfTwoSeqOfSquares - sumOfTwo*sumOfTwo)) / 2)

    return (a,b) if a < b else (b,a)





for N in range(2,500):
    print(N)
    for missingItem1 in range(1,N):
        for missingItem2 in range(missingItem1+1,N+1):

            array = [x+1 for x in list(range(N))]

            array.remove(missingItem1)
            array.remove(missingItem2)

            solution = missing_two_book_solution(array)

            assert(solution == (missingItem1, missingItem2))

