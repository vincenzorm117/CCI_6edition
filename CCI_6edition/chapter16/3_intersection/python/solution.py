#!/usr/local/bin/python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)


def intersection(A1, A2, B1, B2):
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
        # Points must intersect, find x that matches both
        x = (B1.y - (dBy/dBx)*B1.x - A1.y + (dAy/dAx)*A1.x) / ((dAy/dAx) - (dBy/dBx))
        return (x, x*(dBy/dBx) + B1.y - (dBy/dBx)*B1.x)



testcases = [
    (Point(0,0),Point(1,1),Point(0,2),Point(1,3), None),
    (Point(0,0),Point(1,1),Point(0,0),Point(1,1), None),
    (Point(0,0),Point(1,1),Point(0,0),Point(1,3), None),
]

for A1, A2, B1, B2, answer in testcases:
    print(A1, A2, B1, B2)
    solution = intersection(A1, A2, B1, B2)
    print(solution)