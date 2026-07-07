def get_index():
    print("please enter row and then column (1-3):" )
    row = int(input())
    column = int(input())
    if (row or column > 3) or (row or column <1):
        print ("index out of range")
        get_index ()
    return row, column

def is_free(board,row,column):
    if board[row-1][column-1] == "-":
        return True
    else:
        False

def mark_board(board, row,column ,symbol):
    board[row-1][column-1] = symbol
    return board
