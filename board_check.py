def all_checks (board):
    if check_board_column(board) or check_board_row(board) or check_board_diagonal(board):
        return True


def check_board_row(board):
    for x in board:
        if  x[0]==x[1]==x[2] and x[0] !="-":
            return True
def check_board_column(board):
    for y in range(3):
        if board[0][y]==board[1][y]==board[2][y] and board[0][y] != "-":
            return True


def check_board_diagonal(board):
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] != "-":
        return True
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2] != "-":
        return True


def boards_outputs(board,player,name1,name2):
    print()
    if player % 2 !=0:
        winner = name1
    else:
        winner = name2
    if all_checks(board):
        print(f"{winner} You Won!\nGame Over!" )




