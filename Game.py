from Computer import *

class Game:
    def __init__(self,board,computer_player):
        self._board=board
        self._computer=computer_player

    def move_player(self,col):
        self._board.drop_piece(col,1) # player moves pieces numbered with '1'

    def move_computer(self):
        col,score=self._computer.move_minimax(self._board,5,-10000000,10000000,True) # depth is 4 for speed, maximizing is set to True
        self._board.drop_piece(col,2) # computer moves pieces numbered with '2'

    def get_board(self):
        return self._board

    def game_over(self):
        return self._board.is_tie() or self._board.is_won(1) or self._board.is_won(2) # If the game is tied or won, then it is over