from tictactoe import player, actions, winner, minimax

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
         [X, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

# print(player(board))
# print(actions(board))
print(minimax(board))