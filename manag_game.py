from board_check import all_checks,boards_outputs
from board import print_board, create_board,input_explain
from play_movement import is_free, get_index, mark_board,get_simbol
from players import ask_player_names

def run_game():
    name1,name2 = ask_player_names()
    sign_1,sign_2=get_simbol(name1,name2)
    input_explain(name1)
    board = create_board ()
    player = 1

    for turn in range (9):
        
        row, column = get_index(player, name1,name2)
    
        if is_free(board,row,column):
            if player % 2 != 0:
                mark_board(board,row,column,sign_1)
            else:
                mark_board(board,row,column,sign_2)
            print_board(board)

        else:
            print ("that index wasn't free") 
            turn-=1
            continue

            
        if all_checks(board):
            boards_outputs (board, player, name1, name2)
            break

        if turn == 9:
            print ("Board is full, game over!")
        
        player += 1                    



