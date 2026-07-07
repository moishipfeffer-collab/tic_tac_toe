def check_board_row(board):
    for x in board:
        if  x[0]==x[1]==x[2]:
            return True
def check_board_column(board):
    for y in range(3):
        if board[0][y]==board[1][y]==board[2][y]:
            return True
def check_board_full(board):
    if not " " in board:
        print("the board is full, game over")
    
    

