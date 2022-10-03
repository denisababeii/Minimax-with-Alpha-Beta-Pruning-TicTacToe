from UI import *

board=Board()
computer=Computer()
game=Game(board,computer)
ui=UI(game)
ui.start()