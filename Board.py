from texttable import *

class Board:

    def __init__(self):
        '''

        0 is empty square
        1 is player
        2 is computer

        '''
        self._board=[[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7] # the board is a matrix with 6 rows and 7 columns
        self._moves=0


    def get (self,row,col): # gets a certain position in the board
        return self._board[row][col]

    def get_board(self): # gets the board
        return self._board


    def drop_piece(self,col,piece):
        if piece not in [1,2]: # piece must be numbered with 1 or 2
            raise Exception("Invalid piece!")
        if col<0 or col>6: # columns are counted from 0 to 6
            raise Exception("Invalid column!")
        row=5
        for i in range(6): # the pieces are positioned in columns starting from the bottom
            if self._board[i][col]!=0:
                row=i-1
                break
        if row==-1:
            raise Exception("Column is full!")
        self._board[row][col]=piece
        self._moves+=1


    def is_won(self,piece):

        # horizontal checking

        for c in range(4):
            for r in range(6):
                if self._board[r][c]==self._board[r][c+1]==self._board[r][c+2]==self._board[r][c+3]==piece:
                    return True

        # vertical checking

        for c in range(7):
            for r in range(3):
                if self._board[r][c]==self._board[r+1][c]==self._board[r+2][c]==self._board[r+3][c]==piece:
                    return True

        # diagonal checking

        for c in range(4):
            for r in range(3):
                if self._board[r][c]==self._board[r+1][c+1]==self._board[r+2][c+2]==self._board[r+3][c+3]==piece:
                    return True
        for c in range(4):
            for r in range(3,6):
                if self._board[r][c]==self._board[r-1][c+1]==self._board[r-2][c+2]==self._board[r-3][c+3]==piece:
                    return True

        return False


    def is_tie(self): # if the game is not won and there is no move left, then it is a tie
        return self._moves==42


    def draw_board(self):
        t=Texttable()
        for i in range(6):
            row=[]
            d={0:' ',1:'o',2:'●'}
            for j in range(7):
                row.append(d[self._board[i][j]])
            t.add_row(row)
        return t.draw()
