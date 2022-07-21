from classes_and_functions import *
from build_board import *
from Andrew_rooms import *
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

    # Andrew's Rooms
    explode_boulder(player)
    jump_puzzle(player)

    return


# ------------------------------Andrew's CLUSTER CONDITIONS ------------------------------------------------------
# Andrew room 1
def check_coffin(player):
    # add coffin ability, can toggle
    # put ruby description in coffin, color code
    # check if ruby is in player inventory, if so update description
    return


# Andrew room 3
# player must jump onto small pillar, medium pillar, box, large pillar in that order to progress to next room
def jump_puzzle(player):
    in_room = False
    short_pillar = False
    medium_pillar = False
    large_pillar = False

    if player.current_location.name == "Andrew 3":
        in_room = True
    for items in player.current_location.in_room:
        if items.name == "short_pillar" and items.ability == True:
            short_pillar = True
        elif items.name == "medium_pillar" and items.ability == True:
            medium_pillar = True
        elif items.name == "large_pillar" and items.ability == True:
            large_pillar = True

    if in_room == True and (
        short_pillar == True or medium_pillar == True or large_pillar == True
    ):
        if short_pillar == False:
            print("You jump and fall back to the floor, ouch")
            # lower player HP
            return

        print("You are standing on top of the short pillar")
        print("What will you do next?")
        response = input()
        if response != "activate medium_pillar":
            print("You jump and fall back to the floor, ouch")
            return

        print("You are standing on top of the medium pillar")
        print("What will you do next?")
        response = input()
        if response != "activate large_pillar":
            print("You jump and fall back to the floor, ouch")
            return

        print(
            "You made it to the roof chamber. You find a rope nearby and lower it so you can slide down quickly... not sure you have the strength to climb back up the rope though."
        )
        # move the player into the next room
        for items in player.current_location.in_room:
            items.ability = False
        player.current_location = player.current_location.north_wall


# if player lights the dynamite and throws it at the wrong object (dynamite bounces back and blows you up)
def dead_to_dynamite(player):
    return


# Andrew room 1
# blow up the stone blocking a door in room 1 by lighting dynamite on the rock
def explode_boulder(player):
    if player.current_location.name == "Andrew 1":
        for items in player.current_location.in_room:
            if items.name == "boulder":
                for i in items.contains:
                    if i.name == "dynamite" and i.ability == False:
                        return
                        # ask ashwin!
                        # add dynamite back to player inventory
                        # print "maybe you should light the dynamite first"
                    if i.name == "dynamite" and i.ability == True:
                        print(
                            "You place the stick of dynamite near the rock, and run. The rock explodes, leaving an open doorway. \nDefying the laws of physics, there's almost no damage in your current room, but you hear rumblings in the northern room... \nit must be in complete disarray."
                        )
                        player.current_location.in_room.remove(items)

                        """for items in player.current_location.in_room:
                            if items.name == "boulder":
                                player.current_location.in_room.remove(items)"""

                        # CONNECT west_three to west_one now that the boulder is gone
                        # create the shortened description for the room, will be displayed when you are visiting a room you have been to
                        description = (
                            "You enter a dark room with a pile of coffins and treaures in the corner.\nOne appears"
                            + (Fore.MAGENTA + " wooden")
                            + "\033[39m"
                            + " and ripped open, one appears"
                            + (Fore.MAGENTA + " metallic")
                            + "\033[39m"
                            + ", and the third appears to be"
                            + (Fore.MAGENTA + " small")
                            + "\033[39m"
                            + " and molded over."
                            + "\nPerhaps you should take a closer look at the coffins for anything useful?"
                            + "\nOn the northern wall, there is a narrow passage that leads into a pitch black corridor ("
                            + (Fore.YELLOW + "northern corridor")
                            + "\033[39m"
                            + ").\nOn the eastern wall, where the boulder used to be, you spot a newly revealed eastern passage"
                            + (Fore.YELLOW + " (eastern corridor).")
                            + "\033[39m"
                        )
                        # now add the description to the shortened_description attribute of the room
                        player.current_location.add_shorter_description(description)


# Andrew room 4
# Player must pick up python, alligator, eagle figurines, and place them on the correct pedestals to unlock diamond key
def animal_puzzle(player):
    return


# Andrew room 2
# still undecided on the crux of this puzzle
def darkness_puzzle(player):
    return


# ------------------------------ASH's CLUSTER CONDITIONS ------------------------------------------------------


def water_room_mummy(player):
    """
    When you enter the water room, you will immediately be attacked by the mummy with the axe. When he dies, he will
    drop the axe.
    """
    if (
        player.current_location.name == "Water Room"
        and player.current_location.visited == True
    ):
        for (
            enemies
        ) in (
            player.current_location.enemies
        ):  # iterate through enemies to see if the mummy is dead
            if enemies.name == "mummy" and enemies.is_dead == False:
                player.in_combat = enemies
            if enemies.name == "mummy" and enemies.is_dead == True:
                print(
                    "As the defeated mummy vanishes into dust, he drops his axe to the floor."
                )
                print("Press Enter to return")
                input()
                player.current_location.enemies.remove(enemies)
                axe = Item("axe")
                axe.add_description(
                    "A powerful axe that fell from a vanquished mummy. Might come in handy. \n Power: 35"
                )
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
                print(
                    "You pour the water from the chalice into the mouth of the statue of Khnum."
                )
                print(
                    "Suddenly, you hear a rush of water coming from beneath you! The sink begins to overflow with water! "
                )
                print(
                    "Water begins pouring through the cracks of the limestone walls, flooding the room!"
                )
                print(
                    "The flooding causes the water level of the room to rise, taking you with it."
                )
                print(
                    "Finally, the flooding stops. You are now able to reach the door on the southern wall ("
                    + (Fore.YELLOW + "southern door")
                    + "\033[39m"
                    + ")."
                )
                player.current_location.long_description = (
                    "The room has been flooded. All that remains is a pool of glistening water. You can now swim to the door on the southern wall("
                    + (Fore.YELLOW + "southern door")
                    + "\033[39m"
                    + ")."
                )
                player.current_location.shortened_description = (
                    "The room has been flooded. All that remains is a pool of glistening water. You can now swim to the door on the southern wall("
                    + (Fore.YELLOW + "southern door")
                    + "\033[39m"
                    + ")."
                )
                items.ability = False
                print("Press Enter to return")
                input()
