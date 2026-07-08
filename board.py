def create_board ():
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return board

def print_board (board:list):
    print()
    for row in board:
        for column in row:
            print (f"{column}", end ="  ")
        print()

def input_explain (name1):
    print ("to play, please enter the row index\nand then the column index\n . here is an example\n with a 3:# board size:")
    print (f""" 
        columnn 
            1  2  3
    Row 1   -  -  -
        2   -  -  -
        3   -  -  -
           
           Lets Start Playing!
           {name1} you are going to start!
           """)

def choose_size ():
    size = input ("please enter size of board that you want\nfor example - if you enter 5 the game will be a 5X5 board")
    while not size.isdigit():
        size = input ("invalid input. please re enter a number for the size")
    
    return int(size)

