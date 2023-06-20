"""
Main script.
Handle menu/game choice (in case we want more games)
"""

# Import pyfiglet for menu
import pyfiglet

# Import game
from games import battleships, hangman


def run_game(choice):
    if choice == 1:
        battleships.intro()
    elif choice == 2:
        hangman.intro()
    menu()


def menu():
    welcome = pyfiglet.figlet_format("Pixel's Python Arcade", font="small")
    print("\x1b[32m" + welcome + "\x1b[0m")
    print("Select a game from the list below: ")
    print("[1] Battleships")
    print("[2] Hangman")
    while True:
        user_choice = input(
            "Enter the number of the game you want to play: ").strip()
        if user_choice not in ("1", "2", "3"):
            print("Please enter a valid number.")
        else:
            choice = int(user_choice)
            run_game(choice)
            break


menu()
