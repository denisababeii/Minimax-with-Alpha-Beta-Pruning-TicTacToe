from Board import *
import copy
import random

class Computer:

    def is_column_available(self,board,col): # checks whether a column is available for the computer to move
        return board.get(0,col)==0

    def available_columns(self,board): # returns a list of all the available columns
        columns=[]
        for c in range(7):
            if self.is_column_available(board,c):
                columns.append(c)
        return columns

    def is_over(self,board): # returns True if the game is over
        return board.is_won(1) or board.is_won(2) or board.is_tie()

    def evaluate(self,four_tuple,piece): # assigns a score to each situation, depending on the number of positions that need to be taken in order to win the game
        score=0
        opponent_piece=1
        if piece==1:
            opponent_piece=2
        if four_tuple.count(piece)==4: # if there is a tuple of 4 identical pieces, then that is scored the highest (1000p)
            score+=1000
        elif four_tuple.count(piece)==3 and four_tuple.count(0)==1: # if there are 3 identical pieces and an empty slot, then it is scored 25p
            score+=25
        elif four_tuple.count(piece)==2 and four_tuple.count(0)==2: # 2 pieces and 2 empty slots are scored 10p
            score+=10
        if four_tuple.count(opponent_piece)==3 and four_tuple.count(0)==1: # if the opponent has 3 pieces and an empty slot, then the score is decreased with 15p
            score-=15
        return score        

    def score_pos(self,board,piece):
        score=0

        b=board.get_board()

        for r in range(6): # horizontal score
            row=[]
            for c in range(7):
                row.append(b[r][c])
            for c in range(4):
                four_tuple=row[c:c+4]
                score+=self.evaluate(four_tuple,piece)

        for c in range(7): # vertical score
            column=[]
            for r in range(6):
                column.append(b[r][c])
            for r in range(3):
                four_tuple=column[r:r+4]
                score+=self.evaluate(four_tuple,piece)

        for r in range(3): # diagonal score (positively slant)
            for c in range(4):
                four_tuple=[board.get(r+i,c+i) for i in range(4)]
                score+=self.evaluate(four_tuple,piece)

        for r in range(3): # diagonal score (negatively slant)
            for c in range(4):
                four_tuple=[board.get(r+3-i,c+i) for i in range(4)]
                score+=self.evaluate(four_tuple,piece)   

        return score   

    def move_minimax(self,board,depth,alpha,beta,maximizing):
        av_col=self.available_columns(board)
        is_over=self.is_over(board)
        if depth==0 or is_over:
            if is_over: 
                if board.is_won(2): # if the game is won by the AI, then a high score is returned, so that path is chosen
                    return (None,1000000)  
                elif board.is_won(1):
                    return (None,-1000000) # otherwise, a low score is returned, to prevent the player from winning
                else:
                    return (None,0) # if it is a tie then the score is set to 0
            else: # depth is 0
                return (None,self.score_pos(board,2))
        if maximizing: # maximizes the AI score
            maxi=-10000000
            col=random.choice(av_col)
            for c in av_col:
                board_copy=copy.deepcopy(board)
                board_copy.drop_piece(c,2) # tries a move
                new_score=self.move_minimax(board_copy,depth-1,alpha,beta,False)[1] # plays on its own and calculates the score; it alternates between maximizing AI score and minimizing player's score
                if new_score>maxi: # chooses the path with the maximum score
                    maxi=new_score
                    col=c
                alpha=max(alpha,maxi) # eliminates paths that are not efficient
                if alpha>=beta:
                    break
            return col,maxi
        else: # minimizing the player
            mini=1000000
            col=random.choice(av_col)
            for c in av_col:
                board_copy=copy.deepcopy(board)
                board_copy.drop_piece(c,1)
                new_score=self.move_minimax(board_copy,depth-1,alpha,beta,True)[1]
                if new_score<mini: # chooses the path with the minimum score for the player
                    mini=new_score
                    col=c
                alpha=min(beta,mini)
                if alpha>=beta:
                    break
            return col,mini