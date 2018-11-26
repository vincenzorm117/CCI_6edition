#!/usr/local/bin/python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

def isBetween(start, mid, end):
    return (start.x <= mid.x and mid.x <= end.x and start.y <= mid.y and mid.y <= end.y) or (end.x <= mid.x and mid.x <= start.x and end.y <= mid.y and mid.y <= start.y)

def intersection(A1, A2, B1, B2):
    # Check if line segments could not intersect
    if not isBetween(A1, B1, A2) and not isBetween(A1, B2, A2) and not isBetween(B1, A1, B2) and not isBetween(B1, A2, B2):
        return None

    dAx = (A2.x - A1.x)
    dAy = (A2.y - A1.y)
    dBx = (B2.x - B1.x)
    dBy = (B2.y - B1.y)
    
    # Check for same slope
    if dAy*dBx == dBy*dAx:
        # Check for same y-intercept
        if A1.y * dAx * dBx - dAy * dBx * A1.x == B1.y * dAx * dBx - dBy * dAx * B1.x:
            return A1
        else:
            return None
    else:
        if dAx == 0:
            y = A1.y
            return ((y - (B1.y - (dBy/dBx)*B1.x))/(dBy/dBx), y)
        if dBx == 0:
            y = B1.y
            return ((y - (A1.y - (dAy/dAx)*A1.x))/(dAy/dAx), y)

        # Points must intersect, find x that matches both
        x = (B1.y - (dBy/dBx)*B1.x - A1.y + (dAy/dAx)*A1.x) / ((dAy/dAx) - (dBy/dBx))
        return (x, x*(dBy/dBx) + B1.y - (dBy/dBx)*B1.x)



testcases = [
    (Point(0,0),Point(1,1),Point(0,2),Point(1,3), None),
    (Point(0,0),Point(1,1),Point(0,0),Point(1,1), None),
    (Point(0,0),Point(1,1),Point(0,0),Point(1,3), None),
    (Point(-1,1),Point(1,-1),Point(-1,-1),Point(1,1), None),
    (Point(0,-4),Point(0,4),Point(0,-1),Point(0,1), None),
    (Point(0,-4),Point(0,4),Point(1,-1),Point(1,1), None),
    (Point(0,0),Point(1,1),Point(1,0),Point(1,1), None),
    (Point(0,0),Point(2,2),Point(1,0),Point(1,3), None),
    (Point(0,0),Point(1,1),Point(2,2),Point(3,5), None),
]

for A1, A2, B1, B2, answer in testcases:
    print(A1, A2, B1, B2)
    solution = intersection(A1, A2, B1, B2)
    print(solution)
    print()