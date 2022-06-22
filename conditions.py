from classes_and_functions import *
from build_board import *
from conditions import *


def check_conditions(player):
    has_mug = False
    has_book = False
    has_chalice = False
    for items in player.inventory:
        if items.name == "mug":
            has_mug = True
        if items.name == "book":
            has_book = True
        if items.name == "chalice":
            has_chalice = True
    if has_mug == True and has_book == True and has_chalice == True:
        print(
            "You have collected all of the magical items. They will be removed from you inventory and replaced with a "
            "magical key")
        for items in player.inventory:
            if items.name == "mug":
                player.inventory.remove(items)
        for items in player.inventory:
            if items.name == "book":
                player.inventory.remove(items)
        for items in player.inventory:
            if items.name == "chalice":
                player.inventory.remove(items)
        magic_key = Item("magic key")
        magic_key.add_description("a magical key. If you go into the Test Room with this key, a new door will appear")
        player.inventory.append(magic_key)

    has_magic_key = False
    for items in player.inventory:
        if items.name == "magic key":
            has_magic_key = True

    if has_magic_key == True and player.current_location.name == "Test_Room":
        player.current_location.shortened_description = "Room with a painting of man on a horse. Door on western " \
                                                        "wall. A new door has appeared on the northern wall. Your " \
                                                        "magical key is glowing "

        North_Room = Room("North_Room")

        # create the long description of the room you just made, and then add it to the room
        description = "This is the room to the North of the Test Room that just opened from the magical key. Its full " \
                      "of treasure. There are chanedliers dangling from the ceiling. There are golden statues " \
                      "everywhere and more gold than a king would have. "
        North_Room.add_long_description(description)

        # create the shortened description for the room, will be displayed when you are visiting a room you have been to
        description = "Room containing a wealth of treasures"
        North_Room.add_shorter_description(description)

        player.current_location.add_adjacent_room("north", North_Room)
        North_Room.add_adjacent_room("south", player.current_location)
