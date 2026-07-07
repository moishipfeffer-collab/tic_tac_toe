def get_index():
    while True:
#        try:
            index= int(input("choose a place (1-9): "))
            if 1 <= index <=9:
                break
            print('index must be between 1 and 9 ')
#        except ValueError:
#            print('please enter a number ')    
    return index

def is_free(board,index):
    return board[index] == " "

def mark_board(board, index, symbol):
    board[index] = symbol
        
