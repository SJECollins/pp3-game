"""
Connect 4 is basically just bigger tic tac toe, right?
"""
from random import randint
from helpers.helpers import Colours, get_input

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
    print("comp")
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
                    print("above")
                    break
                # Check right, go left
                if (0 < col < 6 and board[row][col + 1] == comp
                        and board[row][col - 1] == space):
                    if (row == 5) or (row > 0 and board[row + 1][col - 1] != space):
                        target = True
                        comp_col = col - 1
                        print("left")
                        break
                # Go left
                if (col > 0 and board[row][col - 1] == space):
                    if (row == 5) or (row > 0 and board[row + 1][col - 1] == space):
                        target = True
                        comp_col = col - 1
                        print("left")
                        break
                # Go right
                if (col < 6 and board[row][col + 1] == space):
                    if (row == 5) or (row > 0 and board[row + 1][col + 1] != space):
                        target = True
                        comp_col = col + 1
                        print("right")
                        break
                # Check below left, go above right
                if (0 < row < 5 and 0 < col < 6 and board[row + 1][col - 1] == comp
                        and board[row][col + 1] != space
                        and board[row - 1][col + 1] == space):
                    target = True
                    comp_col = col + 1
                    print("above right")
                    break
                # Check below right, go above left
                if (0 < row < 5 and 0 < col < 6 and board[row + 1][col + 1] == comp
                        and board[row][col - 1] != space
                        and board[row - 1][col - 1] == space):
                    target = True
                    comp_col = col - 1
                    print("above left")
                    break
                # Go below left
                if (0 <= row < 4 and 0 < col < 6 and board[row + 1][col - 1] == space
                        and board[row + 2][col - 1] != space):
                    target = True
                    comp_col = col - 1
                    print("below left")
                    break
                # Go below right
                if (0 <= row < 4 and 0 < col < 6 and board[row + 1][col + 1] == space
                        and board[row + 2][col - 1] != space):
                    target = True
                    comp_col = col + 1
                    print("Below right")
                    break
                
        if target:
            row = 5
            while (row >= 0):
                if board[row][comp_col] == space:
                    comp_row = row
                    move = comp_row, comp_col
                    return move
                row -= 1
        print("end of loop?")
    if not target:
        print("get random")
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
        for row in range(3):
            if (board[row][col] == board[row - 1][col + 1]
                    == board[row - 2][col + 2] == board[row - 3][col + 3]
                    == player):
                return True


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

    while not check_win(BOARD, human):
        if human == player_one:
            row, col = get_user_move(BOARD)
            BOARD[row][col] = human
            print_board(BOARD)
            row, col = get_comp_move(BOARD, comp)
            BOARD[row][col] = comp
        else:
            row, col = get_comp_move(BOARD, comp)
            BOARD[row][col] = comp
            row, col = get_user_move(BOARD)
            BOARD[row][col]
        print_board(BOARD)

