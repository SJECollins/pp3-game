"""
Hangman, why not
"""
import pyfiglet
import re
import requests
from helpers.helpers import clear_terminal, slowprint, get_input, Colours


THE_MAN = [
                            r"""
                                ##=======#
                                ||       ¦
                                ||
                                ||
                                ||
                                ||
                                ||
                            [][][][][]
                            """,
                            r"""
                                ##=======#
                                ||       ¦
                                ||       O
                                ||
                                ||
                                ||
                                ||
                            [][][][][]
                            """,
                            r"""
                                ##=======#
                                ||       ¦
                                ||       O
                                ||       |
                                ||
                                ||
                                ||
                            [][][][][]
                            """,
                            r"""
                                ##=======#
                                ||       ¦
                                ||       O
                                ||      /|
                                ||
                                ||
                                ||
                            [][][][][]
                            """,
                            r"""
                                ##=======#
                                ||       ¦
                                ||       O
                                ||      /|\
                                ||
                                ||
                                ||
                            [][][][][]
                            """,
                            r"""
                                ##=======#
                                ||       ¦
                                ||       O
                                ||      /|\
                                ||      /
                                ||
                                ||
                            [][][][][]
                            """,
                            r"""
                                ##=======#
                                ||       ¦
                                ||       O
                                ||      /|\
                                ||      / \
                                ||
                                ||
                            [][][][][]
                            """,
]


GAME_VARS = {
    "word": "",
    "guesses": "",
    "correct": 0,
    "lives": 7,
    "won": False
}


def get_word():
    """
    Using random-word-api.herokuapp.com
    """
    response = requests.get(
        "https://random-word-api.herokuapp.com/word",
        timeout=5
    )
    if response.status_code == 200:
        GAME_VARS["word"] = re.sub(r"\W+", "", response.text)
        if len(GAME_VARS["word"]) > 10:
            get_word()
    else:
        print("Error: ", response.status_code, response.text)


def get_guess():
    while True:
        user_guess = get_input("Guess a letter: ")
        if user_guess == "quit":
            break
        elif user_guess.isnumeric():
            print("Words are made up of letters...")
        elif len(user_guess) > 1:
            print("Ah ah ah! One letter at a time!")
        elif user_guess in GAME_VARS["guesses"]:
            print("You guessed that one already.")
        elif user_guess == "":
            print("Try entering something...")
        else:
            check_guess(user_guess)
            break
    check_win()


def check_guess(guess):
    GAME_VARS["guesses"] += guess
    if guess in GAME_VARS["word"]:
        GAME_VARS["correct"] += 1
        print("{:>40}".format(f"Correct! {guess} is in the word!"))
    else:
        GAME_VARS["lives"] -= 1
        print("{:>40}".format(f"Wrong! {guess} is not in the word!"))


def print_word(guess):
    print("{:>34}".format("The word: "), end="")
    for letter in GAME_VARS["word"]:
        if letter in guess:
            print(letter, end="")
        else:
            print("_", end="")
    print("")
    print("{:>38}".format("Your guesses: "), guess)


def print_hangman():
    """
    Print the man!
    """
    print(THE_MAN[(len(THE_MAN) - GAME_VARS["lives"])])


def check_win():
    GAME_VARS["won"] = all(item in GAME_VARS["guesses"]
                           for item in GAME_VARS["word"])


def end_game():
    if GAME_VARS["lives"] == 1:
        slowprint("Uh oh... \n")
    else:
        slowprint("You did it! You saved him!")
    print("The word was: ", GAME_VARS["word"])
    while True:
        user_choice = get_input("Do you want to play again? Yes or no: ")
        if user_choice not in ("yes", "no"):
            print("Please enter a real choice.")
        elif user_choice in ("yes", "y"):
            clear_terminal()
            main()
        else:
            break


def main():
    GAME_VARS["word"] = ""
    GAME_VARS["guesses"] = ""
    GAME_VARS["correct"] = 0
    GAME_VARS["lives"] = 7
    GAME_VARS["won"] = False

    get_word()
    print_hangman()
    print_word(GAME_VARS["guesses"])

    while GAME_VARS["lives"] > 1 and not GAME_VARS["won"]:
        get_guess()
        clear_terminal()
        print_hangman()
        print_word(GAME_VARS["guesses"])

    end_game()


def intro():
    slowprint("Let's play \n")
    title = pyfiglet.figlet_format("HANGMAN", font="small")
    print(f"{Colours.RED}" + title + f"{Colours.END}")
    slowprint("Guess one letter at a time.\nSave the man.")
    main()
