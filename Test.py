import unittest
from Game import *

class Tests(unittest.TestCase):
    def test_drop_piece(self):
        board=Board()
        board.drop_piece(1,1)
        self.assertTrue(board._moves==1)
        with self.assertRaises(Exception):
            board.drop_piece(1,3)
        with self.assertRaises(Exception):
            board.drop_piece(7,1)
        board.drop_piece(1,1)
        board.drop_piece(1,1)
        board.drop_piece(1,1)
        board.drop_piece(1,1)
        board.drop_piece(1,1)
        with self.assertRaises(Exception):
            board.drop_piece(1,1)

    def test_is_won(self):
        board=Board()
        board.drop_piece(1,1)
        self.assertFalse(board.is_won(1))
        board.drop_piece(2,1)
        board.drop_piece(3,1)
        board.drop_piece(4,1)
        self.assertTrue(board.is_won(1))

    def test_game(self): # tests players's move and when the game is over
        board=Board()
        computer=Computer()
        game=Game(board,computer)
        game.move_player(2)
        self.assertTrue(board._moves==1)
        with self.assertRaises(Exception):
            game.move_player(7)
        game.move_player(2)
        game.move_player(2)
        game.move_player(2)
        self.assertTrue(game.game_over())
    
    def test_computer(self):
        board=Board()
        computer=Computer()
        game=Game(board,computer)
        game.move_computer()
        self.assertFalse(board.get(5,3)==0)
        game.move_player(1)
        game.move_player(1)
        game.move_player(1)
        game.move_computer()
        self.assertTrue(board.get(2,1)==2)