#!/usr/local/bin/python3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.dx = (point2[0] - point1[0])
        self.dy = (point2[1] - point1[1])
        self.points = []
        self.addPoint(point1)
        self.addPoint(point2)

    def addPoint(self, point):
        self.points.append(point)

    def size(self):
        return len(self.points)

    def pointOnLine(self, point):
        return point[1] * self.dx + self.dy * self.point1[0] == self.dy * point[0] + self.point1[1] * self.dx

    def __str__(self):
        return str(self.size()) + ' ' + str(self.points)


def GetBestLine(points):
    if len(points) < 2:
        return None
    bestLine = None
    lines = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            A,B = points[i], points[j]
            if (A,B) in lines:
                continue
            line = Line(A, B)
            lines[(A,B)] = line
            lines[(B,A)] = line
            for curr in range(j+1, len(points)):
                C = points[curr]
                if line.pointOnLine(C):
                    lines[(B,C)] = line
                    lines[(C,B)] = line
                    line.addPoint(C)
            if bestLine is None or bestLine.size() < line.size():
                bestLine = line
    return bestLine



testcases = [
    [(0,0)],
    [(0,0),(1,1)],
    [(-1,1),(-1,-1),(1,1),(1,-1)],
    [(0,0),(0,1),(0,1),(3,1)],
    [(0,0),(0,1),(0,1),(3,1),(3,0),(3,-5),(3,9)],
]


for i in range(len(testcases)):
    case = testcases[i]
    print('Case %s:' % i)
    print(case, end="\n\n")
    print(GetBestLine(case))