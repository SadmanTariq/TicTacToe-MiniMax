class Board:
    def __init__(self):
        self.BoardList = self.EmptyBoard()

    def EmptyBoard(self):
        """Return an empty Tic-Tac-Toe board as a list"""
        x = []
        for i in range(9):
            x.append(' ')
        return x

    def PrintBoard(self):
        """Print the board of this instance"""
        #   0   1   2
        # 0   |   |
        #  ---+---+---
        # 1   |   |
        #  ---+---+---
        # 2   |   |
        print("  0   1   2")
        print("0 %s | %s | %s" % tuple(self.BoardList[i] for i in range(3)))
        print(" ---+---+---")
        print("1 %s | %s | %s" % tuple(self.BoardList[i] for i in range(3, 6)))
        print(" ---+---+---")
        print("2 %s | %s | %s" % tuple(self.BoardList[i] for i in range(6, 9)))
