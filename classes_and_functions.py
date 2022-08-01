import pickle
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()


class Room:
    def __init__(self, name):
        """
        Initialize and instance of a Room. Each room has a name, a long description, and a short description. It has a list
        of item that are found in the room, which are in in_room. These will all be Item objects. It has a list of enemies
        that are in the room, if any. These will be enemy objects. It will also have a field for each wall, which will
        either be empty or another Room object. Finally, it will have a True or False value for whether the room was visited
        or not.
        """
        self.name = name
        self.long_description = None
        self.shortened_description = None
        # this is for the items in the room
        self.in_room = []
        # this is for the enemies in the room
        self.enemies = []
        self.north_wall = None
        self.east_wall = None
        self.west_wall = None
        self.south_wall = None
        self.center = None
        self.visited = False

    def build_description(self):
        """This function builds the correct description that will be displayed when the player walks into
        a room. First, it will check if the player has visited this room before. It he hasn't, it will display the
        long form description. If he has, it will print the shorter description. It will then iterate through
         every item in the room, and check whether or not that item has been dropped on the floor. If the item has
         not been dropped on the floor (meaning it is in its original place), it will then read the item's description.
         It will list all of the items that are on the floor and set the room as visited. Finally, it will list
         the enemies in the room and their environmental description.
        """

        # print the long or short description
        if not self.visited:
            print(self.long_description)
        if self.visited:
            print(self.shortened_description)

        # print the items in the room that are not on the floor (original place)
        for items in self.in_room:
            if not items.on_floor and items.can_pick_up:
                print(items.e_description)

        # print the items on the floor
        floor_items = []
        for items in self.in_room:
            if items.on_floor:
                floor_items.append(items.name)
        if len(floor_items) > 0:
            print("These items are on the floor:")
            for items in self.in_room:
                if items.on_floor:
                    if items.is_weapon:
                        print((Fore.MAGENTA + items.name) + "\033[39m")
                    elif items.can_consume:
                        print((Fore.BLUE + items.name) + "\033[39m")
                    else:
                        print((Fore.WHITE + items.name) + "\033[39m")

        # print the enemies in the room
        for enemies in self.enemies:
            if not enemies.is_dead:
                print(enemies.e_description)

        # set the room as visited
        self.visited = True

    def take_input(self, player):
        """
        After the player reads the description, he will have to take an action. This method receives the input that the
        user will type, and splits it into a list of strings. This list of strings will be returned to main.py, where it
        will be used in a function to execute the command that was typed
        """
        user_input = input()
        while len(user_input) == 0:
            print("invalid command")
            input("Press Enter to return")
            user_input = input()
        user_input = user_input.split()
        if len(user_input) > 2 and user_input[0] == "go" and user_input[1] == "to":
            if len(user_input) == 4:
                user_input[2] = str(user_input[2]) + " " + str(user_input[3])
                user_input.remove(user_input[3])
            # the same concept described above applies for commands that make up 5 words. Example: pick up red rusted sword
            if len(user_input) == 5:
                user_input[2] = (
                    str(user_input[2])
                    + " "
                    + str(user_input[3])
                    + " "
                    + str(user_input[4])
                )
                user_input.remove(user_input[4])
            user_input = self.check_room_conditions(player, user_input)
        return user_input

    def check_room_conditions(self, player, user_input):

        # ----------------Connecting MAIN CHAMBER to ash cluster room 1 ---------------------------------

        if (
            player.current_location.name == "Main Chamber"
            and user_input[2] == "eastern door"
        ):
            user_input[2] = "Water Room"
        if (
            player.current_location.name == "Water Room"
            and user_input[2] == "western door"
        ):
            user_input[2] = "Main Chamber"
        # ----------------Connecting Andrew 1 to Andrew 2 ---------------------------------
        if (
            player.current_location.name == "Andrew 1"
            and user_input[2] == "northern corridor"
        ):
            user_input[2] = "Andrew 2"
        if (
            player.current_location.name == "Andrew 2"
            and user_input[2] == "southern corridor"
            or user_input[2] == "back"
        ):
            user_input[2] = "Andrew 1"
        # ----------------Connecting Andrew 1 to Andrew 3 ---------------------------------
        if (
            player.current_location.name == "Andrew 1"
            and user_input[2] == "eastern corridor"
        ):
            user_input[2] = "Andrew 3"
        if (
            player.current_location.name == "Andrew 3"
            and user_input[2] == "western corridor"
            or user_input[2] == "back"
        ):
            user_input[2] = "Andrew 1"
        # ----------------Connecting Andrew 3 to Andrew 4 ---------------------------------
        # this should be tied to jumping puzzle
        if (
            player.current_location.name == "Andrew 3"
            and user_input[2] == "northern corridor"
        ):
            user_input[2] = "Andrew 4"
        if (
            player.current_location.name == "Andrew 4"
            and user_input[2] == "southern hole"
            or user_input[2] == "back"
        ):
            user_input[2] = "Andrew 3"

        return user_input

    def add_long_description(self, description):
        """
        As per the requirements, when a player enters a room for the first time they will be presented with the long-form
        description. However, when the player navigates back to the same room, they will see a shorter description. This
        method is used when a room has been visited in order to change the description to a shorter one
        """
        self.long_description = description

    def add_shorter_description(self, shorter_description):
        """
        As per the requirements, when a player enters a room for the first time they will be presented with the long-form
        description. However, when the player navigates back to the same room, they will see a shorter description. This
        method is used when a room has been visited in order to change the description to a shorter one
        """
        self.shortened_description = shorter_description

    def add_item_to_room(self, item):
        """
        This adds an item to a room.
        """
        self.in_room.append(item)

    def add_enemy_to_room(self, enemy):
        """
        Adds an enemy object to a room
        """
        self.enemies.append(enemy)

    def remove_item_from_room(self, item):
        """
        This removes an item from a room when Player picks up an item.
        """
        if item in self.in_room:
            self.in_room.remove(item)

    def add_adjacent_room(self, direction, room):
        """
        This method adds an adjacent room to a Room object. The wall direction must be specified, and the Room object
        that is the adjacent room must be passed as the argument
        """
        if direction == "north":
            self.north_wall = room
        if direction == "south":
            self.south_wall = room
        if direction == "west":
            self.west_wall = room
        if direction == "east":
            self.east_wall = room
        if direction == "center":
            self.center = room


class Player:
    """
    Initialize an instance of a Player object. The person has a name and an inventory full of Item objects. The current
    location is kept track of. The death status is also kept track of. The player's Health Points (HP) is set to 100.
    The currently equipped weapon is set to None. This will always be an Item object that is a weapon. When the player has
    won the game, self.has_won will be set to True.
    """

    def __init__(self):
        self.name = None
        self.inventory = []
        self.current_location = None
        self.is_dead = False
        self.HP = 100
        self.equipped = None
        self.has_won = False
        self.exit = False
        self.in_combat = None

    def execute_input(self, user_input, player, save_name):
        """This function parses the input that the use typed in."""
        # ----------------------------------------------------------------------------------------------------------------------------
        # checking if input is at least one word
        if len(user_input) < 1:
            print("Please enter an input")
            input("Press Enter to return")
            return

        # ----------------------------------- PUT ___ IN ____  -------------------------------------------------------
        # if we are doing command "put ___ in ___" we need to do some special parsing of the command to make it work
        o1 = None
        o2 = None
        i1 = None
        i2 = None
        if user_input[0] == "put":
            new_ui = user_input[0]
            for i in range(1, len(user_input)):
                new_ui = new_ui + " " + user_input[i]

            new_ui = new_ui.split(" in ")
            o1 = new_ui[0]
            o2 = new_ui[1]
            o1 = o1[4:]

            for items in self.inventory:
                if items.name == o1:
                    i1 = items
            for items in self.current_location.in_room:
                if items.name == o1:
                    i1 = items
            for items in self.inventory:
                if items.name == o2 and items.can_contain == True:
                    items.contains.append(i1)
                    for i in self.inventory:
                        if i.name == o1:
                            self.inventory.remove(i)
                    for p in self.current_location.in_room:
                        if p.name == o1:
                            self.current_location.in_room.remove(p)
                    print("Done")
                    input("Press Enter to return")
                    return
            for items in self.current_location.in_room:
                if items.name == o2 and items.can_contain == True:
                    items.contains.append(i1)
                    for i in self.inventory:
                        if i.name == o1:
                            self.inventory.remove(i)
                    for p in self.current_location.in_room:
                        if p.name == o1:
                            self.current_location.in_room.remove(p)
                    print("Done")
                    input("Press Enter to return")
                    return
            print("action not permitted")
            return

        # if the command is more than 3 words, for example "pick up red sword". In this case, user_input[2] = "red"
        # and user_input[3] = "sword". For the purposes of this function, we need to combine these to make "red sword" in
        # user_input[2]
        if len(user_input) == 4:
            user_input[2] = str(user_input[2]) + " " + str(user_input[3])

        # the same concept described above applies for commands that make up 5 words. Example: pick up red rusted sword
        if len(user_input) == 5:
            user_input[2] = (
                str(user_input[2]) + " " + str(user_input[3]) + " " + str(user_input[4])
            )

        # ------------------------------------------SAVE GAME-------------------------------------------------------------------------
        # when user enters 'savegame' the game state is pickled into a file
        if user_input[0] == "savegame":
            self.save_game(player, save_name)
            print("game saved")
            input("Press Enter to return to game")
            return
        # ---------------------------------------- HELP -------------------------------------------------------------------------
        # when user enters 'help' the help screen is printed
        if user_input[0] == "help":
            self.help_screen()
            input("Press Enter to return to game")
            return

        # ---------------------------------------- EXIT -----------------------------------------------------------------------
        # if player wants to exit the game without using the stop button on Python
        if user_input[0] == "exit":
            self.exit = True
            return

        # -----------------------------------------INVENTORY--------------------------------------------------------------------------
        # when the user enters 'inventory' a list of the items in the inventory is displayed
        if user_input[0] == "inventory":
            self.look_at_inventory()
            input("Press Enter to return")
            return

        # ----------------------------------------------- HP ---------------------------------------------------------
        if user_input[0] == "HP":
            print(" HP : " + str(self.HP))
            input("Press Enter to return")
            return
        # --------------------------------------------------------------------------------------------------------------

        # since we have made it past all of the one-word commands, we know that if the user enters any other one-word
        # commands, it will be an invalid input
        if len(user_input) < 2:
            print("invalid input")
            input("Press Enter to return")
            return

        # ----------------------------------------LOOK AT--------------------------------------------------------------------------
        # when the user enters 'look at item', first the inventory is checked for that item, and then the room is checked for
        # that item. If it is found, the item's description is printed.
        if user_input[0] == "look" and user_input[1] == "at":
            if len(user_input) < 3:
                print("invalid input")  # if the user types only "look at" its invalid
                input("Press Enter to return")
                return
            for (
                items
            ) in (
                self.inventory
            ):  # first iterate through inventory to see if you can look at an item
                if items.name == user_input[2]:
                    print(items.description)
                    if items.can_contain == True and len(items.contains) > 0:
                        print(items.container_type + " :")
                        for x in items.contains:
                            print(x.name)
                    input("Press Enter to return")
                    return
            for (
                items
            ) in (
                self.current_location.in_room
            ):  # then check the room to see if the item is there
                if items.name == user_input[2]:
                    print(items.description)
                    if items.can_contain == True and len(items.contains) > 0:
                        print(items.container_type + " :")
                        for x in items.contains:
                            print(x.name)
                    input("Press Enter to return")
                    return
            for (
                enemies
            ) in (
                self.current_location.enemies
            ):  # check to see if you are looking at an enemy in the room
                if enemies.name == user_input[2]:
                    print(enemies.description)
                    print("HP: " + str(enemies.HP))  # if so, print out its HP
                    input("Press Enter to return")
                    return
            print("Not found in current room or inventory")
            input("Press Enter to return to game")
            return
        # --------------------------------------PICK UP ---------------------------------------------------------------------------
        # checks room for item to pick up
        if user_input[0] == "pick" and user_input[1] == "up":
            if len(user_input) < 3:  # check for invalid input
                print("invalid input")
                input("Press Enter to return")
                return
            for (
                items
            ) in (
                self.current_location.in_room
            ):  # check current room for item to pick up
                if items.can_pick_up == True and items.name == user_input[2]:
                    self.add_to_inventory(items)
                    input("Press Enter to return")
                    return
                if items.name == user_input[2] and items.can_pick_up == False:
                    print(
                        "item cannot be picked up"
                    )  # lets user know that the item can't be picked up
                    input("Press Enter to return")
                    return
            for items in self.current_location.in_room:
                if items.can_contain and len(items.contains) > 0:
                    for i in items.contains:
                        if i.name == user_input[2]:
                            self.add_to_inventory(i)
                            items.contains.remove(i)
                            input("Press Enter to return")
                            return
            for items in self.inventory:
                if items.can_contain and len(items.contains) > 0:
                    for i in items.contains:
                        if i.name == user_input[2]:
                            self.add_to_inventory(i)
                            items.contains.remove(i)
                            input("Press Enter to return")
                            return

            print("Item not found")
            input("Press Enter to return")
            return
        # ----------------------------------------------DROP---------------------------------------------------------------------------
        # if the user enters 'drop item', the items is dropped from inventory onto the floor. It is added to the room's
        # item list, and its on_floor status is toggled
        if user_input[0] == "drop":
            for items in self.inventory:
                if items.can_pick_up == True and items.name == user_input[1]:
                    self.drop_item(items)
                    input("Press Enter to return")
                    return

        # -------------------------------------------ACTIVATE-------------------------------------------------------------------------
        # if the user enters 'activate item' this will toggle the item's ability attribute to True or False. Whatever the
        # consequences of this action are will be determined by conditions.py file. First, we will check to see if the item
        # is in your inventory. Then we will check to see if the item is in the room.
        if user_input[0] == "activate" or user_input[0] == "deactivate":
            for (
                items
            ) in (
                self.inventory
            ):  # we are checking the inventory to see if you are activating one of your items
                if items.name == user_input[1] and items.can_activate_ability == True:
                    items.toggle_ability()  # toggle whether the ability is on or off
                    if items.ability:
                        if items.ability_on_description is not None:
                            print(
                                items.ability_on_description
                            )  # print the description when the ability is turned on or
                    if not items.ability:
                        if items.ability_off_description is not None:
                            print(items.ability_off_description)
                    input("Press Enter to return")
                    return
                if items.name == user_input[1] and items.can_activate_ability == False:
                    print(
                        items.name + " cannot be activated"
                    )  # name matches but item does not have an ability
                    input("Press Enter to return")
                    return
            for (
                items
            ) in (
                self.current_location.in_room
            ):  # this does the same as above but for items in the room, for example, if you want to pull a lever or press a button
                if items.name == user_input[1] and items.can_activate_ability == True:
                    items.toggle_ability()
                    if items.ability:
                        if items.ability_on_description is not None:
                            print(items.ability_on_description)
                    if not items.ability:
                        if items.ability_off_description is not None:
                            print(items.ability_off_description)
                    input("Press Enter to return")
                    return
                if items.name == user_input[1] and items.can_activate_ability == False:
                    print(items.name + " cannot be activated")
                    input("Press Enter to return")
                    return
            for enemies in self.current_location.enemies:
                if (
                    enemies.name == user_input[1]
                    and enemies.can_activate_ability == True
                ):
                    enemies.toggle_ability()
                    if enemies.ability:
                        if enemies.ability_on_description is not None:
                            print(enemies.ability_on_description)
                    if not enemies.ability:
                        if enemies.ability_off_description is not None:
                            print(enemies.ability_off_description)
                    input("Press Enter to return")
                    return
                if (
                    enemies.name == user_input[1]
                    and enemies.can_activate_ability == False
                ):
                    print(enemies.name + " cannot be activated")
                    input("Press Enter to return")
                    return

        # -----------------------------------CONSUME----------------------------------------------------------------------------
        # this will let you consume a consumable item only if it is in your inventory. If there are, it will have
        # an effect on your HP
        if user_input[0] == "consume":
            for items in self.inventory:
                if (
                    items.name == user_input[1] and items.can_consume == True
                ):  # check if the items name matches and is consumable
                    self.HP = self.HP + items.HP_gain_or_loss  # add or lose your HP
                    print("consumed " + items.name)
                    self.inventory.remove(items)  # remove consumable from you inventory
                    input("Press Enter to return")
                    return
                if items.name == user_input[1] and items.can_consume == False:
                    print(items.name + " cannot be consumed")
                    input("Press Enter to return")
                    return

        # ---------------------------- EQUIP ------------------------------------------------------------------------------
        # this will equip a weapon to the player with a power that will take away from an enemy HP

        if user_input[0] == "equip":
            for items in self.inventory:
                if (
                    items.name == user_input[1] and items.is_weapon == True
                ):  # check name matches and if it is a weapon
                    self.equipped = items  # equip it
                    print("equipped " + items.name)
                    input("Press Enter to return")
                    return
                if items.name == user_input[1] and items.is_weapon == False:
                    print(items.name + " is not a weapon")
                    input("Press Enter to return")
                    return

        # --------------------------UNEQUIP ---------------------------------------------------------------------------

        if len(user_input) < 2:
            print("invalid command")
            input("Press Enter to return")
            return
        if user_input[0] == "unequip":
            if user_input[1] == self.equipped.name:
                print("Unequipped " + self.equipped.name)
                self.equipped = None
                input("Press Enter to return")
                return
            if user_input[1] != self.equipped.name:
                print("item not equipped")
                input("Press Enter to return")
                return

        # -------------------------- ATTACK -----------------------------------------------------------------------------
        # this will use whatever the player has equipped to attack and enemy object. If nothing is equipped the player
        # will fight with his hands, which will do very little damage

        if user_input[0] == "attack":
            if self.in_combat is None:
                for enemies in self.current_location.enemies:
                    if enemies.name == user_input[1]:
                        self.in_combat = enemies
                        print("You are now fighting the " + enemies.name + "!")
            for enemies in self.current_location.enemies:
                if enemies.name == user_input[1]:
                    if self.equipped is not None:
                        enemies.HP = (
                            enemies.HP - self.equipped.weapon_power
                        )  # enemy takes damage equal to weapon power
                        print(
                            enemies.name
                            + " took "
                            + str(self.equipped.weapon_power)
                            + " damage! HP: "
                            + str(enemies.HP)
                        )
                        if (
                            enemies.HP == 0 or enemies.HP < 0
                        ):  # if enemy HP is 0 or less, it dies
                            print(enemies.name + " was defeated!")
                            enemies.is_dead = True
                            self.in_combat = None
                            input("Press Enter to return")
                            return
                        input("Press Enter to return")
                        return
                    if self.equipped is None:
                        enemies.HP = enemies.HP - 5  # unarmed combat damage
                        print(enemies.name + " took 5 damage! HP: " + str(enemies.HP))
                        if enemies.HP == 0 or enemies.HP < 0:
                            print(enemies.name + " was defeated!")
                            enemies.is_dead = True
                            self.in_combat = None
                            input("Press Enter to return")
                            return
                        input("Press Enter to return")
                        return

        # --------------------------------------------GO TO ----------------------------------------------------------------------------

        # If the user enters "go to room" they will enter a new room. This will check to see if that room exists on the
        # specified wall and then check if the name of the room matches the input. If it does, the current location will
        # be changed to the new room
        if user_input[0] == "go" and user_input[1] == "to":
            if len(user_input) < 3:
                print("invalid input")
                input("Press Enter to return")
                return
            if (
                self.current_location.north_wall is not None
                and user_input[2] == self.current_location.north_wall.name
            ):
                direction = "north"
                self.move_to_new_room(direction)
                return
            elif (
                self.current_location.south_wall is not None
                and user_input[2] == self.current_location.south_wall.name
            ):
                direction = "south"
                self.move_to_new_room(direction)
                return
            elif (
                self.current_location.east_wall is not None
                and user_input[2] == self.current_location.east_wall.name
            ):
                direction = "east"
                self.move_to_new_room(direction)
                return
            elif (
                self.current_location.west_wall is not None
                and user_input[2] == self.current_location.west_wall.name
            ):
                direction = "west"
                self.move_to_new_room(direction)
                return
            elif (
                self.current_location.center is not None
                and user_input[2] == self.current_location.center.name
            ):
                direction = "center"
                self.move_to_new_room(direction)
                return
            else:
                print("room does not exist")
                input("Press Enter to return")
                return
        print("invalid command")

    def save_game(self, player, save_name):
        """
        Saves the game. Uses Python pickle package to save the player object into a file. That file will be used
        later to load the game data
        """
        new_save_name = save_name + ".pickle"
        with open(new_save_name, "wb") as f:
            pickle.dump(player, f)
        return

    def help_screen(self):
        """
        When the player types in "help", this help screen is displayed
        """
        print("\n")
        print("Welcome to Treasure Tomb, a text-based treasure hunting game!")
        print(
            "The objective of this game is to get to the treasure by making your way through a dangerous, haunted tomb."
        )
        print(
            "If you make the wrong decision and your HP goes to 0, you will die, so be careful!"
        )
        print("\n")
        print(
            "In each room, you will be presented with a description of your surroundings."
        )
        print("Items and Enemies that may be interacted with are color-coded: ")
        print("regular items are white")
        print("consumable items are blue")
        print("weapon items are magenta")
        print("rooms are yellow")
        print("enemies are red")
        print("\n")
        print(
            "You may interact with certain objects in your environment using player-inputted commands."
        )
        print("Warning: commands must be inputted exactly as they are listed here")
        print("List of supported commands:")
        print("savegame   : saves the current state of the game")
        print("help    : shows this help screen")
        print("inventory    : shows you the items in your inventory")
        print("exit     : exits the game. Make sure to save before using this command")
        print("HP     : shows you your current HP")
        print(
            "look at _____  :  Allows you to see a description of any item or enemy in the room."
        )
        print(
            "pick up _____  : Allows you to pick up an item, as long as that item can be picked up. It "
            "will be placed in your inventory"
        )
        print(
            "go to _____ : Allows you to go into a new room, which will be highlighted yellow"
        )
        print(
            "drop _____   : Allows you to drop an item from your inventory onto the floor"
        )
        print(
            "activate ______   : Allows you to 'turn on' any item in your current room or in your inventory."
        )
        print(
            "deactivate _______ : Allows you to 'turn off' any item in your current room or inventory "
        )
        print(
            "equip ______    :  Allows you to equip an item, only if it is a weapon. Equipped weapons can be used to attack enemies"
        )
        print(
            "unequip ______  : Allows you to unequip and item. You will be unarmed unless you equip a weapon."
        )
        print(
            "attack ______  :   Must be directed towards an enemy, which is highlighted in red. If a weapon is not equipped, you will attack with your hands"
        )
        print(
            "consume _____ :  Allows you to consume a consumable item, which is highlighted in blue. Consumable items have an effect on your HP  "
        )

    def add_to_inventory(self, item):
        """
        Adds an item to a player's inventory. Removes it from the current room
        """
        if not item.can_pick_up:
            print("cannot pick up item")
            return
        self.inventory.append(item)
        print("picked up " + item.name)
        if item.on_floor:
            item.toggle_on_floor()
        self.current_location.remove_item_from_room(item)

    def drop_item(self, item):
        """
        Drops an item from the inventory and adds it to the current room
        """
        if item in self.inventory:
            if not item.on_floor:
                item.toggle_on_floor()  # item is now on the floor
            self.current_location.add_item_to_room(item)  # item is now in the room
            self.inventory.remove(item)
            if (
                self.equipped == item
            ):  # if you are dropping a weapon item you have equipped, you are now unarmed
                self.equipped = None
            print("dropped " + item.name)
        else:
            print("item not in inventory")

    def look_at_inventory(self):
        """
        Prints all of the items in your inventory
        """
        for items in self.inventory:
            print(items.name)

    def move_to_new_room(self, direction):
        """
        This function is used when the Player enters one of the adjacent rooms. It sets the player's current location
        to the new room.
        """
        if direction == "north":
            self.current_location = self.current_location.north_wall
        if direction == "south":
            self.current_location = self.current_location.south_wall
        if direction == "east":
            self.current_location = self.current_location.east_wall
        if direction == "west":
            self.current_location = self.current_location.west_wall
        if direction == "center":
            self.current_location = self.current_location.center

    def fight(self, enemy):
        odds = random.randint(1, 4)
        if odds == 1:
            print(enemy.move_1)
            print("You took " + str(enemy.move_1_power) + " damage!")
            self.HP = self.HP - enemy.move_1_power
            print("HP: " + str(self.HP))
        if odds == 2:
            print(enemy.move_2)
            print("You took " + str(enemy.move_2_power) + " damage!")
            self.HP = self.HP - enemy.move_2_power
            print("HP: " + str(self.HP))
        if odds == 3:
            print(enemy.move_3)
            print("You took " + str(enemy.move_3_power) + " damage!")
            self.HP = self.HP - enemy.move_3_power
            print("HP: " + str(self.HP))
        if odds == 4:
            print(enemy.move_4)
            print("You took " + str(enemy.move_4_power) + " damage!")
            self.HP = self.HP - enemy.move_4_power
            print("HP: " + str(self.HP))
        if self.HP == 0 or self.HP < 0:
            print("You have died")
            print("GAME OVER")


class Item:
    """
    Initialize an instance of an Item object. Each item has a name, description, and an e_description. The description
    will be printed when the player looks at the item. The e_description is the description that will be printed when
    the room is described. The can_pick_up attribute must be set to True if the item can be picked up. An item will be
    on the floor if the item has been dropped.
    If the item has an ability, set can_activate_ability to True. Then, you need to create the ability_on_description
    and ability_off_description, that will be printed when the ability is turned on or off.
    If the item is a consumable, set can_consume to True. Then set the HP_gain_or_loss to an integer.
    If the item is a weapon, set is_weapon to True, then set the weapon_power to a positive integer
    """

    def __init__(self, name):
        self.name = name
        self.description = None

        self.can_contain = False
        self.contains = []
        self.container_type = None

        # if the item can be picked up
        self.e_description = None
        self.can_pick_up = False
        self.on_floor = False

        # if the item has an ability
        self.can_activate_ability = False
        self.ability = False
        self.ability_on_description = None
        self.ability_off_description = None

        # if the item is a consumable
        self.can_consume = False
        self.HP_gain_or_loss = None

        # if the item is a weapon
        self.is_weapon = False
        self.weapon_power = None

    def remove_item_from_container(self, item):
        """
        Used to remove an item from its item container."""
        if item in self.contains:
            self.contains.remove(item)

    def add_description(self, description):
        """
        Used to add a description
        """
        self.description = description

    def add_env_description(self, description):
        """
        Used to add an environmental description
        """
        self.e_description = description

    def toggle_can_pick_up(self):
        """Toggles whether or not you can pick up an item"""
        if not self.can_pick_up:
            self.can_pick_up = True
        else:
            if self.can_pick_up:
                self.can_pick_up = False

    def toggle_on_floor(self):
        """Toggles whether an item is on the floor"""
        if not self.on_floor:
            self.on_floor = True
        else:
            if self.on_floor:
                self.on_floor = False

    def toggle_can_activate_ability(self):
        """
        Make it so an item has an ability
        """
        if not self.can_activate_ability:
            self.can_activate_ability = True
        else:
            if self.can_activate_ability:
                self.can_activate_ability = False

    def toggle_ability(self):
        """
        Toggles the ability
        """
        if not self.ability:
            self.ability = True
        else:
            if self.ability:
                self.ability = False

    def add_ability_on_description(self, description):
        """add description that is printed when an ability is turned on"""
        self.ability_on_description = description

    def add_ability_off_description(self, description):
        """add description that is printed when an ability is turned on"""
        self.ability_off_description = description

    def toggle_can_consume(self):
        """
        Toggle whether an item is a consumable
        """
        if not self.can_consume:
            self.can_consume = True
        else:
            if self.can_consume:
                self.can_consume = False

    def set_consumable_effect(self, integer):
        """
        Set the positive or negative effect of the consumable on player HP
        """
        self.HP_gain_or_loss = integer

    def toggle_is_weapon(self):
        """
        Toggle whether an item is a weapon
        """
        if not self.is_weapon:
            self.is_weapon = True
        else:
            if self.is_weapon:
                self.is_weapon = False

    def set_weapon_power(self, integer):
        """
        Sets the power of the weapon. Must be a positive integer
        """
        if integer < 0:
            print("power must be a positive integer")
            return
        self.weapon_power = integer


class Enemy:
    """
    Initialize an instance of an Enemy object. Each enemy has a description, and e_description, HP, and power. When
    the HP is depleted to 0 or less from player attacks, the enemy dies. The power is the damage that the enemy will
    do to the player
    """

    def __init__(self, name):
        self.name = name
        self.description = None
        self.e_description = None
        self.is_dead = False
        self.HP = None

        # if the enemy has an ability
        self.can_activate_ability = False
        self.ability = False
        self.ability_on_description = None
        self.ability_off_description = None

        # moves
        # move 1
        self.move_1 = None
        self.move_1_power = None

        # move 2
        self.move_2 = None
        self.move_2_power = None

        # move 3
        self.move_3 = None
        self.move_3_power = None

        # move 4
        self.move_4 = None
        self.move_4_power = None

    def add_description(self, description):
        """
        Used to add a description
        """
        self.description = description

    def add_env_description(self, description):
        """
        Used to add an environmental description
        """
        self.e_description = description

    def toggle_can_activate_ability(self):
        """
        Make it so an enemy has an ability
        """
        if not self.can_activate_ability:
            self.can_activate_ability = True
        else:
            if self.can_activate_ability:
                self.can_activate_ability = False

    def toggle_ability(self):
        """
        Toggles the ability
        """
        if not self.ability:
            self.ability = True
        else:
            if self.ability:
                self.ability = False

    def add_ability_on_description(self, description):
        """add description that is printed when an ability is turned on"""
        self.ability_on_description = description

    def add_ability_off_description(self, description):
        """add description that is printed when an ability is turned on"""
        self.ability_off_description = description

    def set_HP(self, int):
        """
        Used to add a description
        """
        self.HP = int

    def set_moves_and_power(self, move_num, description, power):
        """
        Used to set move descriptions and powers
        """
        if move_num == 1:
            self.move_1 = description
            self.move_1_power = power
        if move_num == 2:
            self.move_2 = description
            self.move_2_power = power
        if move_num == 3:
            self.move_3 = description
            self.move_3_power = power
        if move_num == 4:
            self.move_4 = description
            self.move_4_power = power
