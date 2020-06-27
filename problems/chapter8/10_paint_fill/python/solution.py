#!/usr/local/bin/python3

def printGrid(grid):
    width, height = len(grid), len(grid[0])
    for x in range(width):
        for y in range(height):
            print(grid[x][y], end="")
        print()
    print()



def paintFill(grid, location, newColor):
    # Init variables
    width, height = len(grid), len(grid[0])
    x,y = location
    oldColor = grid[x][y]
    usedSpaces = set()

    stack = [(x,y)]
    while 0 < len(stack):
        x,y = stack.pop(0)
        grid[x][y] = newColor

        if 0 <= x - 1 and grid[x-1][y] == oldColor and (x-1,y) not in usedSpaces:
            stack.append((x-1,y))
            usedSpaces.add((x-1,y))
        if x+1 < width and grid[x+1][y] == oldColor and (x+1,y) not in usedSpaces:
            stack.append((x+1,y))
            usedSpaces.add((x+1,y))
        if 0 <= y - 1 and grid[x][y-1] == oldColor and (x,y-1) not in usedSpaces:
            stack.append((x,y-1))
            usedSpaces.add((x,y-1))
        if y+1 < height and grid[x][y+1] == oldColor and (x,y+1) not in usedSpaces:
            stack.append((x,y+1))
            usedSpaces.add((x,y+1))
    return grid


testcases = [
    (
    [[0,0,0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,0,1,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,1,1,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]], 
    (4,5), 
    4
    ),
    (
    [[0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]], 
    (4,5), 
    4
    ),
    (
    [[0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]], 
    (4,5), 
    4
    ),
    (
    [[1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]], 
    (0,0), 
    4
    ),
    (
    [[0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1]], 
    (8,11), 
    4
    ),
]

for G, loc, newColor in testcases:
    printGrid(G)
    paintFill(G,loc,newColor)
    printGrid(G)
    print('============\n')
