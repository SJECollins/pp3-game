"""
Imports
"""
import time
import pyfiglet
from .hsimages import game_images
from helpers.helpers import clear_terminal, slowprint


# Variables and objects
GAME_VARS = {
    "username": "",
    "pick_ups": [],
    "window_closed": False,
    "door_open": False,
    "stool_out": False,
    "shadow_delayed": False,
}


def get_user_choice(message):
    """
    Function to take input from user and format

    Args:
        message: str - message to print to screen requesting user input

    Returns:
        str - user's input, converted to lowercase and stripped of spaces
    """
    user_choice = input("\n==================================================\
==============================\n" + message + "\n").strip().lower()
    if user_choice == "quit":
        main()
    return user_choice


def draw_image(title):
    """
    Print image function

    Args:
        title: str - title of image to print to screen

    Draws images, centered, from image dictionary in images.py
    Code from stack overflow, link in credits in readme
    """
    lines = game_images[title].splitlines()
    print("\n".join(line.center(80) for line in lines))


def main():
    """
    Start function.
    Displays the start screen. Prompts the user to press enter to begin.
    """
    clear_terminal()
    game_title = pyfiglet.figlet_format("\nHide & Seek", font="shadow",
                                        justify="center")
    print(game_title)
    subtitle_text = "A choose your own adventure game"
    subtitle = subtitle_text.center(80)
    slowprint(subtitle)
    input("\n\n\nPress Enter to begin")
    intro()


def intro():
    """
    Starting function. Updates username. Prompts user to begin story.
    User can choose to say no, which prints a disappointed message and game
    doesn't start
    """
    clear_terminal()
    GAME_VARS["username"] = input("What's your name? \n").strip().capitalize()
    if not GAME_VARS["username"]:
        GAME_VARS["username"] = "Stranger"
    while True:
        start_answer = input(f"\nHello, {GAME_VARS['username']}, do you want "
                             "to play a game? Yes or No\n").strip().lower()
        if start_answer == "yes":
            print("\nGreat. To play:\n"
                  "When given a choice, either type the letter of your choice"
                  " or the underlined\nkeyword in the terminal and press "
                  "enter.\n"
                  "Or, you can enter 'quit' to return to the title screen.")
            while True:
                user_choice = input("\nReady to start?\n"
                                    "[A] \033[4mYes\033[0m!\n"
                                    "[B] Actually, \033[4mno\033[0m, I don't "
                                    "think I want to play after all...\n")\
                    .strip().lower()
                if user_choice == "a" or user_choice == "yes":
                    clear_terminal()
                    start_room()
                elif user_choice == "b" or user_choice == "no":
                    slowprint(f"\nThat's too bad, {GAME_VARS['username']}...")
                    time.sleep(1)
                    clear_terminal()
                    main()
                elif user_choice == "quit":
                    clear_terminal()
                    main()
                else:
                    print("That's isn't an option...")
        elif start_answer == "no" or user_choice == "quit":
            slowprint(f"\nWell, alright {GAME_VARS['username']}. Maybe next "
                      "time...")
            time.sleep(1)
            clear_terminal()
            main()
        else:
            print("That isn't an option.")


def start_room():
    """
    Starting room. Choice to get up or go back to sleep
    """
    GAME_VARS["pick_ups"].clear()
    GAME_VARS["window_closed"] = False
    GAME_VARS["door_open"] = False
    GAME_VARS["stool_out"] = False
    GAME_VARS["shadow_delayed"] = False
    clear_terminal()
    draw_image("bed")
    slowprint("You slowly open your eyes to find yourself safely in your own "
              "bed. At first the\nroom seems pitch black, except for the light"
              " from the clock on your bedside\ntable. It reads: 02:00.\n"
              "Slowly, your eyes adjust to the darkness and you look around "
              "your quiet room.\nYou don't know why, but you feel wide awake "
              "and your heart is beating hard.\n")
    while True:
        user_choice = get_user_choice("Will you:\n"
                                      "[A] Get up and make a cup of \033[4mtea"
                                      "\033[0m.\n"
                                      "[B] Try to go back to \033[4msleep"
                                      "\033[0m.")
        if user_choice == "a" or user_choice == "tea":
            get_up()
            break
        elif user_choice == "b" or user_choice == "sleep":
            try_sleep()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def try_sleep():
    """
    Try to go back to sleep. Choice to get up or keep trying to sleep
    """
    clear_terminal()
    slowprint("You have to get up for school early in the morning. So, you "
              "roll over in your\nbed and pull the covers up over your head. "
              "After a few moments of silence, you\nhear a soft rustling.\n"
              "Very slowly, you peek out from under your covers. In the "
              "darkness, you spy the\nwindow open a crack. A light breeze is "
              "moving the curtains.\n")
    while True:
        user_choice = get_user_choice("It's chilly in your room, so you:\n"
                                      "[A] Get \033[4mup\033[0m.\n"
                                      "[B] Pull the blanket \033[4mtighter\033"
                                      "[0m and close your eyes.")
        if user_choice == "a" or user_choice == "up":
            get_up()
            break
        elif user_choice == "b" or user_choice == "tighter":
            blanket_tighter()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def blanket_tighter():
    """
    Blankets tighter. Final chance to get up
    """
    clear_terminal()
    slowprint("You pull the blanket back over your head and squeeze your eyes "
              "shut.\n"
              f"""'{GAME_VARS["username"]}'\n"""
              "You think you hear a voice softly calling your name. You're "
              "not sure where it's\ncoming from, or even if you really heard "
              "it.\n")
    while True:
        user_choice = get_user_choice("You decide to:\n"
                                      "[A] \033[4mInvestigate\033[0m.\n"
                                      "[B] Sleep \033[4mharder\033[0m.")
        if user_choice == "a" or user_choice == "investigate":
            get_up()
            break
        elif user_choice == "b" or user_choice == "harder":
            sleep_harder()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def sleep_harder():
    """
    Sleep harder. Fastest game end.
    """
    clear_terminal()
    slowprint("You really do have to get up early and you've never been a "
              "very inquisitive\nperson. You pull the blanket tight around "
              "your ears and scrunch your eyes \nclosed even harder. As you "
              "do, you feel a chill run up the back of your neck\nand the "
              "blanket starts to feel very heavy...\n")
    time.sleep(1)
    slowprint(f"""\n'{GAME_VARS["username"]}'\n"""
              "Who's saying that? You try to open your eyes and peek out "
              "from the covers, but\nyour eyelids won't open and the covers "
              "are weighing you down...\n")
    time.sleep(1)
    slowprint("\nThe covers press harder and harder and your eyelids squeeze "
              "tighter and\ntighter until all you feel is pressure and all you"
              " see is nothingness.\n"
              "You never wake up again.\n\n")
    print(pyfiglet.figlet_format("The End", font="shadow", justify="center"))
    play_again()


def get_up():
    """
    Get up.
    Choice to close window or get slippers. Either changes window_closed
    boolean or appends slippers to our pick_ups list.
    Calls leave_bedroom function either way after user decision
    """
    clear_terminal()
    slowprint("Maybe a cup of tea will warm you up and help you drift off to "
              "sleep. You climb\nout of bed. You glance at the open window "
              "that's letting a cold breeze into the\nhouse. At the end of "
              "your bed are an oversized pair of fluffy bunny slippers.\n")
    while True:
        user_choice = get_user_choice("You shiver and:\n"
                                      "[A] Close the \033[4mwindow\033[0m.\n"
                                      "[B] Put on your fluffy \033[4mslippers"
                                      "\033[0m.")
        if user_choice == "a" or user_choice == "window":
            GAME_VARS["window_closed"] = True
            break
        elif user_choice == "b" or user_choice == "slippers":
            GAME_VARS["pick_ups"].append("slippers")
            break
        else:
            print(f"{user_choice} isn't really an option...\n")

    leave_bedroom()


def leave_bedroom():
    """
    Leave bedroom.
    First line depends on choice in get_up function
    Choice to investigate closet. Optional - user can ignore
    """
    clear_terminal()
    if GAME_VARS["window_closed"]:
        draw_image("window")
        slowprint("You slide the window closed and shuffle out into the "
                  "hallway in your bare feet.\n")
    else:
        draw_image("slippers")
        slowprint("You shiver and slip your slippers on, then shuffle out "
                  "into the hallway.\n")
    slowprint("The house is still. You cannot hear a sound. You creep along "
              "the hallway as\nquietly as you can. As you go, on your left you"
              " pass the hallway closet.\n")
    while True:
        user_choice = get_user_choice("You feel compelled to:\n"
                                      "[A] \033[4mCheck\033[0m inside, though "
                                      "it's as quiet as the rest of the house."
                                      "\n"
                                      "[B] Keep \033[4mgoing\033[0m - you don'"
                                      "t need to encourage your imagination.")
        if user_choice == "a" or user_choice == "check":
            check_closet()
            break
        elif user_choice == "b" or user_choice == "going":
            continue_hallway()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def check_closet():
    """
    Optional. Can collect teddy or golf club.
    User can also back out and pick up nothing
    """
    clear_terminal()
    draw_image("closet")
    slowprint("For some reason, you decide to investigate the quiet closet. "
              "You try to peek\nthrough the slats of the closet door, but see "
              "nothing except darkness. Slowly,\nyou open the closet and peer "
              "inside.\n"
              "As expected, there is only the regular assortment of clutter - "
              "coats, shoes,\ngolf clubs, your old teddy bear 'Burt'.\n")
    while True:
        user_choice = get_user_choice("You decide to:\n"
                                      "[A] Take \033[4mBurt\033[0m with you, "
                                      "you haven't spent much time together\n"
                                      "lately.\n"
                                      "[B] Take a golf \033[4mclub\033[0m.\n"
                                      "[C] Take \033[4mnothing\033[0m. You "
                                      "don't know why you decided to open the"
                                      "\ncloset in the first place.")
        if user_choice == "a" or user_choice == "burt":
            GAME_VARS["pick_ups"].append("teddy")
            continue_hallway()
            break
        elif user_choice == "b" or user_choice == "club":
            GAME_VARS["pick_ups"].append("golf_club")
            continue_hallway()
            break
        elif user_choice == "c" or user_choice == "nothing":
            continue_hallway()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def continue_hallway():
    """
    After bedroom or closet. User has option to check bedroom. Can ignore
    """
    clear_terminal()
    if "teddy" in GAME_VARS["pick_ups"]:
        draw_image("teddy")
        slowprint("You take Burt down from the shelf in the closet and grip "
                  "him tightly in your\narms.\n")
    elif "golf_club" in GAME_VARS["pick_ups"]:
        draw_image("club")
        slowprint("You nod at Burt, but pull a long golf club from the bag in "
                  "the back of the\ncloset. The metal feels cold in your hands"
                  ".\n")
    slowprint("You continue down the hallway and pass the master bedroom on "
              "your right.\n"
              f"""'{GAME_VARS["username"]}'\n"""
              "Who said that? You think it came from inside the door. It was "
              "so quiet, though.\n"
              "Maybe it was just your mind playing tricks on you?\n")
    while True:
        user_choice = get_user_choice("Will you:\n"
                                      "[A] \033[4mIgnore\033[0m it. It was "
                                      "just the wind.\n"
                                      "[B] \033[4mInvestigate\033[0m.")
        if user_choice == "a" or user_choice == "ignore":
            go_kitchen()
            break
        elif user_choice == "b" or user_choice == "investigate":
            check_bedroom()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def check_bedroom():
    """
    Optional interaction. Leaves master bedroom door open.
    """
    clear_terminal()
    draw_image("master")
    slowprint("Very slowly, you creep across the hall to the door. You press "
              "your ear up\nagainst it, but can hear nothing from inside. The "
              "door knob feels cool on your\nhand.\n"
              "Gingerly, you turn it. The door creaks as you push it open a "
              "crack. Peering in,\nthe room is so dark you can only see the "
              "outline of the duvet on the bed.\n"
              "Nothing is stirring in the room. You cannot hear a sound.\n"
              "Relieved, you leave the door open a crack and continue towards "
              "the kitchen...\n")
    GAME_VARS["door_open"] = True
    time.sleep(1)
    go_kitchen()


def go_kitchen():
    """
    In kitchen. Missable text depending on what items user has
    Choice to use step stool or not
    """
    clear_terminal()
    draw_image("kettle")
    slowprint("You continue on towards the kitchen. It is as quiet as the rest"
              " of the house.\nMoonlight filters in through the windows and "
              "illuminates the room.\n")
    if "slippers" not in GAME_VARS["pick_ups"]:
        if "teddy" in GAME_VARS["pick_ups"]:
            slowprint("The tiles feel like ice under your bare feet. You hug "
                      "Burt closely.\n")
        else:
            slowprint("The tiles feel like ice under your bare feet. You "
                      "shiver and hug yourself.\n")
    slowprint("The kettle is tucked right in under the cabinets on the "
              "counter.\n")
    while True:
        user_choice = get_user_choice("You think:\n"
                                      "[A] You can \033[4mreach\033[0m it if "
                                      "you stretch. \n"
                                      "[B] There's a \033[4mstool\033[0m here "
                                      "somewhere.")
        if user_choice == "a" or user_choice == "reach":
            try_reach()
            break
        elif user_choice == "b" or user_choice == "stool":
            get_stool()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def get_stool():
    """
    Optional function if user decides to get step stool
    """
    clear_terminal()
    draw_image("stool")
    slowprint("You think you remember the stool by the backdoor. You walk past"
              " the island in\nthe middle of the kitchen, past the table and "
              "find the stool next to the door,\nbeside your wellies.\n"
              "You glance at the door quickly as you retrieve the stool. It "
              "looks locked to\nyou. Of course it is.\n"
              "You bring the stool back over to the counter and step up on it."
              " You can easily\npull the kettle out from under the cabinet..."
              "\n")
    GAME_VARS["stool_out"] = True
    time.sleep(1)
    kettle_on()


def try_reach():
    """
    Optional function if user decides to ignore step stool.
    Will lose current item. Except slippers
    """
    clear_terminal()
    slowprint("You think your arms are long enough. The counter is a little "
              "wide, though.\n")
    if "teddy" in GAME_VARS["pick_ups"]:
        GAME_VARS["pick_ups"].remove("teddy")
        slowprint("So, you pop Burt on the counter to free your hands.\n")
    elif "golf_club" in GAME_VARS["pick_ups"]:
        GAME_VARS["pick_ups"].remove("golf_club")
        slowprint("So, you place the golf club down to free your hands.\n")
    slowprint("On your toes, leaning on the counter with one hand, you reach "
              "out for the\nkettle. You can just about pull it out from under "
              "the cabinet.\n")
    time.sleep(1)
    kettle_on()


def kettle_on():
    """
    Turn kettle on. No user interaction.
    Missable text depending on if user got the stool
    """
    clear_terminal()
    draw_image("tea")
    slowprint("You flick the switch on the kettle and the little light above "
              "it comes on. It\nstarts a low rumble. While the kettle boils, "
              "you collect your ingredients.\n"
              "Your favourite mug is sitting on the edge of the sink where you"
              " left it that\nafternoon. You collect it.\n"
              "The tea bags and sugar are much easier to reach than the kettle"
              ". You place a\ntea bag in your mug. You take a spoon from the "
              "drawer and place it next to\nyour cup.\n")
    time.sleep(1)
    slowprint("You walk over to the fridge to get the milk. You open the door "
              "and take out the\nmilk carton. As the fridge door closes, you "
              "can see the back door. It is\nslightly open.\n")
    if GAME_VARS["stool_out"]:
        slowprint("But, it was just closed?\n")
    else:
        slowprint("Was that open before?\n")
    time.sleep(1)
    shadow_appears()


def shadow_appears():
    """
    Monster. User can choose to run or do nothing
    """
    clear_terminal()
    draw_image("shadow")
    slowprint("As you watch, the back door slowly creaks open. A shadowy "
              "figure forms before\nyou. The hair stands up on the back of "
              "your neck as it approaches.\n"
              "It seems to glide across the floor without taking a step.\n")
    while True:
        user_choice = get_user_choice("You:\n"
                                      "[A] \033[4mRun\033[0m.\n"
                                      "[B] \033[4mFreeze\033[0m.")
        if user_choice == "a" or user_choice == "run":
            run_away()
            break
        elif user_choice == "b" or user_choice == "freeze":
            you_freeze()
            break
        else:
            print(f"{user_choice} is not an option.\n")


def you_freeze():
    """
    User chooses freeze. Has another chance do make a choice
    """
    clear_terminal()
    slowprint(f"""'{GAME_VARS["username"]},' the shadowy figure whispers.\n"""
              "How does it know your name?\n")
    while True:
        user_choice = get_user_choice("You:\n"
                                      "[A] \033[4mCall\033[0m for help.\n"
                                      "[B] \033[4mRun\033[0m.")
        if user_choice == "a" or user_choice == "call":
            kitchen_cry()
            break
        elif user_choice == "b" or user_choice == "run":
            run_away()
            break
        else:
            print(f"{user_choice} is REALLY not an option.\n")


def kitchen_cry():
    """
    User calls for help. If has teddy, can survive. Else dies
    """
    clear_terminal()
    if "teddy" in GAME_VARS["pick_ups"]:
        slowprint("You open your mouth, but then in a panic you toss Burt at "
                  "the figure. The\nshadow stops and catches him. While it's "
                  "distracted, you make a break for it.\n")
        GAME_VARS["pick_ups"].remove("teddy")
        time.sleep(1)
        run_away()
    elif "golf_club" in GAME_VARS["pick_ups"]:
        slowprint("The figure reaches for you. Impulsively, you swing the golf"
                  " club that is still\nin your hands. You miss and the shadow"
                  " continues to advance...\n")
    user_dies()


def user_dies():
    """
    Function for user death.
    Reusable for different end game decisions.
    """
    clear_terminal()
    time.sleep(1)
    slowprint("You open your mouth to cry out for help, but your voice stops "
              "in your throat.\n"
              f"""'{GAME_VARS["username"]},' the figure groans.\n"""
              "It reaches for you.\n"
              "Your legs quiver. Your feet refuse to listen to you. Your eyes "
              "widen but your\nvision fades. You can feel a weight press down "
              "upon you...\n")
    time.sleep(1)
    slowprint("You are overcome with darkness. All you feel and see and hear "
              "is nothingness.\n"
              f"""'Goodnight, {GAME_VARS["username"]}.'\n"""
              "You never wake up again.\n\n")
    print(pyfiglet.figlet_format("The End", font="shadow", justify="center"))
    play_again()


def run_away():
    """
    User chooses to run away. If took stool out, can delay shadow
    If has slippers on and stool out, can die unless has teddy
    """
    clear_terminal()
    slowprint("You turn and run.\n"
              f"""'{GAME_VARS["username"]},' the figure growls.\n""")
    if GAME_VARS["stool_out"] and "slippers" in GAME_VARS["pick_ups"]:
        slowprint("You run through the kitchen and hop over the stool as you "
                  "go. As you leap, the\nbunny ears of your fluffy slippers "
                  "catch on the stool and you fall! You\ncollapse on the "
                  "kitchen tiles and the shadow looms over you.\n")
        if "teddy" in GAME_VARS["pick_ups"]:
            slowprint("In a panic, you throw Burt at the shadowy figure. It "
                      "catches him. As it seems\nto stare at Burt in confusion"
                      ", you kick your slippers off and run for the\nhallway"
                      ".\n")
            GAME_VARS["pick_ups"].remove("teddy")
            time.sleep(1)
            run_hallway()
        else:
            user_dies()
    elif GAME_VARS["stool_out"]:
        slowprint("You run through the kitchen, hopping over the stool as you "
                  "go. The figure\nfollows, but as you reach the hallway, you "
                  "glance back and see it stumble over\nyour step stool and "
                  "fall on the kitchen tiles.\n")
        time.sleep(1)
        GAME_VARS["shadow_delayed"] = True
        run_hallway()
    elif not GAME_VARS["stool_out"]:
        run_hallway()


def run_hallway():
    """
    Run to hallway. User has choice of four rooms. 2 could have been changed
    by previous decisions. Time to escape effected by if shadow delayed
    """
    if not GAME_VARS["shadow_delayed"]:
        slowprint("You reach the hallway, but the shadow is right on your "
                  "heels.\n"
                  "There's little time.\n")
    elif GAME_VARS["shadow_delayed"]:
        slowprint("You reach the hallway before the shadowy figure can gather "
                  "itself.\n")
    slowprint("You have to hide.\n")
    while True:
        user_choice = get_user_choice("You run to:\n"
                                      "[A] The \033[4mmaster\033[0m bedroom.\n"
                                      "[B] The \033[4mcloset\033[0m.\n"
                                      "[C] Your \033[4mbedroom\033[0m.\n"
                                      "[D] The front \033[4mdoor\033[0m.")
        if user_choice == "a" or user_choice == "master":
            hide_master()
            break
        elif user_choice == "b" or user_choice == "closet":
            hide_closet()
            break
        elif user_choice == "c" or user_choice == "bedroom":
            hide_bedroom()
            break
        elif user_choice == "d" or user_choice == "door":
            front_door()
            break
        else:
            print(f"{user_choice} is REALLY not an option now!\n")


def front_door():
    """
    Front door. User dies unless has teddy still.
    If has teddy, runs to bedroom
    """
    clear_terminal()
    draw_image("front")
    slowprint("You race for the front door, hoping to escape from the house. "
              "You pull on the\nhandle. The door won't budge.\n"
              f"""'{GAME_VARS["username"]},' whispers the shadowy figure as """
              "it approaches.\nYou fumble with the door and, too late, realise"
              " the bolt at the top is locked,\nout of reach.\n")
    if "teddy" in GAME_VARS["pick_ups"]:
        slowprint("In a panic, you throw Burt at the shadowy figure. It "
                  "catches him. As it seems\nto stare at Burt in confusion, "
                  "you run for your bedroom.\n")
        GAME_VARS["pick_ups"].remove("teddy")
        hide_bedroom()
    else:
        user_dies()


def hide_closet():
    """
    Hide in closet. User dies if shadow right behind, obviously.
    """
    clear_terminal()
    slowprint("You race for the closet, diving through the slatted doors and "
              "pulling them\nclosed behind you. Hastily, you cover yourself "
              "in a pile of winter coats. You\nput your hand to your mouth "
              "and try to stay as quiet as you can.\n"
              "All you can hear is your own breathing.\n")
    if not GAME_VARS["shadow_delayed"]:
        slowprint("Only seconds pass before the closet door slowly opens.\n")
        time.sleep(1)
        hidden_user_dies()
    elif GAME_VARS["shadow_delayed"]:
        time.sleep(1)
        user_hides()


def user_hides():
    """
    Reusable hiding for closet, master bedroom while shadow delayed
    User dies if chooses to stay
    User always runs to own bedroom if chooses to run
    """
    slowprint("An eternity passes as you hide in the darkness. Is it still out"
              " there?\n"
              "You think you hear something pass by the door, but did you just"
              " imagine that?\n"
              "How much longer can you wait?\n"
              "You think you can hear a sound coming from the kitchen.\n")
    while True:
        user_choice = get_user_choice("You decide to:\n"
                                      "[A] \033[4mRun\033[0m to your bedroom."
                                      "\n"
                                      "[B] \033[4mStay\033[0m hidden.")
        if user_choice == "a" or user_choice == "run":
            hide_bedroom()
            break
        elif user_choice == "b" or user_choice == "stay":
            hidden_user_dies()
            break
        else:
            print(f"{user_choice} is not an option!\n")


def hidden_user_dies():
    """
    Reusable death end game when user hidden
    Two lines added for variation, then calls user_dies function
    """
    slowprint("You stay frozen in fear where you are.\n"
              "A cold chill runs up your spine and, suddenly, you see it "
              "before you.\n")
    user_dies()


def hide_master():
    """
    Hide in master bedroom. If user previously interacted, door open.
    If shadow delayed, can hide. If not delayed, caught.
    If not interacted before, door closed. If shadow delayed, can go
    elsewhere. If not delayed, caught
    """
    clear_terminal()
    slowprint("The master bedroom is closest so you race for the door.\n")
    if GAME_VARS["shadow_delayed"] and GAME_VARS["door_open"]:
        slowprint("You slip through the open door.\n"
                  "Expecting safety, you realise the mound of blankets you "
                  "saw earlier is just\nthat - blankets. The room is empty. "
                  "You have no time to wonder why, so you dive\nunderneath "
                  "the bed.\n")
        time.sleep(1)
        user_hides()
    elif GAME_VARS["shadow_delayed"] and not GAME_VARS["door_open"]:
        slowprint("You turn the doorknob, but the door won't open. It's "
                  "locked? Why?\n")
        while True:
            user_choice = get_user_choice("You turn around and:\n"
                                          "[A] Run to your \033[4mbedroom"
                                          "\033[0m.\n"
                                          "[B] Run to the \033[4mcloset"
                                          "\033[0m.")
            if user_choice == "a" or user_choice == "bedroom":
                hide_bedroom()
                break
            if user_choice == "b" or user_choice == "closet":
                hide_closet()
                break
            else:
                print(f"{user_choice} is REALLY not an option now!\n")
    elif not GAME_VARS["shadow_delayed"]:
        slowprint("You almost reach the door, but the shadowy figure is right "
                  "behind you.\n")
        user_dies()


def hide_bedroom():
    """
    Back to own room. 3 options to escape.
    Under covers, with teddy, only happy ending.
    Under bed, caught
    Can go to window
    """
    clear_terminal()
    slowprint("You race into your bedroom. As quickly and quietly as you can, "
              "you close the\ndoor behind you. What now?\n")
    while True:
        user_choice = get_user_choice("You:\n"
                                      "[A] \033[4mSlide\033[0m under your bed"
                                      ".\n"
                                      "[B] \033[4mRun\033[0m to the window.\n"
                                      "[C] \033[4mJump\033[0m back into bed "
                                      "and pull the covers over your head.")
        if user_choice == "a" or user_choice == "slide":
            under_bed()
            break
        elif user_choice == "b" or user_choice == "run":
            run_window()
            break
        elif user_choice == "c" or user_choice == "jump":
            back_bed()
            break
        else:
            print(f"{user_choice} is not an option!\n")


def under_bed():
    """
    Hiding under bed. Gets caught always
    """
    clear_terminal()
    slowprint("You dive head first under your bed and curl yourself into as "
              "small of a ball as\nyou can.\n"
              "You cover your mouth and try to quiet your breathing.\n"
              f"""'{GAME_VARS["username"]}.'\n"""
              "The bedroom door creaks open slowly.\n")
    time.sleep(1)
    hidden_user_dies()


def run_window():
    """
    If window still open or has golf club, can escape.
    If window closed and no golf club, caught.
    """
    clear_terminal()
    if GAME_VARS["window_closed"]:
        draw_image("window_closed")
        if "golf_club" in GAME_VARS["pick_ups"]:
            slowprint("You run over to the window and try to slide it open, "
                      "but it's jammed. You can't\nforce it.\n"
                      "The golf club! You still have it!\n"
                      "You can hear the door slowly open behind you.\n"
                      f"""'{GAME_VARS["username"]},' the shadow softly """
                      "growls.\n"
                      "You swing the club..\n")
            time.sleep(1)
            escape_house()
        else:
            slowprint("You run over to the window and try to slide it open. "
                      "It's jammed. Pushing with\nall your strength, you can't"
                      " force it open.\n"
                      "You turn as the bedroom door slowly opens and try to "
                      "make yourself as small as\nyou can in the corner of the"
                      " room...\n")
            user_dies()
    elif not GAME_VARS["window_closed"]:
        draw_image("window")
        slowprint("You run over to the window. It's still open a crack. You "
                  "slide it open even\nwider as you hear your bedroom door "
                  "slowly open behind you.\n"
                  f"""'{GAME_VARS["username"]},' the shadow softly """
                  "growls...\n")
        escape_house()
        play_again()


def escape_house():
    """
    Ending - survives?
    """
    clear_terminal()
    slowprint("You slip out your bedroom window and run out on to the footpath"
              ". Looking back\nat your house, you think you see the shadow in "
              "your window.\n"
              "It's quiet out. The road is still. There are no lights in any "
              "of the houses.\n"
              "Your grandparents live nearby. You go there every Sunday, it's "
              "not a very long\ndrive.\n"
              "You think you know which way to go. It'll be safe there.\n"
              "You start walking.\n\n")
    print(pyfiglet.figlet_format("The End", font="shadow", justify="center"))
    play_again()


def back_bed():
    """
    Under covers. If have teddy, can win.
    Otherwise, dies
    """
    clear_terminal()
    draw_image("bed")
    slowprint("You dive into your bed and pull the covers up over your head. "
              "You close your\neyes and try as hard as you can to fall back "
              "to sleep.\n")
    if "teddy" in GAME_VARS["pick_ups"]:
        slowprint("You hug Burt close.\n")
        time.sleep(1)
        wake_win()
    else:
        slowprint("You can hear it. The bedroom creaks open. You lift the edge"
                  " of your blankets\nand peek out with one eye.\n")
        time.sleep(1)
        hidden_user_dies()


def wake_win():
    """
    Happy ending!
    """
    clear_terminal()
    draw_image("teddy")
    slowprint(f"""'{GAME_VARS["username"]}, why is there milk all over the """
              "kitchen floor?'\nYour eyes open. Light seeps in around your "
              "blankets. You throw them back.\n"
              "It's morning. Your bedroom is bright and empty. There's no "
              "shadowy figures \nlurking in the corners.\n"
              "It must have all been a terrible nightmare.\n"
              "You're safe.\n"
              "You look at Burt, still cradled in your arms.\n\n")
    print(pyfiglet.figlet_format("The End", font="shadow", justify="center"))
    play_again()


def play_again():
    """
    Function at end of game to ask user if they want to play or quit
    """
    time.sleep(2)
    user_choice = get_user_choice(f"Well, {GAME_VARS['username']}, would you "
                                  "like to try again?\n"
                                  "[A] \033[4mYes\033[0m! Let's play again!\n"
                                  "[B] No, I want to \033[4mquit\033[0m to the"
                                  " title screen.")
    while True:
        if user_choice == "a" or user_choice == "yes":
            start_room()
            break
        elif user_choice == "b":
            main()
        else:
            print(f"{user_choice} isn't an option")
