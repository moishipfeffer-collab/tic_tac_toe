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
    print ("to play, please enter the row index\npres enter and then the column index\n as seen in the picture:")
    print (""" 
        columnn 
            1  2  3
    Row 1   -  -  -
        2   -  -  -
        3   -  -  -
           
           Lets Start Playing!
           """)
