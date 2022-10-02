
import numpy as np
ROW, COLS = 8, 8
piece = {'b_pawn': 1.0, 'b_rook': 5.0, 'b_knight': 3.1, 'b_bishop': 3.0, 'b_queen': 9.0, 'b_king': 1000.0,
         'w_pawn': -1.0, 'w_rook': -5.0, 'w_knight': -3.1, 'w_bishop': -3.0, 'w_queen': -9.0, 'w_king': -1000.0}
player1 = "White"
player2 = "Black"

play1pt = 0
player2pt = 0

winner = None

if play1pt == 1000:
    print(winner=player1)
elif player2pt == -1000:
    print(winner=player2)


interactive_board = []

chessboard = [[5.0, 3.1, 3.0, 1000.0, 9.0, 3.0, 3.1, 5.0],
              [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
              [-5.0, -3.1, -3.0, -9.0, -1000.0, -3.0, -3.1, -5.0]]


# numpy loop to get cols and rows to store into interactive_board
chessboard = np.asarray(chessboard)
for col in range(chessboard.shape[1]):
    interactive_board.append(chessboard[:, col])


print(interactive_board[0][-1])
game_on = 'Y'
while game_on:
    game_on = input("Press 'Y' to start: ")
    if start.upper() == "Y":
        player1_move =
