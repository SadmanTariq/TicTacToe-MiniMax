from Player import Player
import Game


class MiniMax(Player):
    def __init__(self, name, symbol):
        self.Name = name
        self.Type = "Computer"
        self.Symbol = symbol
        if symbol == "X":
            self.OpponentSymbol = 'O'
        else:
            self.OpponentSymbol = 'X'

    def GetMove(self, board):
        """Return the best possible move."""
        return self.BestMove(board)

    def Evaluate(self, board):
        """Return 10 if game won, -10 if game lost and 0 for tie."""
        if Game.CheckWinner(board) == self.Symbol:
            return 10
        elif Game.CheckWinner(board) is None:
            return 0
        else:
            return -10

    def MovesLeft(self, board):
        """Return False if there are no moves left. Otherwise, return True."""
        if " " in board:
            return True
        else:
            return False

    def MiniMax(self, board, depth, isMax):
        # print(depth)
        score = self.Evaluate(board)

        if score == 10 or score == -10:
            return score

        if not self.MovesLeft(board):
            return 0

        if isMax:
            best = -1000

            for i in range(len(board)):
                if board[i] == ' ':
                    new_board = board.copy()
                    new_board[i] = self.Symbol

                    best = max(best, self.MiniMax(new_board, depth + 1,
                               not isMax))

            return best

        else:
            best = 1000

            for i in range(len(board)):
                if board[i] == ' ':
                    new_board = board.copy()
                    new_board[i] = self.OpponentSymbol

                    best = min(best, self.MiniMax(new_board, depth + 1,
                               not isMax))

            return best

    def BestMove(self, board):
        best_value = -1000
        best_move = None

        for i in range(len(board)):
            if board[i] == ' ':
                new_board = board.copy()
                new_board[i] = self.Symbol

                move_value = self.MiniMax(new_board, 0, False)

                if move_value > best_value:
                    best_value = move_value
                    best_move = i

        return best_move
