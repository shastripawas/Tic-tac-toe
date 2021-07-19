import numpy as np
import random
from time import sleep

def create_board():
    board=np.zeros((3,3))
    return board

def check_empty(board):
    L=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j]==0):
                L.append((i,j))
    return L

def random_moves(board,player):
    L=check_empty(board)
    selected=random.choice(L)
    board[selected]=player
    return board

def check_winner_row(board,player):
    i=0
    while i<len(board):
        if np.all(board[i,:]==(player*(np.ones(len(board))))):
            break
        i+=1
    return (i!=(len(board)))

def check_winner_column(board,player):
    i=0
    while i<len(board):
        if np.all(board[:,i]==(player*(np.ones(len(board))))):
            break
        i+=1
    return (i!=(len(board)))

def check_winner_diagonal(board,player):
    n=len(board)
    L1=[(board[i][i]==(player)) for i in range(len(board))]
    L2=[(board[i][n-1-i]==(player)) for i in range(len(board))]
    return (all(L1) or all(L2))

def evaluate_winner(board,player):
    winner=0
    if check_winner_row(board,player) or check_winner_column(board,player) or check_winner_diagonal(board,player):
        winner=player
    if np.all(board!=0) and winner==0:
        winner=-1
    return winner

def play():
    board=create_board()
    count=1
    winner=0
    while winner==0:
        for player in range(1,3):
            board=random_moves(board,player)
            sleep(2)
            print("Board after " + str(count) + " moves: ")
            print(board)
            count+=1
            winner=evaluate_winner(board,player)
            if winner!=0:
                break
    return (winner)

print("The winner of the game is: " + str(play()))
