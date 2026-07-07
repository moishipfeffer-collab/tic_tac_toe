def check_board_row(board):
    for x in board:
        if  x[0]==x[1]==x[2] and x[0] !="-":
            return True
def check_board_column(board):
    for y in range(3):
        if board[0][y]==board[1][y]==board[2][y] and board[0][y] != "-":
            return True

def boards_outputs(board):
    if check_board_row(board):
        print("You Won!\nGame Over!" )
    elif check_board_column(board):
        print("You Won!\nGame Over!")

