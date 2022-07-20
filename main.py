from classes_and_functions import *

# from build_board import *
from Andrew_rooms import *
from conditions import *
import time
import pickle
import colorama
import random
from colorama import Fore, Back, Style

colorama.init()


def main():
    #    TREASURE TOMB
    #  print the title and a graphic with ASCII art

    # ask the user if they want to start a new game or load a saved game
    print("Press 1 to start a new game")
    print("Press 2 to load a saved game")
    game = input()

    gn = False

    while not gn:
        if game != "1" and game != "2":
            print("Press 1 to start a new game")
            print("Press 2 to load a saved game")
            game = input()
        else:
            gn = True

    load = False
    gn = False

    if game == "1":
        print("Please enter the name of your new save")
        save_name = input()
        # cannot have a new file named 'new' since we use new.pickle to load every new game from
        while save_name == "new":
            print("Please choose a different name for your save ")
            print("Please enter the name of your new save")
            save_name = input()
        while not gn:
            try:
                with open(save_name + ".pickle", "rb") as f:
                    gn = False
                    print("File already exists with this save name.")
                    print("Please enter a different save name")
                    save_name = input()
            except OSError:
                gn = True
    if game == "2":
        print("Please enter the name of your saved game")
        save_name = input()
        load = True
    # pull the relevant data from a saved json file
    if not load:
        print(
            "You have finally arrived at the temple. It's a tall, stone structure with stairs leading up to a dark "
            "entryway."
        )
        print(
            "You'd been following the clues and you are ready to retrieve the treasure. Thunder rolls ominously in "
            "the distance."
        )
        print("It's your last chance to turn back.")

        print("1) Go inside")
        print("2) Turn back")

        decision = input()

        if decision == "2":
            print("Game Over")
            return
        # You have now entered the temple.
        player = build_the_board()

    lf = False

    if load:
        while not lf:
            try:
                with open(save_name + ".pickle", "rb") as f:
                    player = pickle.load(f)
                    lf = True
            except OSError:
                print("save file not found")
                print("Please enter the name of your saved game")
                save_name = input()
    while True:
        print("\n")
        if player.in_combat is None:
            player.current_location.build_description()
        if player.in_combat is not None:
            player.fight(player.in_combat)
            input("Press Enter to return")
            print("What will you do?")
        time.sleep(0.25)
        user_inputted_command = player.current_location.take_input(player)
        time.sleep(0.25)
        player.execute_input(user_inputted_command, player, save_name)
        time.sleep(0.25)
        check_conditions(player)
        time.sleep(0.25)
        if player.HP == 0:
            player.is_dead = True
        if player.is_dead:
            return
        if player.has_won:
            print("Congratulations, you have found the treasure and won the game!")
            return
        if player.exit:
            print("exiting game")
            return


main()
