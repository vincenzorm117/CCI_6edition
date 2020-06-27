#!/usr/local/bin/python3



def gcd(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception('Arguments not ints')
    if a > b:
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    return b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return (self.y - other.y, self.x - other.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))


class Line:
    def __init__(self, pointA, pointB):
        if not isinstance(pointA, Point) or not isinstance(pointB, Point):
            raise Exception("Invalid Arguments. Make sure they are two arguments of type Point.")

        if pointA == pointB:
            raise Exception("Invalid Arguments. Make sure the two points provided are different.")

        self.pointA = pointA
        self.pointB = pointB

        dy, dx = pointB - pointA
        g = gcd(dx, dy)
        self.dx = int(dx / g)
        self.dy = int(dy / g)
        self.Bdx = pointA.y * self.dx - pointA.x * self.dy
        # Note: Bdx comes from:
        #   y = mx + B
        #   y = (dy/dx)x + B
        #   y(dx) = (dy)x + B(dx)

    def id(self):
        return (self.dx, self.dy, self.Bdx)

    def __hash__(self):
        return hash((self.dx, self.dy, self.Bdx))

    def __str__(self):
        return '(dx: %s, dy: %s, Bdx: %s)' % (self.dx, self.dy, self.Bdx)

    def __repr__(self):
        return '(dx: %s, dy: %s, Bdx: %s)' % (self.dx, self.dy, self.Bdx)

    def clone(self):
        return Line(self.pointA, self.pointB)



class LineMap:

    def __init__(self, EPSILON):
        self.EPSILON = EPSILON
        self.lines = {}

    def add(self, line):
        for key in self.getLineKeys(line):
            if key in self.lines:
                self.lines[key].append(line)
            else:
                self.lines[key] = [line]


    def getLineKeys(self, line):
         key0 = (self.round(line.dx), self.round(line.dy), self.round(line.Bdx))
         key1 = (key0[0] + self.EPSILON, key0[1] + self.EPSILON, key0[2] + self.EPSILON)
         key2 = (key0[0] - self.EPSILON, key0[1] - self.EPSILON, key0[2] - self.EPSILON)
         return [hash(key0), hash(key1), hash(key2)]

    def round(self, value):
        factor = int(value / self.EPSILON)
        return float(factor) * self.EPSILON

    def getLineWithMostPoints(self):
        # print(self.lines)
        lineWithMostPointsList = []
        for key in self.lines:
            if len(lineWithMostPointsList) < len(self.lines[key]):
                lineWithMostPointsList = self.lines[key]
        if 0 < len(lineWithMostPointsList):
            return lineWithMostPointsList[0]
        else:
            return None




def getBestLine(points):
    if not (0 < len(points)):
        return None

    lines = LineMap(.0001)
    for i in range(0, len(points)-1):
        for j in range(1, len(points)):
            pointA, pointB = points[i], points[j]

            if pointA == pointB:
                continue

            line = Line(pointA, pointB)
            lines.add(line)

    lineWithMostPoints = lines.getLineWithMostPoints()

    if lineWithMostPoints == None:
        somePoint = points[0]
        otherPoint = Point(somePoint.x + 1, somePoint.y)
        return Line(somePoint, otherPoint)

    return lineWithMostPoints


testcases = [
    [Point(0,0)],
    [Point(0,0),Point(1,1)],
    [Point(-1,1),Point(-1,-1),Point(1,1),Point(1,-1)],
    [Point(0,0),Point(0,1),Point(0,2),Point(3,1)],
    [Point(0,0),Point(0,1),Point(0,1),Point(3,1),Point(3,0),Point(3,-5),Point(3,9)],
    [Point(0,0),Point(0,0),Point(0,0),Point(0,0)],
    [Point(0,0),Point(0,0),Point(0,0),Point(0,0),Point(1,1),Point(0,1)],
    [Point(100,20), Point(120,40), Point(-900,-980), Point(100, 30)],
    [Point(33, 35), Point(37, 36)]
]


for i in range(len(testcases)):
    case = testcases[i]
    print('Case %s:' % i)
    print(case, end="\n")
    print(getBestLine(case))
    print()