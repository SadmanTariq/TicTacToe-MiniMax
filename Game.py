def GetIndexFromCoords(x, y):
    """Return index of 3x3 board from x and y polar coordinates."""
    i = 0
    i += int(x)
    i += int(y) * 3
    return i


def HorizontalWinner(board):
    """Return the symbol of 3 in a row. If no winner, return None"""
    rows = [[board[i] for i in range(3)],
            [board[i] for i in range(3, 6)],
            [board[i] for i in range(6, 9)]]
    for row in rows:
        if all(row[i] != ' ' for i in range(3)):
            if all(row[0] == row[i] for i in range(3)):
                return row[0]

    return


def VerticalWinner(board):
    """Return the symbol of 3 in a column. If no winner, return None"""
    columns = [[board[i] for i in [0, 3, 6]],
               [board[i] for i in [1, 4, 7]],
               [board[i] for i in [2, 5, 8]]]
    for column in columns:
        if all(column[i] != ' ' for i in range(3)):
            if all(column[0] == column[i] for i in range(3)):
                return column[0]

    return


def DiagWinner(board):
    """Return the symbol of 3 in a diagonal. If no winner, return None"""
    if board[0] != ' ':
        if board[0] == board[4]:
            if board[0] == board[8]:
                return board[0]

    if board[2] != ' ':
        if board[2] == board[4]:
            if board[2] == board[6]:
                return board[2]

    return


def CheckWinner(brd):
    """Return the winner of a board. If no winner, return None"""
    return HorizontalWinner(brd) or VerticalWinner(brd) or DiagWinner(brd)


def IsOver(board):
    """Return True if game is over for board. Otherwise return False"""
    if CheckWinner(board):
        return True
    elif " " not in board:
        return True
    else:
        return False


def UpdateBoard(board, player):
    """Update board by getting input from player."""
    print("\n"+player.Name)
    new_board = board.copy()
    new_board[player.GetMove(board)] = player.Symbol

    return new_board
