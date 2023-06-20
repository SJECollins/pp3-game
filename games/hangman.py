"""
Hangman, why not
"""
import pyfiglet
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


def print_hangman():
    """
    Print the man!
    """
    print(THE_MAN[(len(THE_MAN) - GAME_VARS["lives"])])


def main():
    GAME_VARS["word"] = ""
    GAME_VARS["guesses"] = ""
    GAME_VARS["correct"] = 0
    GAME_VARS["lives"] = 7
    GAME_VARS["win"] = False

    print_hangman()


def intro():
    slowprint("Let's play \n")
    title = pyfiglet.figlet_format("HANGMAN", font="small")
    print(f"{Colours.RED}" + title + f"{Colours.END}")
    slowprint("Guess one letter at a time.\nSave the man.")
    main()
