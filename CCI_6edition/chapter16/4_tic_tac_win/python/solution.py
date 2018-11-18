



class TicTacToeGame:
    # 01 is 0
    # 10 is X

    def __init__(self):
        self.resetBoard()

    def resetBoard(self):
        self.board = 0b000000000000000000

    def makeMove(self, type, x, y):
        if type != 0b01 or type != 0b10:
            return None
        x, y = int(x), int(y)
        if not (0 <= x and x < 3 and 0 <= y and y < 3):
            return None
        offset = 3*y+x
        self.board = self.board | (type << offset)
    
    def print(self):
        for y in range(2):
            for x in range(2):
                offset = 3*y+x
                value = (self.board & (0b11 << offset)) >> offset
                if value == 0b01:
                    print('O', end="")
                elif value == 0b10:
                    print('X', end="")
                else:
                    print(' ', end="")
            print()

    def checkWin(self):
        t1 = self.board & 0b111111000000000000
        t2 = self.board & 0b000000111111000000
        t3 = self.board & 0b000000000000111111
    
        if t1 == 0b010101000000000000:
            return 0b01
        if t1 == 0b101010000000000000:
            return 0b10

        if t2 == 0b000000010101000000:
            return 0b01
        if t2 == 0b000000101010000000:
            return 0b10
        
        if t3 == 0b000000000000010101:
            return 0b01
        if t3 == 0b000000000000101010:
            return 0b10

        t4 = self.board & 0b110000110000110000
        t5 = self.board & 0b001100001100001100
        t6 = self.board & 0b000011000011000011

        if t4 == 0b010000010000010000:
            return 0b01
        if t4 == 0b100000100000100000:
            return 0b10

        if t5 == 0b000100000100000100:
            return 0b01
        if t5 == 0b001000001000001000:
            return 0b10
        
        if t6 == 0b000001000001000001:
            return 0b01
        if t6 == 0b000010000010000010:
            return 0b10

        t7 = self.board & 0b110000001100000011
        t8 = self.board & 0b000011001100110000


        if t7 == 0b010000000100000001:
            return 0b01
        if t7 == 0b100000001000000010:
            return 0b10

        if t8 == 0b000001000100010000:
            return 0b01
        if t8 == 0b000010001000100000:
            return 0b10
        
        return None
