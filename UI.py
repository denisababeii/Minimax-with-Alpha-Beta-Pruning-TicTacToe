from Game import *

class UI:
    def __init__(self,game):
        self._game=game

    def start(self):
        player_move=True # player starts
        print(self._game._board.draw_board())
        print("Player is o, Computer is ●")
        print("Columns are counted from 1 to 7")
        while not self._game.game_over():
            try:
                if player_move:
                    col=int(input("Drop piece at column: "))
                    self._game.move_player(col-1) # columns are counted from 1 by the player
                else:
                    self._game.move_computer()
                player_move=not player_move
                print(self._game._board.draw_board())
            except Exception as e:
                print(e)
        print("GAME OVER!")
        if self._game._board.is_won(2)==True: # the game is won and it was the computers move
            print("Computer is the winner!")
        elif self._game._board.is_won(1)==True: # the game is won and it was the players move
            print("Player is the winner!")
        else:
            print("It's a tie!") # otherwise, it's a tie