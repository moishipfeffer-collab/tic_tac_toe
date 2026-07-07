def check_board(board):
    for x in board:
        if  x[0]==x[1]==x[2]:
            print("win!")
    for y in range(3):
        if board[0][y]==board[1][y] and board[0][y]==board[2][y]:
            print("win!")
    if not " " in board:
        print("the board is full, game over")
    
    

check_board([[0,1,0],[1,0,0],[1,1,0]])