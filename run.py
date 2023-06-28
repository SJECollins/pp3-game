"""
Main script.
Handle menu/game choice (in case we want more games)
"""

# Import pyfiglet for menu
import pyfiglet

# Import game
from games import battleships, hangman, tictactoe, hideseek, connectfour, quiz


def run_game(choice):
    if choice == 1:
        battleships.intro()
    elif choice == 2:
        hangman.intro()
    elif choice == 3:
        tictactoe.intro()
    elif choice == 4:
        connectfour.intro()
    elif choice == 5:
        hideseek.main()
    elif choice == 6:
        quiz.intro()
    menu()


def menu():
    welcomeOne = pyfiglet.figlet_format(("Pixel's Python").center(40),
                                        font="small")
    welcomeTwo = pyfiglet.figlet_format(("Arcade").center(50), font="small")
    print("\x1b[32m" + welcomeOne + "\x1b[0m")
    print("\x1b[32m" + welcomeTwo + "\x1b[0m")
    print("Select a game from the list below: ")
    print("[1] Battleships")
    print("[2] Hangman")
    print("[3] Tic Tac Toe")
    print("[4] Connect 4")
    print("[5] Hide & Seek - a text adventure")
    print("[6] Pixel's Quiz")
    while True:
        user_choice = input(
            "\nEnter the number of the game you want to play: ").strip()
        if user_choice not in ("1", "2", "3", "4", "5", "6"):
            print("Please enter a valid number.")
        else:
            choice = int(user_choice)
            run_game(choice)
            break


menu()
