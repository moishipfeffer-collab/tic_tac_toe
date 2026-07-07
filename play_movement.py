def get_index(player, name1,name2):
    if player % 2 !=0:
        row = int(input(f"{name1} please enter the row and click enter"))
        column = int(input(f"{name1}please enter the column and hit enter"))
    else:
        row = int(input(f"{name2} please enter the row and click enter"))
        column = int(input(f"{name2}please enter the column and hit enter"))

    while row > 3 or column > 3 or row <1 or column <1:
        print ("index out of range")
        row = int(input("please enter the row and click enter: "))
        column = int(input("please enter the column and hit enter: "))
            
    return row, column

def is_free(board,row,column):
    if board[row-1][column-1] == "-":
        return True
    

def mark_board(board, row,column ,symbol):
    board[row-1][column-1] = symbol
    return board
