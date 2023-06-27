"""
Maybe some tic tac toe??
"""
import pyfiglet
from random import randint
from helpers.helpers import Colours, get_input, slowprint, clear_terminal

nought = f"{Colours.YELLOW}O{Colours.END}"
cross = f"{Colours.RED}X{Colours.END}"


def print_board(board):
    ends = "{:^79}".format("     +-+-+-+")
    print("{:^79}".format("     1 2 3"))
    print(ends)
    num = 1
    for row in board:
        print("{:^79}".format("%d |%s|") % (num, "|".join(row)))
        print(ends)
        num += 1


def get_user_move(board):
    while True:
        while True:
            user_row = get_input("Enter the row number: ")
            if user_row not in ("1", "2", "3"):
                print("Enter a valid number.")
            else:
                break
        row = int(user_row) - 1
        while True:
            user_col = get_input("Enter a column number: ")
            if user_col not in ("1", "2", "3"):
                print("Enter a valid number.")
            else:
                break
        col = int(user_col) - 1
        user_move = row, col
        if board[row][col] == " ":
            return user_move
        print("That's already taken.")


def get_comp_move(board, comp):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                if check_win(board, comp):
                    return row, col
                board[row][col] = " "
    other_player = cross if comp == nought else nought
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = other_player
                if check_win(board, other_player):
                    board[row][col] = comp
                    return row, col
                board[row][col] = " "
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if board[row][col] == " ":
            return row, col


def check_win(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player
            or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False


def is_full(board):
    for row in board:
        for col in row:
            if col == " ":
                return False
    return True


def end_game(winner):
    if winner == "human":
        slowprint("You won!\n")
    elif winner == "comp":
        slowprint("The computer won!\n")
    elif winner == "none":
        slowprint("It's a tie!\n")
    while True:
        play_again = get_input("Play again? Yes or no: ")
        if play_again in ("yes", "y"):
            return main()
        elif play_again == "no":
            break
        else:
            print("Please choose yes or no.")


def intro():
    clear_terminal()
    title = pyfiglet.figlet_format(("Tic Tac Toe!").center(40), font="small")
    slowprint("Welcome to\n")
    print(f"{Colours.PURPLE}" + title + f"{Colours.END}")
    main()


def main():
    BOARD = [[" "] * 3 for x in range(3)]
    print_board(BOARD)

    while True:
        choose_move = get_input("Do you want to move first or second? ")
        if choose_move not in ("first", "second"):
            print("Please choose first or second.")
        else:
            break

    if choose_move == "first":
        human = cross
        comp = nought
    else:
        human = nought
        comp = cross

    while not is_full(BOARD) and not check_win(BOARD, human):
        if human == cross:
            row, col = get_user_move(BOARD)
            BOARD[row][col] = human
            if is_full(BOARD):
                break
            print_board(BOARD)
            slowprint("Computer's turn... \n")
            row, col = get_comp_move(BOARD, comp)
            BOARD[row][col] = comp
        else:
            slowprint("Computer's turn... \n")
            row, col = get_comp_move(BOARD, comp)
            BOARD[row][col] = comp
            if is_full(BOARD):
                break
            slowprint("Your turn... \n")
            row, col = get_user_move(BOARD)
            BOARD[row][col]
        clear_terminal()
        print_board(BOARD)

    if check_win(BOARD, human):
        end_game(winner="human")
    elif check_win(BOARD, comp):
        end_game(winner="comp")
    elif is_full(BOARD):
        end_game(winner="none")
