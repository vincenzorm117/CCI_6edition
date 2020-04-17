#!/usr/local/bin/python3




def pondSizes(pond):
    if len(pond) <= 0:
        return None

    length = len(pond)
    width = len(pond[0])

    connectedWaterCells = set()
    connectedWaterCellSizes = []

    for y in range(len(pond)):
        for x in range(len(pond[0])):
            if (x,y) in connectedWaterCells:
                continue
            if pond[y][x] == 0:
                size = 0
                queue = [(x,y)]
                while 0 < len(queue):
                    x0,y0 = queue.pop(0)
                    # Check for valid unchecked space
                    if x0 < 0 or width <= x0 or y0 < 0 or length <= y0 or pond[y0][x0] != 0 or (x0,y0) in connectedWaterCells:
                        continue
                    # Mark space as visited
                    connectedWaterCells.add((x0,y0))
                    size += 1
                    queue += [(x0-1,y0),(x0-1,y0+1),(x0,y0+1),(x0+1,y0+1),(x0+1,y0),(x0-1,y0-1),(x0,y0-1),(x0+1,y0-1)]
                connectedWaterCellSizes.append(size)
    return connectedWaterCellSizes



def pondSizesAlternate(pond):
    if len(pond) <= 0:
        return None

    connectedWaterCells = set()
    connectedWaterCellSizes = []

    for y in range(len(pond)):
        for x in range(len(pond[0])):
            if pond[y][x] == 0:
                connectedWaterCells.add((x,y))

    while 0 < len(connectedWaterCells):
        connectedWaterCellSize = 0
        subPond = [connectedWaterCells.pop()]

        while 0 < len(subPond):
            connectedWaterCellSize += 1
            x, y = subPond.pop()

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    subPondCoordinate = (x + dx, y + dy)
                    if subPondCoordinate in connectedWaterCells:
                        connectedWaterCells.remove(subPondCoordinate)
                        subPond.append(subPondCoordinate)

        connectedWaterCellSizes.append(connectedWaterCellSize)
    return connectedWaterCellSizes





def printPond(pond):
    for y in pond:
        for x in y:
            print(x, end=" ")
        print()
    print()


testcases = [
    [
        [0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]
    ],
    [
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
    ],
    [
        [0,1,1,1,0],
        [1,0,1,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [0,1,1,1,0]
    ],
    [
        [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
    ],
    [
        [1,0,1,0,1,0,1],
        [0,1,0,1,0,1,0],
    ],
    [
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1],
    ],
    [
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ],
    [
        [1,1,1],
        [1,1,1],
        [1,1,0],
    ],
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
]


for pond in testcases:
    printPond(pond)
    print(pondSizes(pond))
    print(pondSizesAlternate(pond))
    print()