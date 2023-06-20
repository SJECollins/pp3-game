"""
Battleships vs computer
"""

from random import randint


class Style():
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    GREY = "\033[37m"
    PURPLE = "\033[35m"
    END = "\033[0m"


sea_icon = f"{Style.BLUE}~{Style.END}"
boat_icon = f"{Style.GREY}B{Style.END}"
hit_icon = f"{Style.YELLOW}H{Style.END}"
sunk_icon = f"{Style.RED}X{Style.END}"
miss_icon = f"{Style.PURPLE}M{Style.END}"


COMP_BOARD = [[sea_icon] * 10 for x in range(10)]
USER_BOARD = [[sea_icon] * 10 for y in range(10)]

COMP_SHIPS = []
USER_SHIPS = []

USER_MOVES = []
COMP_MOVES = []


def print_player(board):
    print("{:^40}".format("PLAYER"), end="")
    yield
    print("{:^40}".format("A B C D E F G H I J"), end="")
    yield
    ends = "{:^40}".format("#===================#")
    print(ends, end="")
    yield
    num = 1
    for row in board:
        if num != 10:
            print("%d           |%s|" % (num, "|".join(row)), end="")
            yield
        else:
            print("%d          |%s|" % (num, "|".join(row)), end="")
            yield
        num += 1
    print(ends, end="")
    yield


def print_comp(board):
    print("{:^40}".format("COMPUTER"), end="")
    yield
    print("{:^40}".format("A B C D E F G H I J"), end="")
    yield
    ends = "{:^40}".format("#===================#")
    print(ends, end="")
    yield
    for row in board:
        print("{:^20}".format("  |%s|") % ("|".join(row)), end="")
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
                USER_BOARD[row][col] = boat_icon
        else:
            COMP_SHIPS.append(coordinates)


def get_user_ship_position(board, user_sizes):
    row_nums = []
    col_nums = []
    col_letters = []
    for ship in user_sizes:
        placed = False
        while not placed:
            print(f"Placing a ship {ship} cells long.")
            print_boards()
            while True:
                direction = input("Enter orientation - 'H' for horizontal "
                                  "or 'V' for vertical: ").strip().lower()
                if direction in ("h", "v"):
                    break
                else:
                    print("Please enter a valid orientation.")
            while True:
                row = input("Enter the row number for the first cell of "
                            "the ship: ").strip()
                if row in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                    row_num = int(row) - 1
                    break
                else:
                    print("Please enter a valid row number.")
            while True:
                col = input("Enter the column letter for the first cell "
                            "of the ship: ").strip().lower()
                if col in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"):
                    col_num = ord(col) - 97
                    break
                else:
                    print("Please enter a valid column letter.")
            if direction == "h":
                if col_num + ship < 11:
                    row_nums = [row_num] * ship
                    col_nums = list(range(col_num, col_num + ship))
                    for col in col_nums:
                        if board[row_num][col] == boat_icon:
                            print("There is already a ship in that position.")
                        else:
                            board[row_num][col] = boat_icon
                            placed = True
                else:
                    print("The ship does not fit in those coordinates."
                          "Please enter a valid position for the ship.")
            else:
                if row_num + ship < 11:
                    row_nums = list(range(row_num, row_num + ship))
                    col_nums = [col_num] * ship
                    for row in row_nums:
                        if board[row][col_num] == boat_icon:
                            print("There is already a ship in that position.")
                        else:
                            board[row][col_num] = boat_icon
                            placed = True
                else:
                    print("The ship does not fit in those coordinates."
                          "Please enter a valid position for the ship.")
        for col in col_nums:
            col_letter = chr(col + 96)
            col_letters.append(col_letter)
        coordinates = list(zip(row_nums, col_letters))
        USER_SHIPS.append(coordinates)


def get_user_move():
    guess = ()
    player = True
    print(f"The enemy has {len(COMP_SHIPS)} battleships remaining.", end=" ")
    print(f"You have {len(USER_SHIPS)} battleships remaining.")
    print("Enter the coordinates for your missile below!")

    while True:
        while True:
            row_num = input("Enter row number: ").strip()
            if row_num not in (
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
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


def get_comp_move(board):
    move = ()
    player = False
    target = False
    row_num = 0
    col_num = 0
    while True:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == hit_icon:
                    if row < 8 and board[row + 1][col] == hit_icon:
                        if (row > 0 and board[row - 1][col] in (
                                sea_icon, boat_icon)):
                            row_num = row
                            col_num = col + 1
                            target = True
                            print("Target above")
                        break
                    elif col < 8 and board[row][col + 1] == hit_icon:
                        if (col > 0 and board[row][col - 1] in (
                                sea_icon, boat_icon)):
                            row_num = row + 1
                            col_num = col
                            target = True
                            print("Target left")
                            break
                        continue
                    if (row > 0 and board[row - 1][col] in (
                            sea_icon, boat_icon)):
                        row_num = row
                        col_num = col + 1
                        target = True
                        print("Target above")
                        break
                    elif (row < 8 and board[row + 1][col] in (
                            sea_icon, boat_icon)):
                        row_num = row + 2
                        col_num = col + 1
                        target = True
                        print("Target below")
                        break
                    elif (col > 0 and board[row][col - 1] in (
                            sea_icon, boat_icon)):
                        row_num = row + 1
                        col_num = col
                        target = True
                        print("Target left")
                        break
                    elif (col < 8 and board[row][col + 1] in (
                            sea_icon, boat_icon)):
                        row_num = row + 1
                        col_num = col + 2
                        target = True
                        print("Target right")
                        break
                    else:
                        continue
            if target:
                break

        if not target:
            row_num = randint(1, 10)
            col_num = randint(1, 10)

        move = move + (row_num, )
        col = chr(col_num + 96)
        move = move + (col, )
        if move in COMP_MOVES:
            move = ()
        else:
            break
    COMP_MOVES.append(move)
    check_hit(move, USER_SHIPS, board, player)


def check_hit(move, ships, board, player):
    hit = False
    sunk = False

    for ship in ships:
        if move in ship:
            hit = True
            if len(ship) == 1:
                ships.remove(ship)
                sunk = True
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
        board[row][col] = hit_icon
        print("Hit!")
    else:
        board[row][col] = miss_icon
        print("Miss!")

    if sunk:
        sink_ships(board)


def sink_ships(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == hit_icon:
                board[row][col] = sunk_icon


def start_game():
    print("Welcome to Battleships!")
    print("When prompted, enter the row number, then column letter for the "
          "coordinates you wish to attack.")
    print("Destroy all 5 of your enemy's ships to win!")
    user_sizes = [2, 3, 3, 4, 5]
    comp_sizes = [2, 3, 3, 4, 5]

    print("You may choose to place your ships or they will be randomly placed "
          "on the board for you.")
    user_placing = input("Place your own ships? yes or no: ").strip().lower()

    while len(COMP_SHIPS) < 5:
        ship = comp_sizes.pop(0)
        is_player = False
        add_ships(ship, COMP_SHIPS, is_player)

    if user_placing in ("yes", "y"):
        get_user_ship_position(USER_BOARD, user_sizes)
    else:
        while len(USER_SHIPS) < 5:
            ship = user_sizes.pop(0)
            is_player = True
            add_ships(ship, USER_SHIPS, is_player)

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
        get_comp_move(USER_BOARD)
        print_boards()
    end_game()
