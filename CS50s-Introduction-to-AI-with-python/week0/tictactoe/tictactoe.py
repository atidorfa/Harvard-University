"""
Tic Tac Toe Player
"""

import math
import numpy as np
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == X:
                turn += 1
            elif board[i][j] == O:
                turn -= 1
    
    if turn % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)

    if action == []:
        raise NameError('no action to be performed')

    i, j = action
    if player(board) == X:
       new_board[i][j] = X
    else:
       new_board[i][j] = O

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board.count(X) >= 3:
        for i in range(0, len(board)):
            if (board[i][0] != EMPTY) and (board[i][0] == board[i][1] == board[i][2]):
                return board[i][0]

        for j in range(0, len(board)):
            if (board[0][j] != EMPTY) and (board[1][j] == board[i][1] == board[2][j]):
                return board[0][j]

        if (board[0][0] != EMPTY) and (board[0][0] == board[1][1] == board[2][2]):
            return board[0][0]

        if (board[0][2] != EMPTY) and (board[0][2] == board[1][1] == board[2][0]):
            return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == EMPTY:
                return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def max_value(board):
        v = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, min_value(result(board,action)))
        return v

    def min_value(board):
        v = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board,action)))
        return v
    
    if terminal(board):
        return None

    move = None  
    
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            min_v = min_value(result(board, action))
            if v < min_v:
                v = min_v
                move = action
    elif player(board) == O:
        v = math.inf
        for action in actions(board):
            max_v = min_value(result(board, action))
            if v > max_v:
                v = max_v
                move = action
    
    return move