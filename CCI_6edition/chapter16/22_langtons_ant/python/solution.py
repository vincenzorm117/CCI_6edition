


def printMoves(k):

    blackSpaces = set()
    location = (0,0)
    direction = 0
    deltas = [(+1, 0), (0, -1), (-1, 0), (0, +1)]

    minX, minY, maxX, maxY = 0, 0, 0, 0


    for _ in range(k):
        x,y = location

        if location in blackSpaces:
            blackSpaces.remove(location)
            direction = ((direction - 1) + 4) % 4
        else:
            blackSpaces.add(location)
            direction = ((direction + 1) + 4) % 4

        dx, dy = deltas[direction]

        location = (x+dx, y+dy)
        minX = min(location[0], minX)
        minY = min(location[1], minY)
        maxX = max(location[0], maxX)
        maxY = max(location[1], maxY)

    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            space = 'X' if (x,y) in blackSpaces else '_'
            print(space, end='')
        print()

printMoves(15000)

# for k in range(10000):
#     printMoves(k)
#     print()