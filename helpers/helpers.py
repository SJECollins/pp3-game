import os
import sys
import time


def clear_terminal():
    os.system("clear")


def slowprint(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def get_input(message):
    user_input = input(message).strip().lower()
    return user_input
