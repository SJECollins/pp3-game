"""
Maybe some tic tac toe??
"""


def print_board(board):
    ends = "{:^79}".format("     +-+-+-+")
    print("{:^79}".format("     1 2 3"))
    print(ends)
    num = 1
    for row in board:
        print("{:^79}".format("%d |%s|") % (num, "|".join(row)))
        print(ends)
        num += 1


def main():
    BOARD = [[" "] * 3 for x in range(3)]
    print_board(BOARD)

