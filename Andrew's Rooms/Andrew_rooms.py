from classes_and_functions import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()

# *** REFERENCE: ROOM TEMPLATE AND COMMENTS FOR ROOM 1-2 CREATED BY ASHWIN THIRUPPATHI ***
# core template in build_board.py

# change items from WHITE to a different color

# This tutorial will show how to build the game board, piece by piece. The game essentially consists
# of a bunch of room objects, filled with a bunch of item objects or enemy objects. The player object
# navigates these rooms until they find the treasure, then the game ends.

# If you take a look at main.py, you will see the gameplay loop is basically
#   1. print the room description
#   2. get the user's typed input
#   3. execute that input
#   4. check to see if any special conditions happened in the game
#   5. check to see if the player has died or won the game

# This loop continues until the game ends. However, before the game can begin the board must be
# built. Each one of use will create our clusters and connect it to the Main Chamber (or whatever we want to call it)
# That is what this tutorial is for.


#  regular items are white
#  consumable items are blue
#  weapon items are magenta
#  rooms are yellow
#  enemies are red


def build_west_one():
    #  STEP 1:  CREATE A ROOM

    # create the room, using the name of the room as the argument
    West_one = Room("Main Chamber")

    # create the long description of the room you just made
    # its important that you add a newline character at appropriate places so that the text does not go too far
    # off of the screen.
    # you need to make sure that items are color coded appropriately. See color key at beginning of this file
    # you can color code using this format " first part of sentence" + (Fore.Color + "item") + '\033[39m' + " rest of the sentence"

    # keep in mind that any item that can be removed from the room (can be picked up) should not be contained in this
    # description. Their description will be in their own e_description of their own object. Notice how the mosaic described
    # in the description is an item that can't be picked up. The rooms that are connected to the current room are also described
    # in the description.

    description = (
        "You find yourself in a dark chamber with coffins strewn about. There are cobwebs everywhere and the walls are covered with dust and mold."
        + "\nSquinting at the coffins to get a better glimpse, you spot three total: One appears"
        + (Fore.WHITE + "wooden")
        + "\033[39m"
        + "and ripped open, one appears"
        + (Fore.WHITE + "metallic")
        + "\033[39m"
        + ", and the third appears to be"
        + (Fore.WHITE + "small")
        + "\033[39m"
        + "and molded over."
        + "\nPerhaps you should take a closer look at the coffins for anything useful?"
        # plan is player can blow this up with dynamite
        + "\nOn the eastern wall, there is a stone boulder blocking what appears to be a doorway ("
        + (Fore.YELLOW + "eastern door")
        + "\033[39m"
        # player needs torch active to see northern room
        + ").\nOn the northern wall, there is an open narrow passage that leads into a pitch black corridor ("
        + (Fore.YELLOW + "northern corridor")
        + "\033[39m"
        + ")."
    )
    # now add the description to the long_description attribute of the room. This is the description that will pop up the first time you enter the room
    West_one.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = (
        "A dark room with a pile of coffins and treaures in the corner. One appears"
        + (Fore.WHITE + "wooden")
        + "\033[39m"
        + "and ripped open, one appears"
        + (Fore.WHITE + "metallic")
        + "\033[39m"
        + ", and the third appears to be"
        + (Fore.WHITE + "small")
        + "\033[39m"
        + "and molded over."
        + "\nPerhaps you should take a closer look at the coffins for anything useful?"
        + "\nOn the eastern wall, there is a stone boulder blocking what appears to be a doorway ("
        + (Fore.YELLOW + "eastern door")
        + "\033[39m"
        + ").\nOn the northern wall, there is an open narrow passage that leads into a pitch black corridor ("
        + (Fore.YELLOW + "northern corridor")
        + "\033[39m"
        + ")."
    )
    # now add the description to the shortened_description attribute of the room
    West_one.add_shorter_description(description)

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # STEP 2: CREATE THE ITEM OBJECTS THAT YOU ARE GOING TO BE PUTTING INTO THE ROOM

    wooden_coffin = Item("wooden coffin")
    # give the wooden coffin a description
    wooden_coffin.add_description(
        "A putrid smell surrounds the coffin, the wood is rotten, and there is a large hole in the cover revealing a half mummified corpse."
    )
    # since the wooden coffin cannot be picked up, we don't need to give it an e_description

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    metallic_coffin = Item("metallic coffin")
    # give the metallic coffin
    metallic_coffin.add_description(
        "The coffin is coated in a metal of some sort... gold... silver.. platinum? It's difficult to discern in the dark, the metal is reflective, greeting you with a blurred silhouette of yourself.\nIt doesn't have a clear opening, a weapon of some sort may be needed to get inside..."
    )
    # since the metallic coffin cannot be picked up, we don't need to give it an e_description

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    small_coffin = Item("small coffin")
    # give the small coffin a description
    small_coffin.add_description(
        "The coffin is similar in construction to the cracked, wooden coffin, albeit its much smaller... wait, does that mean its just a Box?\nIt appears to contain an assortment of golden platewear and a shiny red ruby. Something about the"
        + (Fore.WHITE + "ruby")
        + "\033[39m calls to you..."
    )
    # since the small coffin cannot be picked up, we don't need to give it an e_description

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Now create the red ruby
    red_ruby = Item("red ruby")
    # give the red ruby a description
    red_ruby.add_description(
        "You originally found this shiny red ruby in a room with several coffins, and pucked it out of a smaller coffin (or was it a box???) containing a variety of golden treasures."
    )
    # We need to give this ruby an environmental description, since it can be picked up
    # "red ruby" is colored so the player knows they can interact with the item
    red_ruby.add_env_description(
        "Among the golden treasures resides a shiny "
        + (Fore.WHITE + "red ruby")
        + "\033[39m ."
    )
    # allow ruby to be picked up
    red_ruby.toggle_can_pick_up()

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # STEP 3: ADD THE ITEMS INTO THE ROOM

    # now add the items into the room
    # items are read in the order added
    West_one.add_item_to_room(wooden_coffin)
    West_one.add_item_to_room(metallic_coffin)
    West_one.add_item_to_room(small_coffin)
    West_one.add_item_to_room(red_ruby)

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # STEP 4: CREATE AN ADJACENT ROOM
    # Andrew's room 2

    # Now, we're going to create the room to the east that we mentioned. We're going to add an enemy to the room
    West_two = Room("Andrew room cluster 2")

    # create the long description of the room you just made, and then add it to the room
    description = "You enter a pitch black chamber. Darkness is everywhere. Is it even a chamber? Hallway? Death trap?\n Perhaps there is an item that can provide some light..."

    West_two.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    # don't forget to include you color coding, even for the shortened description
    # also don't forget to describe the door to the room that you come from. In this case is the western door that will
    # lead back into the Main Chamber
    description = (
        "Darkness surrounds you. Perhaps there is an item that can light up the room..."
    )
    West_two.add_shorter_description(description)

    # STEP 5: CREATE ITEMS FOR ADJACENT ROOM

    # create the sarcophagus
    dynamite = Item("dynamite")

    # give the sarcophagus a description
    dynamite.add_description(
        "A stick of explosive dynamite. Looks like its still active, better be careful with fire around it..."
    )

    # We need to give this ruby an environmental description, since it can be picked up
    # "red ruby" is colored so the player knows they can interact with the item
    dynamite.add_env_description(
        "A stick of explosive "
        + (Fore.WHITE + "dynamite")
        + "\033[39m lies on the floor. Better be careful with flames around it... "
    )

    dynamite.toggle_can_pick_up()

    # STEP 7: ADD THE ITEMS AND ENEMY INTO THE ROOM
    West_two.add_item_to_room(dynamite)

    # ------------------------------------------------------------------------------------------------------------------------------
    # create Andrew's room 3
    # JUMPING PUZZLE ROOM, need to implement "jump" action
    West_three = Room("Andrew room cluster 3")

    description = (
        "The dynamite you used earlier has left half this room in shambles. You cough as a cloud of ash and dust greets you.\nThere's rubble and dust everywhere."
        + "Interstingly enough, the explosion seems to have opened a hole in the roof of the chamber towards the northern end, leading to another chamber."
        + "\nThere's a "
        + (Fore.WHITE + "short pillar")
        + "\033[39m"
        + ", a"
        + (Fore.WHITE + "medium pillar")
        + "\033[39m"
        + ", and a"
        + (Fore.WHITE + "box")
        + "\033[39m"
        + "in between a third"
        + (Fore.WHITE + "large pillar")
        + "\033[39m"
        + "leading straight to the"
        + (Fore.YELLOW + "upper northern chamber")
        + "\033[39m"
        + "."
    )

    West_three.add_long_description(description)

    description = (
        "There's rubble and dust everywhere."
        + "A hole in the northern roof of the chamber leads to another room."
        + "\nThere's a "
        + (Fore.WHITE + "short pillar")
        + "\033[39m"
        + ", a"
        + (Fore.WHITE + "medium pillar")
        + "\033[39m"
        + ", and a"
        + (Fore.WHITE + "box")
        + "\033[39m"
        + "in between a third"
        + (Fore.WHITE + "large pillar")
        + "\033[39m"
        + "leading straight to the"
        + (Fore.YELLOW + "upper northern chamber")
        + "\033[39m"
        + "."
    )

    West_three.add_shorter_description(description)

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Create room 3 items

    # create short pillar
    short_pillar = Item("short_pillar")
    # add description
    short_pillar.add_description(
        "A short pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )

    # create medium pillar
    medium_pillar = Item("medium_pillar")
    # add description
    medium_pillar.add_description(
        "A medium pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )

    # create large pillar
    large_pillar = Item("large_pillar")
    # add description
    large_pillar.add_description(
        "A large pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )

    # create box
    box = Item("box")
    # add description
    box.add_description(
        "A box stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )

    # add items to room
    West_three.add_item_to_room(box)
    West_three.add_item_to_room(short_pillar)
    West_three.add_item_to_room(medium_pillar)
    West_three.add_item_to_room(large_pillar)

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Andrew's room #4

    West_four = Room("Andrew room cluster 4")

    description = (
        "A luxurious chamber greets you, the floors and walls are pristine. The mummy janitor clearly spent a lot of time here.\n On each wall, you see an artistic carving."
        + "From afar, you spot what appers to be a bird carving on one side, a snake carving on another, and an alligator on another. \nPedestals lie in front of each carving. Perhaps you should"
        + (Fore.GREEN + "inspect ")
        + "\033[39m"
        + "these drawings further."
    )

    West_four.add_long_description(description)

    description = (
        "On each wall, you see an artistic carving."
        + "From afar, you spot what appers to be a bird carving on one side, a snake carving on another, and an alligator on another. \nPedestals lie in front of each carving. Perhaps you should"
        + (Fore.GREEN + "inspect ")
        + "\033[39m"
        + "these drawings further."
    )

    West_four.add_shorter_description(description)

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Create the item objects we will need for the Python, Alligator, Eagle puzzle to be implemented in conditions.py
    # Player must pick up the python, alligator, and eagle figurines. Player must place the eagle figurine on the Python pedestal, the Alligator figurine on the eagle pedestal, and the Python figurine on the Alligator pedestal to unlock the diamond key.

    # create python wall carving item object
    python_carving = Item("python_carving")
    # add description
    python_carving.add_description(
        "A mystical light illuminates the wall, depicting an ancient carving of a very large Snake, a python."
    )

    # create python figurine object
    python_figurine = Item("python_figurine")
    # add description
    python_figurine.add_description(
        "An ornate figurine of a very large snake, presumably a python or anaconda."
    )

    # create python pedestal
    python_pedestal = Item("python_pedestal")
    # add description
    python_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead python with a prominent skull front and center."
    )

    # Create the item objects we will need for the Python, Alligator, Eagle puzzle
    # create alligator wall carving item object
    alligator_carving = Item("alligator_carving")
    # add description
    alligator_carving.add_description(
        "A mystical light illuminates the wall, depicting an ancient carving of a very large reptile, an alligator."
    )

    # create alligator figurine object
    alligator_figurine = Item("alligator_figurine")
    # add description
    alligator_figurine.add_description(
        "An ornate figurine of a very large reptile, presumably an alligator or crocodile."
    )
    # add environmental description
    alligator_figurine.add_env_description(
        "In one corner of the room there rests a figurine of a powerful lively alligator, resting on a suspicious pedestal of a dead alligator... ironic."
    )

    alligator_figurine.toggle_can_pick_up()

    # create alligator pedestal
    alligator_pedestal = Item("alligator_pedestal")
    # add description
    alligator_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead alligator with a prominent skull front and center."
    )

    # Create the item objects we will need for the Python, Alligator, Eagle puzzle
    # create eagle wall carving item object
    eagle_carving = Item("eagle_carving")
    # add description
    eagle_carving.add_description(
        "A mystical light illuminates the wall, depicting an ancient carving of a very large bird, an eagle."
    )

    # create eagle figurine object
    eagle_figurine = Item("eagle_figurine")
    # add description
    eagle_figurine.add_description(
        "An ornate figurine of a very large eagle, presumably an eagle."
    )
    # add environmental description
    eagle_figurine.add_env_description(
        "In one corner of the room there rests a figurine of a proud tall eagle, resting on a suspicious pedestal of a dead eagle... ironic."
    )

    eagle_figurine.toggle_can_pick_up()

    # create eagle pedestal
    eagle_pedestal = Item("eagle_pedestal")
    # add description
    eagle_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead eagle with a prominent skull front and center."
    )

    """
    # find a way to place this behind door that unlocks after completing puzzle, probably just plop it in player inventory in a conditions loop
    # create diamond key
    diamond_key = Item("diamond_key")
    # add description
    diamond_key.add_description(
        "A shiny key with a large diamond in the handle, this should unlock something special..."
    )
    # add environmental description
    diamond_key.add_env_description(
        "On the ground lies a key with a large diamond in the handle."
    )"""

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # add items to the room
    West_four.add_item_to_room(diamond_key)
    West_four.add_item_to_room(eagle_pedestal)
    West_four.add_item_to_room(eagle_figurine)
    West_four.add_item_to_room(eagle_carving)
    West_four.add_item_to_room(alligator_pedestal)
    West_four.add_item_to_room(alligator_figurine)
    West_four.add_item_to_room(alligator_carving)
    West_four.add_item_to_room(python_pedestal)
    West_four.add_item_to_room(python_figurine)
    West_four.add_item_to_room(python_carving)

    # STEP 8: CONNECT THE MAIN CHAMBER WITH West_two

    # use the add_adjacent_room function to add West_two as the room on the east wall of the Main Chamber
    West_one.add_adjacent_room("east", West_two)
    # since West_two is on the east wall of the main chamber, that means the Main Chamber is on the west all of
    # West_two. So make sure to set it both ways.
    West_two.add_adjacent_room("west", West_one)

    # connect west two, three, and four

    # IMPORTANT NOTE!!!!! :
    # There is one more step that you need to take in order to connect the rooms. The game needs to know that when you
    # are located in the Main Chamber and type in " go to eastern door" that you are going to go into "ash cluster room 1".
    # We need to hard-code that logic in so that "eastern door" is converted into "ash cluster room 1" when we are
    # processing the command. There are a few reasons for this that I can elaborate on more in person. In short, we need
    # to do this because if you have multiple connected rooms, each room is not always going to have the same direction.
    # Ex: the room east of the Main ROom (ash cluster room 1) will not always be east of a different room. So, we need to
    # convert it.  Here's how you will do it.

    # Steps:
    # 1.  go to classes_and_function.py
    # 2.  in the Rooms class, scroll down to the check_room_conditions function
    # 3.  add in your two "if" statements. They should be in this format:

    # ----------------Connecting MAIN CHAMBER to ash cluster room 1 ---------------------------------

    #     if player.current_location.name == "Main Chamber" and user_input[2] == "eastern door":
    #           user_input[2] = "ash cluster room 1"
    #     if player.current_location.name == "ash cluster room 1" and user_input[2] == "western door":
    #           user_input[2] = "Main Chamber"

    # -------------------------------------------------------------------------------------------------

    # STEP 9: ADD THE PLAYER TO THE STARTING LOCATION

    player = Player()

    player.current_location = West_one

    return player

    # STEP 10: CONCLUSION

    # All three of us will use this file to create our final game board using these functions. Once we have done that
    # we can use the Python pickle package to save the player object (and the entire game board with it) into a file.
    # Then, we can just delete this file and load that pickled file for every new game.

    # This tutorial only covered how to create the game board. We will still need to code the conditions that make
    # things actually happen within the game. For example, we can code that if you are holding the magic key of the
    # puzzle, and you type "activate key" while in the room with the puzzle in it, the door will open and you will
    # get the treasure. This will all be covered in the conditions.py file.
