"""
Battleships vs computer
"""

from random import randint

COMP_BOARD = [[" "] * 10 for x in range(10)]
USER_BOARD = [[" "] * 10 for y in range(10)]

COMP_SHIPS = []
USER_SHIPS = []


def print_player(board):
    print("             PLAYER", end="")
    yield
    print("      A B C D E F G H I J", end="")
    yield
    ends = "    #===================#"
    print(ends, end="")
    yield
    num = 1
    for row in board:
        if num != 10:
            print("%d   |%s|" % (num, "|".join(row)), end="")
            yield
        else:
            print("%d  |%s|" % (num, "|".join(row)), end="")
            yield
        num += 1
    print(ends, end="")
    yield


def print_comp(board):
    print("      COMPUTER     ", end="")
    yield
    print(" A B C D E F G H I J", end="")
    yield
    ends = "#===================#"
    print(ends, end="")
    yield
    for row in board:
        print("|%s|" % ("|".join(row)), end="")
        yield
    print(ends, end="")
    yield


def print_boards():
    board_one, board_two = print_comp(COMP_BOARD), print_player(USER_BOARD)
    while True:
        try:
            next(board_one)
            print("    ", end="")
            next(board_two)
            print()
        except StopIteration:
            break


def start_game():
    print_boards()


def main():
    start_game()
