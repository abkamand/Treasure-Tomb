from classes_and_functions import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()

# If you take a look at main.py, you will see the gameplay loop is basically
#   1. print the room description
#   2. get the user's typed input
#   3. execute that input
#   4. check to see if any special conditions happened in the game
#   5. check to see if the player has died or won the game

# This loop continues until the game ends. However, before the game can begin the board must be
# built. Each one of us will create our clusters and connect it to the Main Chamber (or whatever we want to call it)

# regular items that can be picked up = GREEN
# item objects in rooms that can't be picked up = CYAN
#  consumable items = BLUE
#  weapon items = MAGENTA
#  rooms = YELLOW
#  enemies = RED


def build_the_board():
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Andrew Room 1
    # Fairly standard room:
    # Eastern Wall blocked by giant stone boulder than can be blown up by dynamite
    # Northern Wall leads to room 2, which is the darkness puzzle minigame and contains the dynamite

    # create andrew room 1
    West_one = Room("Andrew 1")

    # create long description
    description = (
        "You find yourself in a dark chamber with coffins strewn about. There are cobwebs everywhere and the walls are covered with dust and mold."
        + "\nSquinting at the coffins to get a better glimpse, you spot three total: One appears"
        + (Fore.CYAN + " wooden")
        + "\033[39m"
        + " and ripped open, one is"
        + (Fore.CYAN + " metallic")
        + "\033[39m"
        + ", and the third is"
        + (Fore.CYAN + " small")
        + "\033[39m"
        + " and molded over."
        + "\nPerhaps you should take a closer look at the coffins for anything useful?"
        # darkness puzzle room
        + "\nOn the northern wall, there is an open narrow passage that leads into a pitch black corridor ("
        + (Fore.YELLOW + "northern corridor")
        + "\033[39m"
        + ")."
        + " A giant"
        + (Fore.CYAN + " boulder")
        + "\033[39m"
        + " blocks the way to the eastern chamber.\nYou'll need some way of removing it... explosives maybe?"
    )
    # now add the description to the long_description attribute of the room. This is the description that will pop up the first time you enter the room
    West_one.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = (
        "You enter a dark room with a pile of coffins and treaures in the corner.\nOne appears wooden ("
        + (Fore.CYAN + "wooden coffin")
        + "\033[39m)"
        + " and ripped open, one appears metallic ("
        + (Fore.CYAN + " metallic coffin")
        + "\033[39m)"
        + ", and the third appears to be small ("
        + (Fore.CYAN + "small coffin")
        + "\033[39m)"
        + " and molded over."
        + "\nOn the northern wall, there is a narrow passage that leads into a pitch black corridor ("
        + (Fore.YELLOW + "northern corridor")
        + "\033[39m"
        + "). A "
        + (Fore.CYAN + "boulder")
        + "\033[39m"
        + " blocks the way to the eastern chamber."
    )
    # now add the description to the shortened_description attribute of the room
    West_one.add_shorter_description(description)

    # create wooden coffin
    wooden_coffin = Item("wooden coffin")
    # give the wooden coffin a description
    wooden_coffin.add_description(
        "A putrid smell surrounds the coffin, the wood is rotten, and there is a large hole in the cover revealing a half mummified corpse."
    )
    # since the wooden coffin cannot be picked up, we don't need to give it an e_description

    # create metallic coffin
    metallic_coffin = Item("metallic coffin")
    # give the metallic coffin a description
    metallic_coffin.add_description(
        "The coffin is coated in a metal of some sort... gold... silver.. platinum? It's difficult to discern in the dark, the metal is reflective, greeting you with a blurred silhouette of yourself.\nIt doesn't have a clear opening, a weapon of some sort may be needed to get inside..."
    )

    # create small coffin
    small_coffin = Item("small coffin")
    # give the small coffin a description
    small_coffin.add_description(
        "The coffin is similar in construction to the cracked, wooden coffin, albeit its much smaller... wait, does that mean its just a Box?\nIt appears to contain an assortment of golden platewear."
    )

    # create boulder
    boulder = Item("boulder")
    boulder.add_description = "A giant boulder."
    # boulder.can_activate_ability = True
    boulder.can_contain = True

    # now add the items into the room
    # items are read in the order added
    West_one.add_item_to_room(wooden_coffin)
    West_one.add_item_to_room(metallic_coffin)
    West_one.add_item_to_room(small_coffin)
    West_one.add_item_to_room(boulder)

    # -----------------------------------------------------------------------------------------------------------------------------------------------------
    # Andrew's room 2
    # Pitch black chamber, contains darkness puzzle, player wades through 2d matrix representing location in room until they reach the correct index
    # after completing puzzle, player can pick up dynamite

    # create room 2
    West_two = Room("Andrew 2")

    # create long description + add it to the room
    description = "You enter a pitch black chamber. Darkness is everywhere. Is it even a chamber? Hallway? Death trap?\nYou hear the doorway slam shut behind you."
    West_two.add_long_description(description)

    # create shortened description + add it to the room
    description = "Darkness is everywhere. I need to move!"
    West_two.add_shorter_description(description)

    # required to put in 1 hidden item placeholder to make darkness_puzzle fire off correctly in conditions.py
    item_placeholder = Item("item_placeholder")
    West_two.add_item_to_room(item_placeholder)

    # ------------------------------------------------------------------------------------------------------------------------------
    # Andrew's room 3
    # JUMPING PUZZLE ROOM, need to implement "jump" action
    # Player must jump onto small pillar --> medium pillar --> box --> large pillar in that order to progress to next room

    # create room 3
    West_three = Room("Andrew 3")

    # create long description
    description = (
        "The dynamite you used earlier has left half this room in shambles. You cough as a smoky cloud of ash and dust greet you.\nThere's rubble everywhere."
        + " The explosion seems to have opened a hole "
        + "in the roof of the chamber towards the northern end, leading to another chamber."
        + "\nThere's a "
        + (Fore.CYAN + "short pillar")
        + "\033[39m"
        + ", a"
        + (Fore.CYAN + " medium pillar")
        + "\033[39m"
        + ", and a third"
        + (Fore.CYAN + " large pillar")
        + "\033[39m"
        + " leading straight to the newly revealed chamber."
        + "\nTo the west lies a passage to the coffin room ("
        + (Fore.YELLOW + "western corridor")
        + "\033[39m)."
    )

    West_three.add_long_description(description)

    # create short description
    description = (
        "There's rubble and dust everywhere."
        + "A hole in the northern roof of the chamber leads to another room."
        + "\nThere's a "
        + (Fore.CYAN + "short pillar")
        + "\033[39m"
        + ", a"
        + (Fore.CYAN + " medium pillar")
        + "\033[39m"
        + ", and a third"
        + (Fore.CYAN + " large pillar")
        + "\033[39m"
        + " leading straight to thenewly revealed chamber."
        + "\nTo the west lies a passage to the coffin room ("
        + (Fore.YELLOW + "western corridor")
        + "\033[39m)."
    )

    West_three.add_shorter_description(description)

    # Create room 3 items
    # create short pillar
    short_pillar = Item("short_pillar")
    # add description
    short_pillar.add_description(
        "A short pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )
    # toggle ability for the puzzle in conditions, so can track if player jumps on it
    short_pillar.can_activate_ability = True

    # create medium pillar
    medium_pillar = Item("medium_pillar")
    # add description
    medium_pillar.add_description(
        "A medium pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )
    # toggle ability for the puzzle in conditions, so can track if player jumps on it
    medium_pillar.can_activate_ability = True

    # create large pillar
    large_pillar = Item("large_pillar")
    # add description
    large_pillar.add_description(
        "A large pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )
    # toggle ability for the puzzle in conditions, so can track if player jumps on it
    large_pillar.can_activate_ability = True

    # add items to room
    West_three.add_item_to_room(short_pillar)
    West_three.add_item_to_room(medium_pillar)
    West_three.add_item_to_room(large_pillar)

    # ---------------------------------------------------------------------------------------------------------------------------------------
    # Andrew's room #4
    # Animal/Predator puzzle room
    # Contains an animal carving that depicts the key to solving the puzzle
    # Contains figurines of a python, eagle, and alligator
    # Beneath each is a pedestal which depicts said animal, but dead, with a figurine held on top of said pedestal
    # The player must pickup and place the figurines on the "correct" pedestals to solve the puzzle and receive a diamond key
    # Correct pedestal pairings: Python figurine - Alligator pedestal | Alligator figurine - Eagle pedestal | Eagle figurine - Python pedestal

    # create room 4
    West_four = Room("Andrew 4")

    # create long description
    description = (
        "A luxurious chamber greets you, the floors and walls are pristine. The mummy janitor clearly spent a lot of time here."
        + "From afar, you spot what appears to be an "
        + (Fore.CYAN + "animal carving")
        + "\033[39m on the wall. Perhaps you should inspect this further?"
        + "\nPedestals lie in front of each carving -- an "
        + (Fore.CYAN + "eagle pedestal")
        + "\033[39m"
        + ", a"
        + (Fore.CYAN + " snake pedestal")
        + "\033[39m"
        + ", and an "
        + (Fore.CYAN + "alligator pedestal")
        + "\033[39m"
        + "\nTo the south lies a passage to the coffin room ("
        + (Fore.YELLOW + "southern hole")
        + "\033[39m)."
    )

    West_four.add_long_description(description)

    # create short description
    description = (
        "You spot what appears to be an "
        + (Fore.CYAN + "animal carving")
        + "\033[39m on the wall. Perhaps you should inspect this further?"
        + "\nPedestals lie in front of each carving -- an"
        + (Fore.CYAN + "eagle pedestal")
        + "\033[39m"
        + ", a"
        + (Fore.CYAN + "snake pedestal")
        + "\033[39m"
        + ", and an "
        + (Fore.CYAN + "alligator pedestal")
        + "\033[39m"
        + "\nTo the south lies a passage to the coffin room ("
        + (Fore.YELLOW + "southern hole")
        + "\033[39m)."
    )

    West_four.add_shorter_description(description)

    # Create the item objects we will need for the Python, Alligator, Eagle puzzle to be implemented in conditions.py
    # Player must pick up the python, alligator, and eagle figurines. Player must place the eagle figurine on the Python pedestal,
    # the Alligator figurine on the eagle pedestal, and the Python figurine on the Alligator pedestal to unlock the diamond key.

    # create animal carving that depicts the solution
    animal_carving = Item("python carving")
    # add description
    animal_carving.add_description(
        "A mystical light illuminates the wall, depicting an ancient carving of what appears to be a very large snake choking an alligator,"
        + "an eagle clawing the snake, while the alligator simultaneously snaps at the eagle.\nA predator trifecta ourobouros of sorts... interesting."
    )

    # create python figurine object
    python_figurine = Item("python figurine")
    # add description
    python_figurine.add_description(
        "An ornate figurine of a very large snake, presumably a python or anaconda."
    )
    python_figurine.add_env_description(
        "A figurine of a long and menacing python ("
        + (Fore.GREEN + "python_figurine")
        + "\033[39m)"
        + ", rests on the floor."
    )
    # allow figurine to be picked up
    python_figurine.toggle_can_pick_up()

    # create python pedestal
    python_pedestal = Item("python pedestal")
    # add description
    python_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead python with a prominent skull front and center."
    )
    # allow items sto be placed in the pedestal
    python_pedestal.can_contain = True

    # Create the item objects we will need for the Python, Alligator, Eagle puzzle

    # create alligator figurine object
    alligator_figurine = Item("alligator figurine")
    # add description
    alligator_figurine.add_description(
        "An ornate figurine of a very large reptile, presumably an alligator or crocodile."
    )
    # add environmental description
    alligator_figurine.add_env_description(
        "A figurine of a powerful lively alligator ("
        + (Fore.GREEN + "alligator figurine")
        + "\033[39m)"
        + " rests on the floor."
    )
    # allow figurine to be picked up
    alligator_figurine.toggle_can_pick_up()

    # create alligator pedestal
    alligator_pedestal = Item("alligator pedestal")
    # add description
    alligator_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead alligator with a prominent skull front and center."
    )
    # allow items to be placed in the pedestal
    alligator_pedestal.can_contain = True

    # create eagle figurine object
    eagle_figurine = Item("eagle figurine")
    # add description
    eagle_figurine.add_description(
        "An ornate figurine of a very large eagle, presumably an eagle."
    )
    # add environmental description
    eagle_figurine.add_env_description(
        "A figurine of a proud tall eagle ("
        + (Fore.GREEN + "eagle figurine")
        + "\033[39m)"
        + ", rests on the floor."
    )
    # allow figurine to be picked up
    eagle_figurine.toggle_can_pick_up()

    # create eagle pedestal
    eagle_pedestal = Item("eagle pedestal")
    # add description
    eagle_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead eagle with a prominent skull front and center."
    )
    # allow items to be placed in the pedestal
    eagle_pedestal.can_contain = True

    # add items to the room
    West_four.add_item_to_room(animal_carving)
    West_four.add_item_to_room(eagle_pedestal)
    West_four.add_item_to_room(eagle_figurine)
    West_four.add_item_to_room(alligator_pedestal)
    West_four.add_item_to_room(alligator_figurine)
    West_four.add_item_to_room(python_pedestal)
    West_four.add_item_to_room(python_figurine)

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # Connect all the rooms together

    # room 1 to 3
    West_one.add_adjacent_room("east", West_three)

    # 1 to 2
    West_one.add_adjacent_room("north", West_two)

    # 2 to 1
    West_two.add_adjacent_room("south", West_one)

    # 3 to 4
    West_three.add_adjacent_room("north", West_four)

    # 4 to 3
    West_four.add_adjacent_room("south", West_three)

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
