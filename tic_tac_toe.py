#This is Tic-Tac-Toe game
#Choose a symbol (X or O)
#Who starts first? Choose (Heads/Tails):
#Available coordinates are shown every turn



#=============
#Tic-Tac-Toe # 
#=============

import random                   # Import random module

def computer_turn_coord(crd):   # function to choose computer's coordinate
    return coord[crd]
def your_turn_coord(x, y):      # function to choose user's coordinate
    return (x, y)           

def choose_symbols():           # function to choose initial symbols 
    user_symbol = input("Choose your symbol (X or O): ").upper()
    while user_symbol not in ['X', 'O']:
        user_symbol = input("Invalid choice. Choose 'X' or 'O': ").upper()
    computer_symbol = 'O' if user_symbol == 'X' else 'X'
    print(f"You are '{user_symbol}', Computer is '{computer_symbol}'")
    return user_symbol, computer_symbol

def which_turn_first():         # Who will be the first player?
    user_choice = input("Choose Heads/Tails: ")
    if random.randint(0, 1) == 0:
        turn = "Heads"
    else:
        turn = "Tails"
    print(f"{turn} was chosen!:")
    
    if turn == user_choice:
        print("It is your turn!")
        return "USER"
    elif turn == "Tails":
        return "COMPUTER"
    
def check_win(symbol):              # Check winning combination
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

    
boardsize = 3
board = [[" " for _ in range(3)] for _ in range(3)]                                 # board shown
coord = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]    # available coordinates
    
def print_board():                                                  # Print the board
    print("=" * (boardsize * 2 + 1))
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell + "|", end="")
        print()
    print("=" * (boardsize * 2 + 1))
    
def game():                                                     # game loop
    your_turn_bool = None
    computer_turn_bool = None
    chosen_coord = None
    lst_coord = []
         
    for l in range(9):
        if l == 0:
            which_trn_first = which_turn_first()
            if which_trn_first == "USER":
                x_coord_my_move = int(input("Put your x coordinate: "))
                y_coord_my_move = int(input("Put your y coordinate: "))
                my_move = your_turn_coord(x_coord_my_move, y_coord_my_move)
                while my_move in lst_coord:
                    print("Choose another coordinate:")
                    x_coord_my_move = int(input("Put your x coordinate: "))
                    y_coord_my_move = int(input("Put your y coordinate: "))
                    my_move = your_turn_coord(x_coord_my_move, y_coord_my_move)
                chosen_coord = my_move
                lst_coord.append(chosen_coord)
                your_turn_bool = True
                computer_turn_bool = False
            elif which_trn_first == "COMPUTER":
                print("Computer's turn...")
                x_coord_computer = 0
                y_coord_computer = 0
                computer_move = computer_turn_coord(random.randint(0, len(coord) - 1))
                print(f"Computer chose: ({computer_move})")
                chosen_coord = computer_move
                while chosen_coord in lst_coord:
                    computer_move = computer_turn_coord(random.randint(0, len(coord) - 1))
                    chosen_coord = computer_move
                lst_coord.append(chosen_coord)
                computer_turn_bool = True
                your_turn_bool = False
                
            for u in range(3):
                for v in range(3):
                    if your_turn_bool == True and (u, v) == my_move:
                        board[u][v] = user_symbol
                        index1 = coord.index(chosen_coord)
                        coord.pop(index1)
                        if check_win(user_symbol):
                            print("You won!")
                            break
                        elif check_win("X"):
                            print("Computer won!")
                            break
                    elif computer_turn_bool == True and (u, v) == computer_move:
                        board[u][v] = computer_symbol
                        if check_win(user_symbol):
                            print("You won!")
                            break
                        elif check_win(computer_symbol):
                            print("Computer won!")
                            break
                        index1 = coord.index(chosen_coord)
                        coord.pop(index1)
                if check_win(user_symbol):
                    break
                elif check_win(computer_symbol):
                    break
            print_board()
            print(coord)
            if check_win(user_symbol):
                break
            elif check_win(computer_symbol):
                break
            
            if computer_turn_bool == True:
                your_turn_bool = True
                computer_turn_bool = False
            elif your_turn_bool == True:
                your_turn_bool = False
                computer_turn_bool = True
        else:
            if computer_turn_bool == True:
                print("Computer's turn...")
                computer_move = computer_turn_coord(random.randint(0, len(coord) - 1))
                print(f"Computer chose: ({computer_move})")
                chosen_coord = computer_move
                while chosen_coord in lst_coord:
                    computer_move = computer_turn_coord(random.randint(0, len(coord) - 1))
                    chosen_coord = computer_move
                lst_coord.append(chosen_coord)
                computer_turn_bool = True
                your_turn_bool = False
                    
            elif your_turn_bool == True:
                x_coord_my_move = int(input("Put your x coordinate: "))
                y_coord_my_move = int(input("Put your y coordinate: "))
                my_move = your_turn_coord(x_coord_my_move, y_coord_my_move)
                chosen_coord = my_move
                while chosen_coord in lst_coord:
                    print("Choose another coordinate:")
                    x_coord_my_move = int(input("Put your x coordinate: "))
                    y_coord_my_move = int(input("Put your y coordinate: "))
                    my_move = your_turn_coord(x_coord_my_move, y_coord_my_move)
                    chosen_coord = my_move
                lst_coord.append(chosen_coord)
                your_turn_bool = True
                computer_turn_bool = False
            for m in range(3):
                for j in range(3):
                    if your_turn_bool == True and (m, j) == my_move:
                        board[m][j] = user_symbol
                        if check_win(user_symbol):
                            print("You won!")
                            break
                        elif check_win(computer_symbol):
                            print("Computer won!")
                            break
                        index1 = coord.index(chosen_coord)
                        coord.pop(index1)
                    elif computer_turn_bool == True and (m, j) == computer_move:
                        board[m][j] = computer_symbol
                        if check_win(user_symbol):
                            break
                        elif check_win(computer_symbol):
                            break
                        index1 = coord.index(chosen_coord)
                        coord.pop(index1)
                if check_win(user_symbol):
                    break
                elif check_win(computer_symbol):
                    break

            print_board()
            print(coord)
            if check_win(user_symbol):
                break
            elif check_win(computer_symbol):
                break
            if computer_turn_bool == True:
                your_turn_bool = True
                computer_turn_bool = False
            elif your_turn_bool == True:
                your_turn_bool = False
                computer_turn_bool = True
                
user_symbol, computer_symbol = choose_symbols()
game()
