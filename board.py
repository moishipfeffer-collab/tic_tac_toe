def create_board ():
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return board

def print_board (board:list):
    print()
    for row in board:
        for column in row:
            print (f"{column}", end ="  ")
        print()

def input_explain ():
    print (" to play, please enter the index of row and column as seen in the picture: you would like to put your symbol")
    print (""" 
    columnn 1  2  3
    Row 1   -  -  -
        2   -  -  -
        3   -  -  -
           """)
    
board = create_board()
print_board(board)
input_explain()