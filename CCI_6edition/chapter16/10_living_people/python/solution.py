#!/usr/local/bin/python3

from random import randint

def livingPeopleBrute2(people):
    maxPopSize = 0
    for i in range(1900, 2001):
        popSize = 0
        for start,end in people:
            if start <= i and i <= end:
                popSize += 1
        if maxPopSize < popSize:
            maxPopSize = popSize
    return maxPopSize



def livingPeopleBrute1(people):
    population = [0] * 101
    for start,end in people:
        for i in range(start,end+1):
            population[i-1900] += 1

    maxPopulationSize = 0
    maxPopulationYear = 0

    for year in range(len(population)):
        populationCount = population[year]
        if maxPopulationSize < populationCount:
            maxPopulationSize = populationCount
            maxPopulationYear = year

    return maxPopulationYear + 1900



def livingPeople(people):
    if len(people) <= 0:
        return None

    populationSizeChanges = [0] * 102

    for start,end in people:
        populationSizeChanges[start-1900] += 1
        populationSizeChanges[end-1900+1] -= 1

    maxPopulationYear = 0
    maxPopulationSize = 0
    populationSize = 0

    for year in range(len(populationSizeChanges)-1):
        change = populationSizeChanges[year]
        populationSize += change

        if maxPopulationSize < populationSize:
            maxPopulationSize = populationSize
            maxPopulationYear = year

    return maxPopulationYear + 1900






def graphAges(people):
    for start,end in people:
        for i in range(1900,2001):
            if start <= i and i <= end:
                print('#', end="")
            else:
                print('=', end="")
        print()



# testcases = [
#     [
#         (1920, 1960),
#         (1910, 1959),
#         (1956, 2000),
#         (1989, 1999),
#         (1910, 1913),
#         (1901, 1925),
#         (1940, 1964)
#     ],
#     [
#         (1900, 1910),
#         (1900, 1909),
#         (1900, 1908),
#         (1900, 1907),
#         (1900, 1906),
#         (1900, 1905),
#         (1900, 1904),
#         (1900, 1903),
#         (1900, 1902),
#         (1900, 1901),
#         (1911, 1920),
#         (1911, 1919),
#         (1911, 1918),
#         (1911, 1917),
#         (1911, 1916),
#         (1911, 1915),
#         (1911, 1914),
#         (1911, 1913),
#         (1911, 1912)
#     ],
#     [
#         (1900,1900),
#         (1901,1901),
#         (1902,1902),
#         (1903,1903),
#     ]
# ]

# for people in testcases:
#     print(people)
#     # people.sort(key=lambda x : x[1])
#     people.sort()
#     graphAges(people)

#     solution = livingPeople(people)
#     answer = livingPeopleBrute1(people)
#     print('SOLUTION: %s ANSWER: %s' % (solution, answer))
#     assert(answer == solution)

def generateTestCase():
    count = randint(1,10)
    testcase = []

    while 0 < count:
        start = randint(1900,2000)
        end = randint(start,2000)
        testcase.append((start, end))
        count -= 1
    return testcase


for N in range(1,100001):
    testcase = generateTestCase()
    print('TestCase[%s] Count: %s' % (N, len(testcase)))
    print(testcase)
    graphAges(testcase)

    solution = livingPeople(testcase)
    answer = livingPeopleBrute1(testcase)
    print('SOLUTION: %s ANSWER: %s' % (solution, answer))
    assert(answer == solution)
