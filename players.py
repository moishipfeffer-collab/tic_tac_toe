def ask_player_names():
    name1 =input("player 1 what is your name?\n")
    name2 =input("player 2 what is your name?\n")
    print(f"hello {name1} and {name2}!\nWelcome to tic tac toe!\n{name1} your symbol is X, {name2} your symbol is O")
    return name1, name2
    