#!/usr/local/bin/python3




def pondSizes(pond):
    if len(pond) <= 0:
        return None

    length = len(pond)
    width = len(pond[0])

    connectedWaterCells = set()
    connectedWaterCellSizes = []
    stack = []
    for y in range(len(pond)):
        for x in range(len(pond[0])):
            if (x,y) in connectedWaterCells:
                continue
            if pond[y][x] == 0:
                size = 0
                stack.append((x,y))
                while 0 < len(stack):
                    x0,y0 = stack.pop(0)
                    # Check for valid unchecked space
                    if x0 < 0 or width <= x0 or y0 < 0 or length <= y0 or pond[y0][x0] != 0 or (x0,y0) in connectedWaterCells:
                        continue
                    # Mark space as visited
                    connectedWaterCells.add((x0,y0))
                    size += 1
                    stack += [(x0-1,y0),(x0-1,y0+1),(x0,y0+1),(x0+1,y0+1),(x0+1,y0),(x0-1,y0-1),(x0,y0-1),(x0+1,y0-1)]
                connectedWaterCellSizes.append(size)
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
]


for pond in testcases:
    printPond(pond)
    print(pondSizes(pond))