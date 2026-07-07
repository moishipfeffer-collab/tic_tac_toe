def get_index():
    index= int(input("choose a place (1-9): "))
    return index

def is_free(board,row,column):
    if board[row][column] == "-":
        return True
    else:
        False

def mark_board(board, row,column ,symbol):
    board[row][column] = symbol
    return board
