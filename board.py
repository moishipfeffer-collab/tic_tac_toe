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
    print (" to play, please enter the index (1-9) you would like to put your symbol")
    print (""" 1  2  3
               4  5  6
               7  8  9
           """)