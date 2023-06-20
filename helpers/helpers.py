import os
import sys
import time


def clear_terminal():
    """
    Function to clear terminal
    """
    os.system("clear")


def slowprint(message):
    """
    Function to slowly print to terminal

    Args:
        message - message to print to screen with delay between letters
    """
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def get_input(message):
    user_input = input(message).strip().lower()
    return user_input


class Colours():
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    GREY = "\033[37m"
    PURPLE = "\033[35m"
    GREEN = "\033[32m"
    END = "\033[0m"
