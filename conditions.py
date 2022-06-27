from classes_and_functions import *
from build_board import *
import colorama
from colorama import Fore, Back, Style

colorama.init()

# This is the conditions file that will be run during every gameplay loop in order to change the board
# if anything happens. The function check_conditions is the main function in this file. Since there will
# undoubtedly be many,many conditions that can happen in this game, we will be putting each condition in
# its own function, which will then be run within check_conditions (similar to the main function of a C program).

# If you look at check_conditions, you will see an example of a function diamond_from_dead_mummy that is an example of
# this structure.

# This is just one example, but using similar strategies that are tons of different things you can do by manipulating
# different objects. For example, you can make a room dark to begin with, and then check to see if the player has
# activated a torch. If he/she has, you can change the description of the room to have more information.


def check_conditions(player):
    diamond_from_dead_mummy(player)
    return


# ------------------------------ASH's CLUSTER CONDITIONS ------------------------------------------------------

def diamond_from_dead_mummy(player):
    """
    Once you kill the mummy that is in "ash cluster room 1", he will say a warning and a diamond will fall from his
    chest. You can now pick up that diamond
    """
    if player.current_location.name == "ash cluster room 1":  # check to see if the player is in the right room
        for enemies in player.current_location.enemies:  # iterate through enemies to see if the mummy is dead
            if enemies.name == "mummy" and enemies.is_dead == True:  # name must match and must be dead
                print('As the mummy vanishes into dust, he screeches, "You will not make it out of this tomb alive!" As his body disintegrates, he reaches into his rotting chest and pulls out a diamond from it.')
                print('The diamond falls from his grasp onto the floor.')
                # now remove the mummy from the room so that this condition does not trigger again next time you
                # enter this room
                player.current_location.enemies.remove(enemies)
                # create the diamond that fell from the mummy, and change attributes as needed
                diamond = Item("diamond")
                diamond.add_description("A red diamond that fell from the body of a mummy after you defeated it.")
                diamond.toggle_can_pick_up()
                diamond.toggle_on_floor()
                # add the diamond to the room
                player.current_location.add_item_to_room(diamond)
                return









