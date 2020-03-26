import random
import copy
import time
import pyllist

current_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

num_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # for reference


turn = 1  # TODO


def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print


def check_win(board):
    return check_win_vertical(board) or check_win_horizontal(board) or check_win_diagonal(board)


def check_win_horizontal(board):
    for i in [0, 3, 6]:
        if board[i] == 'X' and board[i + 1] == 'X' and board[i + 2] == 'X':
            return True
        if board[i] == 'O' and board[i + 1] == 'O' and board[i + 2] == 'O':
            return True
    return False


def check_win_vertical(board):
    for i in [0, 1, 2]:
        if board[i] == 'X' and board[i + 3] == 'X' and board[i + 6] == 'X':
            return True
        if board[i] == 'O' and board[i + 3] == 'O' and board[i + 6] == 'O':
            return True
    return False


def check_win_diagonal(board):
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return True
    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return True
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return True
    if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return True
    return False


def board_full(board):  # checks if the board is full (helps check_draw)
    for i in range(0, 9):
        if board[i] == "-":
            return False
    return True


def check_draw(board):
    if board_full(board) and check_win(board) != True:
        return True
    return False


def place_maker(player, square, board):
    if player == 1:  # place the marker on board
        board[square] = 'X'
    else:
        board[square] = 'O'


def player_turn(player):  # takes in which player and places a marker on board
    square = input("player " + str(player) + " choose a square 1-9: ")  # input TODO fix this message
    square = square - 1  # array starts at 0
    if not isinstance(square, int) or square > 8 or square < 0:  # check input is valid
        print("input not an int between 1 and 9")
        player_turn(player)
        return
    if not legal_move(square, current_board):  # check move is legal
        print("square already taken!")
        player_turn(player)
        return
    place_maker(player, square, current_board)


def legal_move(square, board):
    if board[square] == "X" or board[square] == "O":  # square is taken
        return False
    return True


def random_square():
    return random.randint(0, 8)


def computer_random_turn(player):
    square = random_square()
    if current_board[square] == "X" or current_board[square] == "O":  # check square isn't taken
        computer_random_turn(player)  # try again if it is
        return
    place_maker(player, square, current_board)


def computer_smart_turn(player):
    # check if any moves win and play those TODO: clean this up ...
    for i in range(0, 9):
        if not legal_move(i, current_board):  # check if it is legal
            continue
        board_copy = copy.deepcopy(current_board)  # copy board fresh each time
        place_maker(player, i, board_copy)
        if check_win(board_copy):
            place_maker(player, i, current_board)
            return
    # check if the opponent can play any moves that win and block those
    for i in range(0, 9):
        if not legal_move(i, current_board):  # check if it is legal
            continue
        board_copy = copy.deepcopy(current_board)  # copy board fresh each time
        place_maker(change_turn(player), i, board_copy)
        if check_win(board_copy):
            place_maker(player, i, current_board)
            return
    # find available squares
    corners = pyllist.sllist()  # list all available corner spaces (to choose randomly from)
    edges = pyllist.sllist()  # list all available edge spaces (to choose randomly from)
    for i in range(0, 9):
        if not legal_move(i, current_board):
            continue
        if i == 4:  # middle
            place_maker(player, 4, current_board)
            return
        if i == 0 or i == 2 or i == 6 or i == 8:  # corners
            corners.append(i)
        if i == 1 or i == 3 or i == 5 or i == 7:  # edges
            edges.append(i)
    # TODO
    if corners.size != 0:
        square = random.choice(corners)
    else:
        square = random.choice(edges)
    place_maker(player, square, current_board)
    return


def change_turn(player):  # changes 1 to 2 or vise versa
    if player == 1:
        return 2
    else:
        return 1


def two_player_game():
    player = 1
    print_board(num_board)  # gives player reference of squares
    while 1 > 0:
        player_turn(player)
        print_board(current_board)
        if check_draw(current_board):
            print "draw"
            break
        if check_win(current_board):
            print "player " + str(player) + " wins!"
            break
        player = change_turn(player)  # swap to other player


def computer_random_game(player_first=True):
    player = 1
    print_board(num_board)  # gives player reference of squares
    if player_first:
        while 1 > 0:
            player_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "draw"
                break
            if check_win(current_board):
                print "player " + str(player) + " wins!"
                break
            player = change_turn(player)
            print "Computer randomly plays:"
            computer_random_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "draw"
                break
            if check_win(current_board):
                print "Computer wins!"
                break
            player = change_turn(player)
    else:
        while 1 > 0:
            print "Computer randomly plays:"
            computer_random_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "draw"
                break
            if check_win(current_board):
                print "Computer wins!"
                break
            player = change_turn(player)
            player_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "draw"
                break
            if check_win(current_board):
                print "player " + str(player) + " wins!"
                break
            player = change_turn(player)


def computer_game(player_first=True):
    player = 1
    print_board(num_board)  # gives player reference of squares
    if player_first:
        while 1 > 0:
            player_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "tie"
                break
            if check_win(current_board):
                print "You win!"
                break
            player = change_turn(player)
            print "computer plays:"
            time.sleep(0.75)
            computer_smart_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "tie"
                break
            if check_win(current_board):
                print "Computer wins!"
                break
            player = change_turn(player)
    else:
        while 1 > 0:
            print "computer plays:"
            time.sleep(0.75)
            computer_smart_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "tie"
                break
            if check_win(current_board):
                print "Computer wins!"
                break
            player = change_turn(player)
            player_turn(player)
            print_board(current_board)
            if check_draw(current_board):
                print "tie"
                break
            if check_win(current_board):
                print "You win!"
                break
            player = change_turn(player)


# --------- NOTES ---------
# two_player_game() prompts a game between two humans
# computer_random_game(player_first) /
# computer_game(player_first) prompts a game between a user and the computer
#       player_first: boolean, True or False


computer_game(True)
