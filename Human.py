from Player import Player
import Game


class Human(Player):
    def __init__(self, name, Symbol):
        self.Name = name
        self.Type = "Human"
        self.Symbol = Symbol

    def GetMove(self, board):
        """Get user input and handle moves"""
        move = None
        while True:
            move = input("Enter coordinates as XY (e.g. 21): ")
            if board[Game.GetIndexFromCoords(*move)] == " ":
                return Game.GetIndexFromCoords(*move)
            else:
                print("Space occupied.")
