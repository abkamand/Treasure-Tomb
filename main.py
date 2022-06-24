from classes_and_functions import *
from build_board import *
from conditions import *
import time
import pickle
import colorama
from colorama import Fore, Back, Style
colorama.init()
def main():
    #    TREASURE TOMB
    #  print the title and a graphic with ASCII art

    # ask the user if they want to start a new game or load a saved game
    print("Press 1 to start a new game")
    print("Press 2 to load a saved game")
    game = input()

    load = False

    if game == "1":
        print("Please enter the name of your new save")
        save_name = input()
    if game == "2":
        print("Please enter the name of your saved game")
        save_name = input()
        load = True
    # pull the relevant data from a saved json file
    if not load:
        print(
            "You have finally arrived at the temple. It's a tall, stone structure with stairs leading up to a dark "
            "entryway.")
        print(
            "You'd been following the clues and you are ready to retrieve the treasure. Thunder rolls ominously in "
            "the distance.")
        print("It's your last chance to turn back.")

        print("1) Go inside")
        print("2) Turn back")

        decision = input()

        if decision == "2":
            print("Game Over")
            return
        # You have now entered the temple.
        player = build_the_board()

    if load:
        with open(save_name + ".pickle", 'rb') as f:
            player = pickle.load(f)

    while True:
        player.current_location.build_description()
        time.sleep(1)
        user_inputted_command = player.current_location.take_input()
        time.sleep(1)
        player.execute_input(user_inputted_command, player, save_name)
        time.sleep(1)
        check_conditions(player)
        time.sleep(1)
        if player.is_dead:
            return

        # need to add options to class, option to add options and take away options as items are picked up an dropped


main()
