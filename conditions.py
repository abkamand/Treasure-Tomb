from classes_and_functions import *
from build_board import *
import colorama
from colorama import Fore, Back, Style
import random

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
    water_room_mummy(player)
    water_room_conditions(player)
    return


# ------------------------------ASH's CLUSTER CONDITIONS ------------------------------------------------------

def water_room_mummy(player):
    """
    When you enter the water room, you will immediately be attacked by the mummy with the axe. When he dies, he will
    drop the axe.
    """
    if player.current_location.name == "Water Room" and player.current_location.visited == True:
        for enemies in player.current_location.enemies:  # iterate through enemies to see if the mummy is dead
            if enemies.name == "mummy" and enemies.is_dead == False:
                player.in_combat = enemies
            if enemies.name == "mummy" and enemies.is_dead == True:
                print('As the defeated mummy vanishes into dust, he drops his axe to the floor.')
                print("Press Enter to return")
                input()
                player.current_location.enemies.remove(enemies)
                axe = Item("axe")
                axe.add_description("A powerful axe that fell from a vanquished mummy. Might come in handy. \n Power: 35")
                axe.toggle_can_pick_up()
                axe.toggle_on_floor()
                axe.toggle_is_weapon()
                axe.set_weapon_power(35)
                player.current_location.add_item_to_room(axe)
                return

def water_room_conditions(player):
    """
    If you have the chalice in your inventory and you activate the sink, the chalice will be filled with water
    Then, if you activate the statue with the chalice that now has water in it, you will pour water into the mouth of
    the statue.
    If this happens, the room will fill with water and you can swim to the southern door.

    """
    chalice_in_inventory = False
    chalice_ability = False
    for items in player.inventory:
        if items.name == "chalice":
            chalice_in_inventory = True
    for items in player.current_location.in_room:
        if items.name == "sink":
            if items.ability and chalice_in_inventory == True:
                print("The chalice has been filled with a few drops from the sink.")
                print("Press Enter to return")
                input()
                items.ability = False
                for i in player.inventory:
                    if i.name == "chalice":
                        i.ability = True
                        chalice_ability = True
    for items in player.inventory:
        if items.name == "chalice":
            items.ability = True
            chalice_ability = True
    for items in player.current_location.in_room:
        if items.name == "statue":
            if items.ability and chalice_ability:
                print("You pour the water from the chalice into the mouth of the statue of Khnum.")
                print("Suddenly, you hear a rush of water coming from beneath you! The sink begins to overflow with water! ")
                print("Water begins pouring through the cracks of the limestone walls, flooding the room!")
                print("The flooding causes the water level of the room to rise, taking you with it.")
                print("Finally, the flooding stops. You are now able to reach the door on the southern wall (" + (Fore.YELLOW + "southern door") + '\033[39m' + ").")
                player.current_location.long_description = "The room has been flooded. All that remains is a pool of glistening water. You can now swim to the door on the southern wall(" + (Fore.YELLOW + "southern door") + '\033[39m' + ")."
                player.current_location.shortened_description = "The room has been flooded. All that remains is a pool of glistening water. You can now swim to the door on the southern wall(" + (
                            Fore.YELLOW + "southern door") + '\033[39m' + ")."
                items.ability = False
                print("Press Enter to return")
                input()
















