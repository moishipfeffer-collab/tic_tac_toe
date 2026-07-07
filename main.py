from board_check import check_board_column,check_board_full,check_board_row,boards_outputs
from board import print_board, create_board,input_explain
from play_movement import is_free, get_index, mark_board
from players import ask_player_name

def main ():
    ask_player_name()
    input_explain()
    board = create_board ()
    turns_played = 0

    for i in range (9):
        row, column = get_index()
        
        if is_free(board,row,column):
            mark_board(board,row,column,'X')
            print_board(board)
            turns_played +=1

        else:
            print ("that index wasn't free")
            i-=1
            continue
        
        if check_board_row(board) or check_board_column(board):
            boards_outputs (board)
            break

        if i == 9:
            print ("Board is full, game over!")

main ()
