from classes_and_functions import *
import colorama
from colorama import Fore, Back, Style
colorama.init()


def build_the_board():

    # create the room, using the name of the room as the argument
    Test_Room = Room("Test_Room")


#    painting_text = Fore.BLUE + "painting"
#    West_Room_door_text = Fore.RED + "West_Room"
    # create the long description of the room you just made, and then add it to the room
    description = "This is a test room. On the eastern wall there is a " + (Fore.BLUE + "painting") + '\033[39m' + " of a man on a horse. There is a door on the western wall (" + (Fore.RED + "West_Room") + '\033[39m' + "). This is the long-form description that will appear the first time the player is in the room "
    Test_Room.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = "Room with a " + (Fore.BLUE + "painting") + '\033[39m' + " of man on a horse. Door on western wall (" + (Fore.RED + "West_Room") + '\033[39m' + ")."
    Test_Room.add_shorter_description(description)

    # need to create the Item objects first before they can be added to the room

    # first we will create the book
    book = Item("book")

    # give the book a description
    book.add_description("This is a fake description for the book that was found on the table")
    # give the book an environmental description
    book.add_env_description("There is a book laying on a table")
    # make it so we can pick up the book
    book.toggle_can_pick_up()

    # now create the coffee mug
    mug = Item("mug")

    # give mug a description
    mug.add_description("This is a test description for the coffee mug in the test room. Mug with carving of a dog on "
                        "it")
    # give the book an environmental description
    mug.add_env_description("There is a mug sitting on the table in the room")
    # make it so we can pick up the mug
    mug.toggle_can_pick_up()

    # now create the painting
    painting = Item("painting")

    # give the painting a description
    painting.add_description("This is a test description for the painting of a man on a horse in the test room")
    # we don't need to give the painting an environmental description since we can't pick it up

    # now create the torch
    torch = Item("torch")

    # give torch a description
    torch.add_description("This is a torch that can be used to illuminate rooms that are dark")
    # give the torch an environmental description
    torch.add_env_description("There is a torch on the ground next to the table.")
    # make it so we can pick up the torch
    torch.toggle_can_pick_up()
    # make it so we can activate ability
    torch.can_activate_ability = True
    torch.ability_on_description = "The torch has been lit and is glowing brightly"
    torch.ability_off_description = "The torch has been put out"



  # now create a sword
    sword = Item("sword")

    # give sword a description
    sword.add_description("This is a sword that looks like it can do some damage")
    # give the sword an environmental description
    sword.add_env_description("There is a sword hanging up on the wall next to the painting")
    # make it so we can pick up the sword
    sword.toggle_can_pick_up()
    # make the sword object a weapon
    sword.is_weapon = True
    # give the weapon some power
    sword.weapon_power = 25



    # now add the items into the room
    Test_Room.add_item_to_room(book)
    Test_Room.add_item_to_room(mug)
    Test_Room.add_item_to_room(painting)
    Test_Room.add_item_to_room(torch)
    Test_Room.add_item_to_room(sword)









    # create the room to the west of the test room
    West_Room = Room("West_Room")



    # create the long description of the room you just made, and then add it to the room
    description = "This is the room to the west of the test room. There is a sarcophagus in the middle of the room. " \
                  "It looks too heavy to carry. The room is full of gold and smells terrible." \
                  " There are pictures carved in the walls depicting something."
    West_Room.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = "Room containing a sarcophagus and carvings in the wall"
    West_Room.add_shorter_description(description)

    # need to create the Item objects first before they can be added to the room

    # first we will create the sarcophagus
    sarcophagus = Item("sarcophagus")

    # give the sarcophagus a description
    sarcophagus.add_description("This is a fake description for the sarcophagus that was found in the western room")
    # since we can't pick it up we don't need an env description

    # now create the gold chalice
    chalice = Item("chalice")

    # give chalice a description
    chalice.add_description(
        "This is a test description for the chalice that you can pick up in the western room. Made of solid gold and "
        "found next to the sarcophagus")
    # give the book an environmental description
    chalice.add_env_description("There is a chalice on the ground next to the sarcophagus. Looks like solid gold")
    # make it so we can pick up the mug
    chalice.toggle_can_pick_up()

    # now create the wall carvings
    carvings = Item("carvings")

    # give the carvings a description
    carvings.add_description(
        "This is a test description for the wall carvings. The carvings depict a pharaoh holding up a glowing "
        "diamond. People are worshipping him")
    # we don't need to give the carvings an environmental description since we can't pick it up




    # now add the items into the room
    West_Room.add_item_to_room(sarcophagus)
    West_Room.add_item_to_room(chalice)
    West_Room.add_item_to_room(carvings)

    # now we need to connect the Test Room and West Room
    Test_Room.add_adjacent_room("west", West_Room)
    West_Room.add_adjacent_room("east", Test_Room)


    # create the enemy

    mummy = Enemy("mummy")

    # add description

    mummy.add_description("A terrifying mummy wrapped in cloth. It is very scary and want to eat you")

    # add e description

    mummy.add_env_description("A mummy is standing in the middle of the room by the sarcophagus. It was probably his.")

    # set its HP

    mummy.set_HP(100)

    # set its power

    mummy.set_power(50)


    # put the mummy in the West Room

    West_Room.add_enemy_to_room(mummy)



    # now add the player to the room
    player = Player()

    player.current_location = Test_Room

    return player
