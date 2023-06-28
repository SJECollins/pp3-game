import requests
import random
import pyfiglet
from helpers.helpers import Colours, get_input, clear_terminal, slowprint

CATEGORIES = {"1": "general_knowledge",
              "2": "arts_and_literature",
              "3": "film_and_tv",
              "4": "music"}
DIFFICULTY = {"1": "easy",
              "2": "medium",
              "3": "hard"}
QUE_NUMS = {0: "One",
            1: "Two",
            2: "Three",
            3: "Four",
            4: "Five",
            5: "Six",
            6: "Seven",
            7: "Eight",
            8: "Nine",
            9: "Ten"}


def get_quiz(category, difficulty):
    response = requests.get(f"https://the-trivia-api.com/api/questions?\
categories={category}&limit=10&region=IE&difficulty={difficulty}")
    data = response.json()
    que_dict = data
    play_quiz(que_dict)


def play_quiz(que_dict):
    num_right = 0
    que_num = 0
    options = []
    while que_num < 10:
        clear_terminal()
        num_text = QUE_NUMS[que_num]
        rand_que = que_dict.pop(random.randrange(len(que_dict)))
        correct = rand_que["correctAnswer"]
        ans_list = rand_que["incorrectAnswers"]
        ans_list.append(correct)
        random.shuffle(ans_list)
        options = ans_list.copy()
        question = rand_que["question"]
        slowprint(f"Question Number {num_text}:\n")
        slowprint(f"{question}\n")
        ans_num = 1
        que_num += 1
        while len(ans_list) > 0:
            rand_ans = ans_list.pop(0)
            print(f"[{ans_num}] {rand_ans}")
            ans_num += 1
        while True:
            user_answer = get_input("Please enter the number of the right \
answer: ")
            if user_answer not in ("1", "2", "3", "4"):
                print("Please enter a valid number.")
            else:
                break
        answer = options[int(user_answer) - 1]
        if get_correct(correct, answer):
            slowprint(f"Correct! The answer was {correct}!")
            num_right += 1
        else:
            slowprint(f"Wrong! The answer was {correct}...")
    end_game(num_right, que_num)


def get_correct(correct, answer):
    if correct == answer:
        return True
    return False


def end_game(answers, questions):
    clear_terminal()
    slowprint(f"Congratulations! You got {answers} out of {questions}!\n")
    while True:
        choice = get_input("Play again? Yes or no: ")
        if choice in ("yes", "y"):
            main()
        elif choice in ("no", "n"):
            slowprint("Maybe another time...")
            break
        else:
            print("Please choose yes or no.")


def intro():
    clear_terminal()
    title = pyfiglet.figlet_format(("Pixel's Quiz").center(40), font="small")
    slowprint("Welcome to\n")
    print(f"{Colours.BLUE}" + title + f"{Colours.END}")
    slowprint("Choose your category and difficulty.\n"
              "Enter the number of the correct answer.\n"
              "Try to get ten right...")
    main()


def main():
    clear_terminal()
    print("Choose a category number: ")
    while True:
        cat = get_input("[1] General Knowledge \n\
[2] Arts & Literature \n\
[3] Film & TV \n\
[4] Music \n\
Enter your choice: ")
        if cat not in ("1", "2", "3", "4"):
            print("Please choose a number.")
        else:
            break
    while True:
        diff = get_input("[1] Easy\n[2] Medium\n[3] Hard\n\
Enter your choice: ")
        if diff not in ("1", "2", "3"):
            print("Please choose a number.")
        else:
            break
    category = CATEGORIES[cat]
    difficulty = DIFFICULTY[diff]
    get_quiz(category, difficulty)
