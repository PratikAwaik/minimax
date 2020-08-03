"""
Tic Tac Toe Player
"""
import copy
import math
import random

X = "X"
O = "O"
EMPTY = None

def all_cells_filled(board):

    count = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j]) != EMPTY:
                count += 1
    
    if count == 9:
        return True
    
    return False

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
    if board == initial_state():
        return X
    x_count = 0 
    o_count = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
        
    if x_count == o_count:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))
    
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    try:
        if board_copy[action[0]][action[1]] == EMPTY:
            board_copy[action[0]][action[1]] = player(board)
            return board_copy
    except:
        raise Exception("Invalid Move")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal
    for row in board:
        x_count = row.count(X)
        o_count = row.count(O)
        if x_count == 3:
            return X
        elif o_count == 3:
            return O
    
    # Vertical
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            
            if board[j][i] == X:
                x_count += 1
            elif board[j][i] == O:
                o_count += 1
        if x_count == 3:
            return X
        elif o_count == 3:
            return O
        
    # Diagonals 
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O
    
    return None
    
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if all_cells_filled(board) and winner(board) == None:
        return True
    if winner(board) == X or winner(board) == O:
        return True
    elif winner(board) is not None:
        return False


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
    act = None
    if board == initial_state():
        act = random.choice(actions(board))
        return act

    elif player(board) == X:
        v = -math.inf
        for action in actions(board):
            v_new = min_value(result(board, action))
            if v_new > v:
                v = v_new
                act = action
    
    else:
        v = math.inf
        for action in actions(board):
            v_new = max_value(result(board, action))
            if v_new < v:
                v = v_new
                act = action
    return act

def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v