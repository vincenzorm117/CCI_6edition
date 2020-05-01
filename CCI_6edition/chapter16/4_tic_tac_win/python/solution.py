

# Uses 4 arrays to determine who has won. There is an array
# to check the horizontal, vertical and diagonals to see who
# won. Space complexity is 2N or O(N). Checkwin runs in constant time: O(1).
class TicTacToeGameNxN:
    # 00 is None
    # 01 is O
    # 10 is X

    typeMap = {
        0b01: 'X',
        0b10: 'O',
        'X': 0b01,
        'O': 0b10
    }


    def __init__(self, N):
        self.N = N
        self.resetBoard()
        self.winner = None


    def resetBoard(self):
        self.board = 0
        self.checkerHorizontal = [0] * self.N
        self.checkerVertical = [0] * self.N
        self.checkerDiagonalDown = 0
        self.checkerDiagonalUp = 0


    def xyToBinOffset(self, x, y):
        return 2 * (self.N * int(y) + int(x))

    def getValue(self, x, y):
        offset = self.xyToBinOffset(x, y)
        return (self.board & (0b11 << offset)) >> offset

    def setValue(self, type, x, y):
        offset = self.xyToBinOffset(x,y)
        self.board = self.board | (self.typeMap[type] << offset)

        # Update all checkers to determine who won
        value = 1 if type == 'X' else -1
        self.checkerHorizontal[x] += value
        self.checkerVertical[y] += value
        if x == y:
            self.checkerDiagonalDown += value
        if x == (self.N - y - 1):
            self.checkerDiagonalUp += value

        if abs(self.checkerHorizontal[x]) == self.N:
            self.winner = type
        if abs(self.checkerVertical[y]) == self.N:
            self.winner = type
        if abs(self.checkerDiagonalDown) == self.N:
            self.winner = type
        if abs(self.checkerDiagonalUp) == self.N:
            self.winner = type



    def makeMove(self, type, x, y):
        if not self.isMoveValid(type, x, y):
            print('Invalid Move')
            return None
        self.setValue(type, x, y)

    def isMoveValid(self, type, x, y):
        if not (type == 'X' or type == 'O'):
            return False
        if not (0 <= x and x < self.N and 0 <= y and y < self.N):
            return False
        return 0 == self.getValue(x, y)

    def checkWin(self):
        return self.winner

    def print(self):
        for y in range(self.N):
            for x in range(self.N):
                value = self.getValue(x, y)
                if value in self.typeMap:
                    print(self.typeMap[value], end="")
                else:
                    print(' ', end="")
                if x != (self.N-1):
                    print('|', end="")
            print()
            if y != (self.N-1):
                print('–' * (self.N * 2) )




class TicTacToeGame3x3:
    # 00 is None
    # 01 is O
    # 10 is X

    typeMap = {
        0b01: 'X',
        0b10: 'O',
        'X': 0b01,
        'O': 0b10
    }

    def __init__(self):
        self.resetBoard()

    def resetBoard(self):
        self.board = 0b000000000000000000

    def makeMove(self, type, x, y):
        if not self.isMoveValid(type, x, y):
            print('Invalid Move')
            return None

        offset = self.xyToBinOffset(x,y)
        self.board = self.board | (self.typeMap[type] << offset)


    def xyToBinOffset(self, x, y):
        return 2 * (3 * int(y) + int(x))

    def isMoveValid(self, type, x, y):
        if not (type == 'X' or type == 'O'):
            return False
        if not (0 <= x and x < 3 and 0 <= y and y < 3):
            return False

        offset = self.xyToBinOffset(x,y)
        return 0 == (self.board & (0b11 << offset)) >> offset



    def print(self):
        for y in range(3):
            for x in range(3):
                offset = self.xyToBinOffset(x,y)
                value = (self.board & (0b11 << offset)) >> offset
                if value in self.typeMap:
                    print(self.typeMap[value], end="")
                else:
                    print(' ', end="")
                if x != 2:
                    print('|', end="")
            print()
            if y != 2:
                print('–––––')



    def checkWin(self):
        t1 = self.board & 0b111111000000000000
        t2 = self.board & 0b000000111111000000
        t3 = self.board & 0b000000000000111111

        if t1 == 0b010101000000000000:
            return 'X'
        if t1 == 0b101010000000000000:
            return 'O'

        if t2 == 0b000000010101000000:
            return 'X'
        if t2 == 0b000000101010000000:
            return 'O'

        if t3 == 0b000000000000010101:
            return 'X'
        if t3 == 0b000000000000101010:
            return 'O'

        t4 = self.board & 0b110000110000110000
        t5 = self.board & 0b001100001100001100
        t6 = self.board & 0b000011000011000011

        if t4 == 0b010000010000010000:
            return 'X'
        if t4 == 0b100000100000100000:
            return 'O'

        if t5 == 0b000100000100000100:
            return 'X'
        if t5 == 0b001000001000001000:
            return 'O'

        if t6 == 0b000001000001000001:
            return 'X'
        if t6 == 0b000010000010000010:
            return 'O'

        t7 = self.board & 0b110000001100000011
        t8 = self.board & 0b000011001100110000


        if t7 == 0b010000000100000001:
            return 'X'
        if t7 == 0b100000001000000010:
            return 'O'

        if t8 == 0b000001000100010000:
            return 'X'
        if t8 == 0b000010001000100000:
            return 'O'

        return None


# Testcase: Check varying board sizes and wins

# for N in range(10):
#     game = TicTacToeGameNxN(N)
#     for i in range(N):
#         game.makeMove('X', i, 0)
#     game.print()
#     print(game.checkWin())
#     print()

#     game = TicTacToeGameNxN(N)
#     for i in range(N):
#         game.makeMove('O', 0, i)
#     game.print()
#     print(game.checkWin())
#     print()

#     game = TicTacToeGameNxN(N)
#     for i in range(N):
#         game.makeMove('X', i, i)
#     game.print()
#     print(game.checkWin())
#     print()

#     game = TicTacToeGameNxN(N)
#     for i in range(N):
#         game.makeMove('O', i, (N - i - 1))
#     game.print()
#     print(game.checkWin())
#     print()


# Testcase: Check no win when blocked

# game = TicTacToeGameNxN(5)
# game.makeMove('X', 0, 0)
# game.makeMove('X', 1, 0)
# game.makeMove('X', 2, 0)
# game.makeMove('X', 3, 0)
# game.makeMove('O', 4, 0)
# game.print()
# print(game.checkWin())
# print()



# Testcase: Check no win when blocked and invalid move

# game = TicTacToeGameNxN(5)
# game.makeMove('X', 0, 0)
# game.makeMove('X', 1, 0)
# game.makeMove('X', 2, 0)
# game.makeMove('X', 3, 0)
# game.makeMove('O', 4, 0)
# game.makeMove('X', 4, 0)
# game.print()
# print(game.checkWin())
# print()


# Testcase: Check giant board
#   NOTE: Its slow because of the range. Not sure why.

N = 10000
game = TicTacToeGameNxN(N)
for i in range(N):
    game.makeMove('X', i, 0)
print(game.checkWin())
print()

game = TicTacToeGameNxN(N)
for i in range(N):
    game.makeMove('O', 0, i)
print(game.checkWin())
print()


game = TicTacToeGameNxN(N)
for i in range(N):
    game.makeMove('X', i, i)
print(game.checkWin())
print()

game = TicTacToeGameNxN(N)
for i in range(N):
    game.makeMove('O', i, (N - i - 1))
print(game.checkWin())
print()