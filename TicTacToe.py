current_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

num_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # for reference


def print_board(x):
    print(x[0] + "|" + x[1] + "|" + x[2])
    print(x[3] + "|" + x[4] + "|" + x[5])
    print(x[6] + "|" + x[7] + "|" + x[8])


def check_win():
    return check_win_vertical() or check_win_horizontal() or check_win_diagonal()


def check_win_horizontal():
    for i in [0, 3, 6]:
        if current_board[i] == 'X' and current_board[i + 1] == 'X' and current_board[i + 2] == 'X':
            return True
        if current_board[i] == 'O' and current_board[i + 1] == 'O' and current_board[i + 2] == 'O':
            return True
    return False


def check_win_vertical():
    for i in [0, 1, 2]:
        if current_board[i] == 'X' and current_board[i + 3] == 'X' and current_board[i + 6] == 'X':
            return True
        if current_board[i] == 'O' and current_board[i + 3] == 'O' and current_board[i + 6] == 'O':
            return True
    return False


def check_win_diagonal():
    if current_board[0] == 'X' and current_board[4] == 'X' and current_board[8] == 'X':
        return True
    if current_board[2] == 'X' and current_board[4] == 'X' and current_board[6] == 'X':
        return True
    if current_board[0] == 'O' and current_board[4] == 'O' and current_board[8] == 'O':
        return True
    if current_board[2] == 'O' and current_board[4] == 'O' and current_board[6] == 'O':
        return True
    return False


def board_full():  # checks if the board is full (helps check_draw)
    for i in range(0, 9):
        if current_board[i] == "-":
            return False
    return True


def check_draw():
    if board_full() and check_win() != True:
        return True
    return False


def turn(player):  # takes in which player and places a marker on board
    square = input("player " + str(player) + ": choose a square 1-9: ")  # input
    square = square - 1  # array starts at 0
    if not isinstance(square, int) or square > 8 or square < 0:  # check input is valid
        print("input not an int between 1 and 9")
        turn(player)
        return
    if current_board[square] == "X" or current_board[square] == "O":  # check square isn't taken
        print("square already taken!")
        turn(player)
        return
    if player == 1:  # place the marker on board
        current_board[square] = 'X'
    else:
        current_board[square] = 'O'


def change_turn(player):  # changes 1 to 2 or vise versa
    if player == 1:
        return 2
    else:
        return 1


def play_game():
    player = 1
    print_board(num_board) # gives player reference of squares 
    while 1 > 0:
        turn(player)
        print_board(current_board)
        if check_draw():
            print "draw"
            break
        if check_win():
            print "player " + str(player) + " wins!"
            break
        player = change_turn(player) # swap to other player


play_game()
