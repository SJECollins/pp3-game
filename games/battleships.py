"""
Battleships vs computer
"""

from random import randint

COMP_BOARD = [[" "] * 10 for x in range(10)]
USER_BOARD = [[" "] * 10 for y in range(10)]

COMP_SHIPS = []
USER_SHIPS = []

USER_MOVES = []
COMP_MOVES = []


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


def get_user_move():
    guess = ()
    player = True
    print(f"The enemy has {len(COMP_SHIPS)} battleships remaining.", end=" ")
    print(f"You have {len(USER_SHIPS)} battleships remaining.")
    print("Enter the coordinates for your missile below!")

    while True:
        while True:
            row_num = input("Enter row number: ").strip()
            if row_num not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                print("Please enter a valid row number.")
            else:
                row = int(row_num)
                guess = guess + (row, )
                break
        while True:
            col = input("Enter column letter: ").strip().lower()
            if col not in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"):
                print("Please enter a valid column letter.")
            else:
                guess = guess + (col, )
                break
        if guess not in USER_MOVES:
            USER_MOVES.append(guess)
            break
        else:
            guess = ()
            print("You already tried that!")

    check_hit(guess, COMP_SHIPS, COMP_BOARD, player)


def get_comp_move():
    move = ()
    player = False
    while True:
        row = randint(1, 10)
        move = move + (row, )
        col_num = randint(1, 10)
        col = chr(col_num + 96)
        move = move + (col, )
        if move not in COMP_MOVES:
            break
            
    check_hit(move, USER_SHIPS, USER_BOARD, player)


def check_hit(move, ships, board, player):
    hit = False
    for ship in ships:
        if move in ship:
            hit = True
            if len(ship) == 1:
                ships.remove(ship)
                if player:
                    print("You sunk a battleship!")
                else:
                    print("You lost a battleship!")
            else:
                ship.remove(move)
    row = move[0] - 1
    col_letter = move[1]
    col = ord(col_letter) - 97

    if player:
        print("Your guess: ", move)
    else:
        print("Enemy move: ", move)
    if hit:
        board[row][col] = "X"
        print("Hit!")
    else:
        board[row][col] = "O"
        print("Miss!")


def start_game():
    print("Welcome to Battleships!")
    print("When prompted, enter the row number, then column letter for the \
          coordinates you wish to attack.")
    print("Destroy all 5 of your enemy's ships to win!")
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


def end_game():
    if len(USER_SHIPS) < len(COMP_SHIPS):
        print("You lose!")
    else:
        print("You sunk all their battleships!")


def main():
    start_game()
    while len(USER_SHIPS) > 0 and len(COMP_SHIPS) > 0:
        get_user_move()
        get_comp_move()
        print_boards()
    end_game()
