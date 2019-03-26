from Board import Board
import Game
import Human
import AI

CurrentBoard = Board()

player_1 = Human.Human("Computer 1", "X")
player_2 = AI.MiniMax("Computer 2", "O")


while not Game.IsOver(CurrentBoard.BoardList):
    CurrentBoard.PrintBoard()

    CurrentBoard.BoardList = Game.UpdateBoard(CurrentBoard.BoardList, player_1)
    if Game.IsOver(CurrentBoard.BoardList):
        break

    CurrentBoard.PrintBoard()

    CurrentBoard.BoardList = Game.UpdateBoard(CurrentBoard.BoardList, player_2)


CurrentBoard.PrintBoard()

winner = Game.CheckWinner(CurrentBoard.BoardList)

print()
if winner is None:
    print("Tie!")
elif winner == player_1.Symbol:
    print(player_1.Name + " wins!")
elif winner == player_2.Symbol:
    print(player_2.Name + " wins!")
