#!/usr/local/bin/python3

#  ______   ___
# |      |   |
# |      |   | This length is 2 * radius
# |______|  _|_
#

class Square:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return str((self.x, self.y))


class Line:
    def __init__(self, start, end):
        if not isinstance(start, tuple) or not isinstance(end, tuple) or len(start) != 2 or len(end) != 2:
            raise Exception('Invalid Arguments. Arguments must be 2 tuples, each of size 2.')
        self.start = start
        self.end = end

    def __eq__(self, other):
        if not isinstance(other, Line):
            return False
        return (self.start == other.start and self.end == other.end) or (self.start == other.end and self.end == other.start)

    def __str__(self):
        return str(self.start) + ' ' + str(self.end)

# A = squareA
# B = squareB
def getBisectineLineSegment(A, B):

    # Same x,y coordinates
    if A.x == B.x and A.y == B.y:
        radius = B.radius if A.radius < B.radius else A.radius
        lineStart = (A.x - radius, A.y)
        lineEnd = (A.x + radius, A.y)
        return Line(lineStart, lineEnd)

    # Same x coordinate
    if A.x == B.x:
        top, bottom = (B, A) if A.y < B.y else (A, B)
        lineStart = (bottom.x, bottom.y - bottom.radius)
        lineEnd = (top.x, top.y + top.radius)
        return Line(lineStart, lineEnd)

    # Same y coordinate
    if A.y == B.y:
        right, left = (B, A) if A.x < B.x else (A, B)
        lineStart = (left.x - left.radius, left.y)
        lineEnd = (right.x + right.radius, right.y)
        return Line(lineStart, lineEnd)

    dx = B.x - A.x
    dy = B.y - A.y

    # Line Slope = -1
    if dx == dy and dx * dy < 0:
        topLeft, bottomRight = (B, A) if B.x < A.x else (A, B)
        lineStart = (topLeft.x - topLeft.radius, topLeft.y + topLeft.radius)
        lineEnd = (bottomRight.x + bottomRight.radius, bottomRight.y - bottomRight.radius)
        return Line(lineStart, lineEnd)

    # Line Slope = 1
    if dx == dy and not (dx * dy < 0):
        bottomLeft, topRight = (B, A) if B.x < A.x else (A, B)
        lineStart = (bottomLeft.x - bottomLeft.radius, bottomLeft.y - bottomLeft.radius)
        lineEnd = (topRight.x + topRight.radius, topRight.y + topRight.radius)
        return Line(lineStart, lineEnd)

    # Line Slope between -1 and -Inf
    if dx < dy and dx * dy < 0:
        topLeft, bottomRight = (B, A) if B.x < A.x else (A, B)
        lineStart = (topLeft.x - topLeft.radius * dx / dy, topLeft.y + topLeft.radius)
        lineEnd = (bottomRight.x + bottomRight.radius * dx / dy, bottomRight.y - bottomRight.radius)
        return Line(lineStart, lineEnd)

    # Line Slope between -1 and 0
    if dx > dy and dx * dy < 0:
        topLeft, bottomRight = (B, A) if B.x < A.x else (A, B)
        lineStart = (topLeft.x - topLeft.radius, topLeft.y + topLeft.radius * dy / dx)
        lineEnd = (bottomRight.x + bottomRight.radius, bottomRight.y - bottomRight.radius * dy / dx)
        return Line(lineStart, lineEnd)

    # Line Slope between 1 and Inf
    if dx < dy and not (dx * dy < 0):
        bottomLeft, topRight = (B, A) if B.x < A.x else (A, B)
        lineStart = (bottomLeft.x - bottomLeft.radius * dx / dy, bottomLeft.y - bottomLeft.radius)
        lineEnd = (topRight.x + topRight.radius * dx / dy, topRight.y + topRight.radius)
        return Line(lineStart, lineEnd)


    # Line Slope between 1 and 0
    if dx > dy and not (dx * dy < 0):
        bottomLeft, topRight = (B, A) if B.x < A.x else (A, B)
        lineStart = (bottomLeft.x - bottomLeft.radius, bottomLeft.y - bottomLeft.radius * dy / dx)
        lineEnd = (topRight.x + topRight.radius, topRight.y + topRight.radius * dy / dx)
        return Line(lineStart, lineEnd)



# for x0 in range(10):
#     for y0 in range(10):
#         A = Square(x0, y0, 2)
#         for x1 in range(10):
#             for y1 in range(10):
#                 B = Square(x1, y1, 2)
#                 print(A, end=' ')
#                 print(B, end=' => ')
#                 print(getBisectineLineSegment(A,B))



testcases = [
    ( Square(0,0,1), Square(0,0,1), Line((-1,0), (1,0)) ),
    ( Square(0,0,1), Square(5,5,1), Line((-1,-1), (6,6)) ),
]

for A, B, line in testcases:
    assert(getBisectineLineSegment(A,B) == line)