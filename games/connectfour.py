"""
Connect 4 is basically just bigger tic tac toe, right?
"""
import pyfiglet
from random import randint
from helpers.helpers import Colours, get_input, slowprint, clear_terminal

player_one = f"{Colours.YELLOW}\u2B24{Colours.END}"
player_two = f"{Colours.RED}\u2B24{Colours.END}"
space = f"{Colours.GREY}\u2B24{Colours.END}"
bar = f"{Colours.BLUE}|{Colours.END}"


def print_board(board):
    ends = "{:^79}".format(f"{Colours.BLUE}#=============#{Colours.END}")
    mids = "{:^79}".format(f"{Colours.BLUE}|=============|{Colours.END}")
    print("{:^70}".format("1 2 3 4 5 6 7"))
    print(ends)
    num = 1
    for row in board:
        print("{:^75}".format(f"%d {bar}%s{bar}")
              % (num, f"{bar}".join(row)))
        if num < 6:
            print(mids)
        num += 1
    print(ends)


def get_user_move(board):
    while True:
        while True:
            col = get_input("Enter the column number: ")
            if col not in ("1", "2", "3", "4", "5", "6", "7"):
                print("Please enter a valid number.")
            else:
                break
        user_col = int(col) - 1

        for row in range(6):
            if board[row][user_col] == space:
                user_row = row

        move = user_row, user_col
        if board[user_row][user_col] == space:
            return move
        print("That's already taken.")


def get_comp_move(board, comp):
    comp_col = 0
    comp_row = 0
    target = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == comp:
                # Check below, go above
                if (row > 0 and board[row - 1][col] == space):
                    target = True
                    comp_col = col
                    break
                # Check right, go left
                if (0 < col < 6 and board[row][col + 1] == comp
                        and board[row][col - 1] == space):
                    if (row == 5) or (row > 0
                                      and board[row + 1][col - 1] != space):
                        target = True
                        comp_col = col - 1
                        break
                # Go left
                if (col > 0 and board[row][col - 1] == space):
                    if (row == 5) or (row > 0
                                      and board[row + 1][col - 1] == space):
                        target = True
                        comp_col = col - 1
                        break
                # Go right
                if (col < 6 and board[row][col + 1] == space):
                    if (row == 5) or (row > 0
                                      and board[row + 1][col + 1] != space):
                        target = True
                        comp_col = col + 1
                        break
                # Check below left, go above right
                if (0 < row < 5 and 0 < col < 6
                        and board[row + 1][col - 1] == comp
                        and board[row][col + 1] != space
                        and board[row - 1][col + 1] == space):
                    target = True
                    comp_col = col + 1
                    break
                # Check below right, go above left
                if (0 < row < 5 and 0 < col < 6
                        and board[row + 1][col + 1] == comp
                        and board[row][col - 1] != space
                        and board[row - 1][col - 1] == space):
                    target = True
                    comp_col = col - 1
                    break
                # Go below left
                if (0 <= row < 4 and 0 < col < 6
                        and board[row + 1][col - 1] == space
                        and board[row + 2][col - 1] != space):
                    target = True
                    comp_col = col - 1
                    break
                # Go below right
                if (0 <= row < 4 and 0 < col < 6
                        and board[row + 1][col + 1] == space
                        and board[row + 2][col - 1] != space):
                    target = True
                    comp_col = col + 1
                    break

        if target:
            row = 5
            while (row >= 0):
                if board[row][comp_col] == space:
                    comp_row = row
                    move = comp_row, comp_col
                    return move
                row -= 1
    if not target:
        while True:
            comp_col = randint(0, 6)
            row = 5
            while (row >= 0):
                if board[row][comp_col] == space:
                    comp_row = row
                    move = comp_row, comp_col
                    return move
                row -= 1


def check_win(board, player):
    for col in range(4):
        for row in range(6):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2]
                    == board[row][col + 3] == player):
                return True
    for col in range(7):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col]
                    == board[row + 3][col] == player):
                return True
    for col in range(4):
        for row in range(3):
            if (board[row][col] == board[row + 1][col + 1]
                    == board[row + 2][col + 2] == board[row + 3][col + 3]
                    == player):
                return True
    for col in range(4):
        for row in range(6):
            if (board[row][col] == board[row - 1][col + 1]
                    == board[row - 2][col + 2] == board[row - 3][col + 3]
                    == player):
                return True


def is_full(board):
    for row in board:
        for col in row:
            if col == space:
                return False
    return True


def end_game(winner):
    if winner == "human":
        print("You won!")
    elif winner == "comp":
        print("The computer won!")
    elif winner == "none":
        print("It's a tie!")
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
    title = pyfiglet.figlet_format(("Connect4").center(40), font="small")
    slowprint("Welcome to\n")
    print(f"{Colours.BLUE}" + title + f"{Colours.END}")
    main()


def main():
    BOARD = [[space] * 7 for x in range(6)]
    print_board(BOARD)

    while True:
        choose_turn = get_input("Do you want to play first or second? ")
        if choose_turn not in ("first", "second"):
            print("Please choose first or second.")
        else:
            break

    if choose_turn == "first":
        human = player_one
        comp = player_two
    else:
        human = player_two
        comp = player_one

    while (not is_full(BOARD) and not check_win(BOARD, human)
            and not check_win(BOARD, comp)):
        if human == player_one:
            slowprint("Your turn... \n")
            row, col = get_user_move(BOARD)
            BOARD[row][col] = human
            clear_terminal()
            print_board(BOARD)
            if (is_full(BOARD) or check_win(BOARD, human)
                    or check_win(BOARD, comp)):
                break
            slowprint("Computer's turn... \n")
            row, col = get_comp_move(BOARD, comp)
            BOARD[row][col] = comp
        else:
            slowprint("Computer's turn... \n")
            row, col = get_comp_move(BOARD, comp)
            BOARD[row][col] = comp
            clear_terminal()
            print_board(BOARD)
            if (is_full(BOARD) or check_win(BOARD, comp)
                    or check_win(BOARD, human)):
                break
            slowprint("Your turn... \n")
            row, col = get_user_move(BOARD)
            BOARD[row][col] = human
        clear_terminal()
        print_board(BOARD)

    if check_win(BOARD, human):
        end_game(winner="human")
    elif check_win(BOARD, comp):
        end_game(winner="comp")
    elif is_full(BOARD):
        end_game(winner="none")
