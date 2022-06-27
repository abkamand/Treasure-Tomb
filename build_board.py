from classes_and_functions import *
import colorama
from colorama import Fore, Back, Style

colorama.init()


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

def build_the_board():
    #  STEP 1:  CREATE A ROOM

    # create the room, using the name of the room as the argument
    Main_Chamber = Room("Main Chamber")

    # create the long description of the room you just made
    # you need to make sure that items are color coded appropriately. See color key at beginning of this file
    # you can color code using this format " first part of sentence" + (Fore.Color + "item") + '\033[39m' + " rest of the sentence"

    # keep in mind that any item that can be removed from the room (can be picked up) should not be contained in this
    # description. Their description will be in their own e_description of their own object. Notice how the mosaic described
    # in the description is an item that can't be picked up. The rooms that are connected to the current room are also described
    # in the description.

    description = "After hours of trekking through the dank and dangerous caverns, you finally arrive at the tomb  you've been looking for.  You walk into a large chamber, filled with ornate decorations and paintings on the ceiling, There appears to be giant " + (
                Fore.WHITE + "mosaic") + '\033[39m' + " on the floor. On the eastern wall, there is a heavy,golden door with a depiction of a eagle on it (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + "). On the northern wall, there is a staircase leading into the depths of the tomb, with a carving of a crocodile at the top of the stairs (" + (
                              Fore.YELLOW + "northern staircase") + '\033[39m' + "). On the western wall, there is another golden door. This one has the image of a sphinx carved into it (" + (
                              Fore.YELLOW + "western door") + '\033[39m' + "). What appears to be the " + (
                              Fore.WHITE + "corpse") + '\033[39m' + " of a man lays in the center of the room."
    # now add the description to the long_description attribute of the room. This is the description that will pop up the first time you enter the room
    Main_Chamber.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = "A vast room full of ornate decorations. There appears to be giant " + (
                Fore.WHITE + "mosaic") + '\033[39m' + " on the floor. On the eastern wall, there is a heavy,golden door with a depiction of a eagle on it (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + "). On the northern wall, there is a staircase leading into the depths of the tomb, with a carving of a crocodile at the top of the stairs (" + (
                              Fore.YELLOW + "northern staircase") + '\033[39m' + "). On the western wall, there is another golden door. This one has the image of a sphinx carved into it (" + (
                              Fore.YELLOW + "western door") + '\033[39m' + "). What appears to be the " + (
                              Fore.WHITE + "corpse") + '\033[39m' + " of a man lays in the center of the room."
    # now add the description to the shortened_description attribute of the room
    Main_Chamber.add_shorter_description(description)

    # STEP 2: CREATE THE ITEM OBJECTS THAT YOU ARE GOING TO BE PUTTING INTO THE ROOM

    # now we are creating the items in the room
    # Items may have abilities, be consumable, or be weapons.
    # For this demonstration, we will create 6 items in the Main Chamber:
    #   1. The mosaic that we described in the description. This item cannot be picked up but can be looked at
    #   2. The corpse that we described in the description. This item cannot be picked up but can be looked at
    #   3. We are going to put a paper note in the room next to the corpse. This item can be picked up and looked at, but has no abilities and is not consumable or a weapon.
    #   4. We are going to put a sword impaled through the body of the corpse. This item can be picked up and is a weapon.
    #   5. We are going to put a torch on the wall of the chamber. This item can be picked up, and has an ability (turn it on or off)
    #   6. We are going to put a bottle of painkillers next to the corpse. These are consumables.

    # Let's start with the mosaic
    mosaic = Item("mosaic")
    # give the mosaic a description
    mosaic.add_description(
        " This mosaic depicts a pharaoh standing on a stage above his subordinates. He his holding a large, red diamond above his head. The crowd amassed at his feet appears to be worshiping him. Above the diamond, there are 3 indentations in the shape of an eagle, a crocodile, and a sphinx. It looks like you could fill in those indentations with the right piece of the mosaic...")
    # since the mosaic cannot be picked up, we don't need to give it an e_description

    # Now let's do the corpse
    corpse = Item("corpse")
    # give the corpse a description
    corpse.add_description(
        "The corpse appears to have been here for a long time. The body has rotten and all that remains is a skeleton. I hope I don't end up like that guy.")
    # since the corpse cannot be picked up, we don't need to give it an e_description

    # Now create the note
    note = Item("note")
    # give the note a description
    note.add_description(
        "This is a note that was laying next to the corpse in the Main Chamber. It says TURN BACK OR YOU WILL DIE! ")
    # We need to give this note an environmental description, since it can be picked up
    # Keep in mind that we need to color code the word "note" in the env description, so the player knows they can interact with it
    note.add_env_description("On the ground next to the corpse there is a " + (
                Fore.WHITE + "note") + '\033[39m' + " written on a piece of paper.")
    # make it so we can pick up the note
    note.toggle_can_pick_up()

    # Now create the sword. This item is a weapon
    sword = Item("sword")
    # give the sword a description. Since it is a weapon, make sure to include its power in the description
    sword.add_description(
        "This is a sword. Kind of outdated, but it looks like it could do some serious damage. Power: 25")
    # give the sword an environmental description since it can be picked up. Make sure to color-code
    sword.add_env_description(
        "There is a " + (Fore.MAGENTA + "sword") + '\033[39m' + " impaled in the skeleton of the corpse.")
    # since the sword is a weapon, we need to set it as a weapon
    sword.toggle_is_weapon()
    # we need to set the power of the weapon according to its description
    sword.set_weapon_power(25)
    # make it so we can pick up the sword
    sword.toggle_can_pick_up()

    # Now create the torch.  This item has an ability you can toggle on or off
    torch = Item("torch")
    # give torch a description
    torch.add_description("This is a torch that can be used to illuminate rooms that are dark")
    # give the torch an environmental description
    torch.add_env_description(
        "There is a " + (Fore.WHITE + "torch") + '\033[39m' + " on the ground next to the corpse.")
    # make it so we can activate its ability
    torch.toggle_can_activate_ability()
    # add the ability_on_description. This is the description that will print when the ability is turned on.
    torch.add_ability_on_description("The torch has been lit and is glowing brightly.")
    # add the ability_off_description. This is the description that will print when the ability is turned off
    torch.add_ability_off_description("The torch has been put out.")
    # make it so we can pick up the torch
    torch.toggle_can_pick_up()

    # Now create the painkillers. This is a consumable
    painkillers = Item("painkillers")
    # give the painkillers a description. Make sure to include the effect on HP in the description
    painkillers.add_description("Looks like a bottle of painkillers. HP +15")
    # give the painkillers an environmental description since they can be picked up
    painkillers.add_env_description(
        "Looks like there is a bottle of " + (Fore.BLUE + "painkillers") + '\033[39m' + " in the corpse's pocket.")
    # set it as a consumable
    painkillers.toggle_can_consume()
    # set the effect of the consumable
    painkillers.set_consumable_effect(15)
    # make it so we can pick up the painkillers
    painkillers.toggle_can_pick_up()

    # STEP 3: ADD THE ITEMS INTO THE ROOM

    # now add the items into the room
    Main_Chamber.add_item_to_room(mosaic)
    Main_Chamber.add_item_to_room(corpse)
    Main_Chamber.add_item_to_room(sword)
    Main_Chamber.add_item_to_room(torch)
    Main_Chamber.add_item_to_room(painkillers)
    Main_Chamber.add_item_to_room(note)

    # STEP 4: CREATE AN ADJACENT ROOM

    # Now, we're going to create the room to the east that we mentioned. We're going to add an enemy to the room
    Ash_Room_1 = Room("ash cluster room 1")

    # create the long description of the room you just made, and then add it to the room
    description = "This is the room to the east of the Main Chamber. It's very dimly lit. There is an open " + (
                Fore.WHITE + "sarcophagus") + '\033[39m' + " in the middle of the room. There is a door on the western wall (" + (
                              Fore.YELLOW + "western door") + '\033[39m' + ")."
    Ash_Room_1.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    # don't forget to include you color coding, even for the shortened description
    # also don't forget to describe the door to the room that you come from. In this case is the western door that will
    # lead back into the Main Chamber
    description = "Room containing an open " + (Fore.WHITE + "sarcophagus") + '\033[39m' + ". There is a door on the western wall (" + (Fore.YELLOW + "western door") + '\033[39m' + ")."
    Ash_Room_1.add_shorter_description(description)

    # STEP 5: CREATE ITEMS FOR ADJACENT ROOM

    # create the sarcophagus
    sarcophagus = Item("sarcophagus")

    # give the sarcophagus a description
    sarcophagus.add_description("The sarcophagus is open. Whatever was inside is now gone")
    # since we can't pick it up we don't need an env description

    # STEP 6: CREATE THE ENEMY

    # create the mummy
    mummy = Enemy("mummy")
    # add description
    mummy.add_description("A terrifying mummy wrapped in cloth. It is very scary and want to eat you")
    # add an environmental description
    mummy.add_env_description(
        "A " + (Fore.RED + "mummy") + '\033[39m' + " is standing in the middle of the room by the sarcophagus. It was probably his. He begins sauntering towards you.")
    # set its HP
    mummy.set_HP(100)
    # set its power. This is how much damage you will take if he hits you
    mummy.set_power(50)

    # STEP 7: ADD THE ITEMS AND ENEMY INTO THE ROOM

    Ash_Room_1.add_item_to_room(sarcophagus)
    Ash_Room_1.add_enemy_to_room(mummy)

    # STEP 8: CONNECT THE MAIN CHAMBER WITH Ash_Room_1

    # use the add_adjacent_room function to add Ash_Room_1 as the room on the east wall of the Main Chamber
    Main_Chamber.add_adjacent_room("east", Ash_Room_1)
    # since Ash_Room_1 is on the east wall of the main chamber, that means the Main Chamber is on the west all of
    # Ash_Room_1. So make sure to set it both ways.
    Ash_Room_1.add_adjacent_room("west", Main_Chamber)

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

    player.current_location = Main_Chamber

    return player

    # STEP 10: CONCLUSION

    # All three of us will use this file to create our final game board using these functions. Once we have done that
    # we can use the Python pickle package to save the player object (and the entire game board with it) into a file.
    # Then, we can just delete this file and load that pickled file for every new game.

    # This tutorial only covered how to create the game board. We will still need to code the conditions that make
    # things actually happen within the game. For example, we can code that if you are holding the magic key of the
    # puzzle, and you type "activate key" while in the room with the puzzle in it, the door will open and you will
    # get the treasure. This will all be covered in the conditions.py file.