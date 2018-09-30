#!/usr/local/bin/python3



def printBoard(board):
    for row in board:
        print(''.join(row))
    print()


def eight_queens():
    def eq(board, usedCols, usedDiagX, usedDiagY, y):
        if y == 8:
            printBoard(board)
            return
        for x in range(8):
            dx = x+y
            dy = y-x+7
            if x not in usedCols and dx not in usedDiagX and dy not in usedDiagY:
                board[x][y] = 'Q'
                usedCols.add(x)
                usedDiagX.add(dx)
                usedDiagY.add(dy)
                eq(board, usedCols, usedDiagX, usedDiagY, y+1)
                usedCols.remove(x)
                usedDiagX.remove(dx)
                usedDiagY.remove(dy)
                board[x][y] = 'X'
    board = [ 
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X'],
        ['X','X','X','X','X','X','X','X']
    ]
    eq(board, set(), set(), set(), 0)
    

eight_queens()