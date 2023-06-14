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


def add_ships(ship, ships, is_player):
    start = randint(1, 10 - ship)
    direction = randint(0, 1)
    if direction == 0:
        col_letters = []
        row_nums = list(range(start, start + ship))
        col_nums = [randint(1, 10)] * ship
        for col in col_nums:
            col_letter = chr(col + 96)
            col_letters.append(col_letter)
        coordinates = list(zip(row_nums, col_letters))
        check_overlap(coordinates, ship, ships, is_player)
    else:
        col_letters = []
        col_list = list(range(start, start + ship))
        for col in col_list:
            col_letter = chr(col + 96)
            col_letters.append(col_letter)
        row = [randint(1, 10)] * ship
        coordinates = list(zip(row, col_letters))
        check_overlap(coordinates, ship, ships, is_player)


def check_overlap(coordinates, ship, ships, is_player):
    taken = False
    for coords in coordinates:
        if any(coords in ship_list for ship_list in ships):
            taken = True
            break
    if taken:
        return add_ships(ship, ships, is_player)
    else:
        if is_player:
            USER_SHIPS.append(coordinates)
            for coords in coordinates:
                row = coords[0] - 1
                col_letter = coords[1]
                col = ord(col_letter) - 97
                USER_BOARD[row][col] = "$"
        else:
            COMP_SHIPS.append(coordinates)
            for coords in coordinates:
                row = coords[0] - 1
                col_letter = coords[1]
                col = ord(col_letter) - 97
                COMP_BOARD[row][col] = "$"


def start_game():
    user_sizes = [2, 3, 3, 4, 5]
    comp_sizes = [2, 3, 3, 4, 5]

    while len(USER_SHIPS) < 5:
        ship = user_sizes.pop(0)
        is_player = True
        add_ships(ship, USER_SHIPS, is_player)

    while len(COMP_SHIPS) < 5:
        ship = comp_sizes.pop(0)
        is_player = False
        add_ships(ship, COMP_SHIPS, is_player)

    print_boards()


def main():
    start_game()
