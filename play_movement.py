def get_index(player, name1,name2):
    if player % 2 !=0:
        row = input(f"{name1} please enter the row and click enter:\n")
        column = input(f"{name1} please enter the column and hit enter:\n")
    else:
        row = input(f"{name2} please enter the row and click enter:\n")
        column = input(f"{name2} please enter the column and hit enter:\n")

    while not check_integer(row,column):
        row = input()
        column = input()
    
    
    # row > 3 or column > 3 or row <1 or column <1:
    #     print ("index out of range")
    #     row = int(input("please enter the row and click enter:\n"))
    #     column = int(input("please enter the column and hit enter:\n"))
    row =int (row)
    column= int(column)     
    return row, column

def is_free(board,row,column):
    if board[row-1][column-1] == "-":
        return True
    

def mark_board(board, row,column ,symbol):
    board[row-1][column-1] = symbol
    return board




def check_integer(row, column):
    try:
        int(row), int(column)
        return True
    except ValueError:
        print('invalid input please enter a new row and then a new column ')

def is_in_range(row ,column,board_size):
    return 1 <=(row and column) <=board_size

