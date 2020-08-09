from random import randint

def hasFilledBorders(square, xStart, yStart, length):
    # Check top and bottom borders
    for x in range(xStart, xStart+length):
        if square[x][yStart] == 0 or square[x][yStart+length-1] == 0:
            return False
    # Check left and right borders
    for y in range(yStart, yStart+length):
        if square[xStart][y] == 0 or square[xStart+length-1][y] == 0:
            return False
    return True




def solution_brute_force(square):
    N = len(square)
    maxSubsquareLength = 0
    # Loop through all x and y coordinatees
    for x in range(N):
        for y in range(N):
            # Calculate the max possible length of the squares
            #  that can exist from x and y
            maxLength = min(N - y, N - x)
            # Iterate through all possible subsquare lengths
            for length in range(1, maxLength):
                if hasFilledBorders(square, x, y, length):
                    # Compare new subsquare with current max
                    if length > maxSubsquareLength:
                        maxSubsquareLength = length
    return maxSubsquareLength


class NeighborCountNode:
    left=0
    right=0
    top=0
    bottom=0

    def __repr__(self):
        return str((self.left,self.right,self.top,self.bottom))


def mapCellNeighborCounts(square):
    N = len(square)
    counts = [[NeighborCountNode() for _ in range(N)] for _ in range(N)]

    # Calculate left and right values
    for y in range(N):
        totalCount = 0
        for x in range(N):
            totalCount += (1 if square[y][x] else 0)
        leftCount = 0

        for x in range(N):
            counts[y][x].left = leftCount
            counts[y][x].right = totalCount - leftCount - (1 if square[y][x] == 1 else 0)

            if square[y][x] == 1:
                leftCount += 1

    # Calculate top and bottom values
    for x in range(N):
        totalCount = 0
        for y in range(N):
            totalCount += (1 if square[y][x] else 0)
        topCount = 0

        for y in range(N):
            counts[y][x].top = topCount
            counts[y][x].bottom = totalCount - topCount - (1 if square[y][x] == 1 else 0)

            if square[y][x] == 1:
                topCount += 1

    return counts


# neighborCounts: square([top, right, bottom, left])
def hasFilledBordersWithCounts(square, neighborCounts, x,y, length):
    N = len(square)
    # Check corner cells
    if square[y][x] != 1 or square[y][x+length-1] != 1 or square[y+length-1][x] != 1 or square[y+length-1][x+length-1] != 1:
        return False
    # Check top
    x0TotalCount = neighborCounts[y][N-1].left + (1 if square[y][N-1] == 1 else 0)
    if (neighborCounts[y][x+length-1].left + neighborCounts[y][x].right + 2) - x0TotalCount != length:
        return False
    # Check bottom
    x1TotalCount = neighborCounts[y+length-1][N-1].left + (1 if square[y+length-1][N-1] == 1 else 0)
    if (neighborCounts[y+length-1][x+length-1].left + neighborCounts[y+length-1][x].right + 2) - x1TotalCount != length:
        return False
    # Check left
    y0TotalCount = neighborCounts[N-1][x].top + (1 if square[N-1][x] == 1 else 0)
    if (neighborCounts[y+length-1][x].top + neighborCounts[y][x].bottom + 2) - y0TotalCount != length:
        return False
    # Check right
    y1TotalCount = neighborCounts[N-1][x+length-1].top + (1 if square[N-1][x+length-1] == 1 else 0)
    if (neighborCounts[y+length-1][x+length-1].top + neighborCounts[y][x+length-1].bottom + 2) - y1TotalCount != length:
        return False
    # Return True since all borders are filled
    return True


def solution_optimized(square):
    N = len(square)
    # neighborCounts: square([top, right, bottom, left])
    neighborCounts = mapCellNeighborCounts(square)
    maxSubsquareLength = 0
    # Loop through all x and y coordinatees
    for x in range(N):
        for y in range(N):
            # Calculate the max possible length of the squares
            #  that can exist from x and y
            maxLength = min(N - y, N - x)
            # Iterate through all possible subsquare lengths
            for length in range(1, maxLength):
                if hasFilledBordersWithCounts(square, neighborCounts, x, y, length):
                    # Compare new subsquare with current max
                    if length > maxSubsquareLength:
                        maxSubsquareLength = length
    return maxSubsquareLength



def generateTestcases(count, maxSize):
    for _ in range(count):
        N = randint(1,maxSize)
        square = [[0 for _ in range(N)] for _ in range(N)]
        # Pepper some 1s in random spots
        for _ in range(randint(0, N*N)):
            square[randint(0, N-1)][randint(0, N-1)] = 1
        # Generate border start and end
        xStart,yStart = randint(0, N-1), randint(0, N-1)
        length = randint(1, min(N - xStart, N - yStart))
        # Create top and bottom borders
        for x in range(xStart, xStart+length):
            square[x][yStart] = 1
            square[x][yStart+length-1] = 1
        # Create left and right borders
        for y in range(yStart, yStart+length):
            square[xStart][y] = 1
            square[xStart+length-1][y] = 1
        yield square



def printSquare(square):
    N = len(square)
    print(N)

    for x in range(N):
        for y in range(N):
            print('X' if square[y][x] == 1 else ' ', end='')
        print()
    print()

for square in generateTestcases(10000, 100):
    sol1 = solution_brute_force(square)
    sol2 = solution_optimized(square)
    printSquare(square)
    print(sol1, sol2)
    assert(sol1 == sol2)
