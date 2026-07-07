def get_index():
    print("please enter row and then column (1-3):" )
    row = int(input())
    column = int(input())
    return row, column

def is_free(board,row,column):
    if board[row][column] == "-":
        return True
    else:
        False

def mark_board(board, row,column ,symbol):
    board[row][column] = symbol
    return board
