"""
Tic Tac Toe Player
"""
import copy
import math
import itertools 


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
    X_count = count(board)["X_count"]
    O_count = count(board)["O_count"]
    EMPTY_count = count(board)["EMPTY_count"]

    if EMPTY_count != 0:
        if X_count == O_count:
            return X
        elif X_count == O_count + 1:
            return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_cells.add((i, j))
    return empty_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print(action, type(action)) 
    # print(action[0], action[1])
    i = action[0]
    j = action[1]

    if board[i][j] != EMPTY:
        raise Exception(f"({i}, {j}) is an Invalid Action")
    
    new_board = copy.deepcopy(board)

    if new_board[i][j] == EMPTY:
        next_player = player(new_board)
        new_board[i][j] = next_player
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        X_winner = all(cell == X for cell in row)
        O_winner = all(cell == O for cell in row)

        if X_winner is True and O_winner is False:
            return X
        elif X_winner is False and O_winner is True:
            return O
    
    columns = []
    
    for j in range(len(board[0])):
        columns.append([])
        for i in range(len(board)):
            columns[j].append(board[i][j])

    for row in columns:
        X_winner = all(cell == X for cell in row)
        O_winner = all(cell == O for cell in row)

        if X_winner is True and O_winner is False:
            return X
        elif X_winner is False and O_winner is True:
            return O
    
    diagnol_1 = []
    diagnol_2 = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j:
                diagnol_1.append(board[i][j])
            if i + j == len(board) - 1:
                diagnol_2.append(board[i][j])
    
    for diagnol in [diagnol_1, diagnol_2]:
        X_winner = all(cell == X for cell in diagnol)
        O_winner = all(cell == O for cell in diagnol)

        if X_winner is True and O_winner is False:
            return X
        elif X_winner is False and O_winner is True:
            return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    EMPTY_count = count(board)["EMPTY_count"]

    if EMPTY_count == 0:
        return True
    elif EMPTY_count != 0:
        if winner(board) is None:
            return False
        elif winner(board) is not None:
            return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) is True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        elif winner(board) is None:
            return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None

    alpha = float('-inf')
    beta = float('inf')

    if player(board) == X:
        list_of_actions = actions(board)
        values = []

        for action in list_of_actions:
            min_value = minvalue(result(board, action), alpha, beta)
            values.append(min_value)

        highest_minvalue = max(values)
        for (action, value) in zip(list_of_actions, values):
            if value == highest_minvalue:
                # print(f"(minimax fn, player = X) Action is: {action}")
                return action
        
    elif player(board) == O:
        
        list_of_actions = actions(board)
        values = []
        
        for action in list_of_actions:
            max_value = maxvalue(result(board, action), alpha, beta)
            values.append(max_value)

        lowest_maxvalue = min(values)
        # print(list_of_actions)
        # print(values)
        for (action, value) in zip(list_of_actions, values):
            # print(action, value)
            if value == lowest_maxvalue:
                # print(f"(minimax fn, player = O) Action is: {action}")
                return action
    return None


def maxvalue(board, alpha, beta):
    if terminal(board) is True:
        return utility(board)

    v = float('-inf')
    # v = -100000
    
    for action in actions(board):
        v = max(v, minvalue(result(board, action), alpha, beta))
        if v >= beta:
            return v
        if v > alpha:
            alpha = v
    
    # print("(maxvalue) v value is " + str(v))
    return v


def minvalue(board, alpha, beta):
    if terminal(board) is True:
        return utility(board)
    
    v = float('inf')
    # v = 100000

    for action in actions(board):
        v = min(v, maxvalue(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        if v < beta:
            beta = v
    
    # print("(minvalue) v value is " + str(v))
    return v

        
def count(board):
    X_count = 0
    O_count = 0
    EMPTY_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                X_count += 1
            elif cell == O:
                O_count += 1
            elif cell == EMPTY:
                EMPTY_count += 1
    count_dict = {
        "X_count": X_count,
        "O_count": O_count,
        "EMPTY_count": EMPTY_count
    }
    return count_dict