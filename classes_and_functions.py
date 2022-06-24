import pickle
import colorama
from colorama import Fore, Back, Style
colorama.init()

# to do:
# 1. comment everything
# 2. make functions for everything
# 3. make video explaining game
class Room:
    def __init__(self, name):
        """
        Initialize an instance of a Room. Each room has a name and description. It also has a list of items that are
        currently found in the room . This list (self.in_room) can have item objects added and removed from it. An item
        will be added to the list if the player drops an item from their inventory in a room. An item will be removed
        when the player picks up an item and puts it into their inventory. Every room has 4 walls (north, south, east,
        west), and each wall can contain the entry to an adjacent room, if needed. The status of whether the room has
        been visited or not will also be kept track of, so that we know when to use the shorter description of the room.
        Self.enemies is a list of enemies in the room, which consist of enemy objects
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
        self.visited = False

    def build_description(self):
        """ This function builds the correct description that will be displayed when the player walks into
        a room. First, it will check if the player has visited this room before. It he hasn't, it will display the
        long form description. If he has, it will print the shorter description. It will then iterate through
         every item in the room, and check whether or not that item has been dropped on the floor. If the item has
         not been dropped on the floor (meaning it is in its original place), it will then read the item's description.
         It will list all of the items that are on the floor and set the room as visited. Finally, it will list
         the enemies in the room and their environmental description
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
            for items in floor_items:
                print(items)

        # print the enemies in the room
        for enemies in self.enemies:
            print(enemies.e_description)

        # set the room as visited
        self.visited = True

    def take_input(self):
        """
        After the player reads the description, he will have to take an action. This method receives the input that the
        user will type, and splits it into a list of strings. This list of strings will be returned to main.py, where it
        will be used in a function to execute the command that was typed
        """
        user_input = input()
        user_input = user_input.split()
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
        self.enemies.append(enemy)

    def remove_item_from_room(self, item):
        """
        This removes an item from a room when Player picks up an item.
        """
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


class Player:
    """
    Initialize an instance of a Person object. The person has a name and an inventory. Each object also keeps track of
    the room the player visited, the current location of the player, and the location that the Player last saved in.
    """

    def __init__(self):
        self.name = None
        self.inventory = []
        self.rooms_visited = []
        self.current_location = None
        self.is_dead = False
        self.HP = 100
        self.equipped = None

    def execute_input(self, user_input, player, save_name):
        """ This function parses the input that the use typed in. If the user types in "look at x" the function
        first checks your inventory for x and reads its description. If its not in your inventory, it assumes that
        it is in the room that you are currently in and will read the description. If you type "look at inventory" it
        will list all of the items in your inventory. If you type "pick up", this function will look at all of the items
        in your current room and try to pick up the item you typed in. It will also allow you to travel between rooms
        by using "go to room_name". It does this by checking if your current room has an adjacent room with the name
        you entered.
        """
        # TO DO:
        #
        # DONE:
        # look at, pick up, go to , drop, activate, equip, consume, attack
        # ----------------------------------------------------------------------------------------------------------------------------
        # checking if input is at least one word
        if len(user_input) < 1:
            print("Please enter an input")
            input("Press Enter to return")
            return

        if len(user_input) == 4:
            user_input[2] = str(user_input[2]) + " " + str(user_input[3])

        if len(user_input) == 5:
            user_input[2] = str(user_input[2]) + " " + str(user_input[3]) + " " + str(user_input[4])
        # ------------------------------------------SAVE GAME-------------------------------------------------------------------------
        # when user enters 'savegame' the game state is pickled into a file
        if user_input[0] == "savegame":
            self.save_game(player, save_name)
            return
        # ---------------------------------------- HELP -------------------------------------------------------------------------
        # when user enters 'help' the help screen is printed
        if user_input[0] == "help":
            self.help_screen()
            input("Press Enter to return to game")
            return

        # -----------------------------------------INVENTORY--------------------------------------------------------------------------
        # when the user enters 'inventory' a list of the items in the inventory is displayed
        if user_input[0] == "inventory":
            self.look_at_inventory()
            input("Press Enter to return")
            return

        if len(user_input) < 2:
            print("invalid input")
            input("Press Enter to return")
            return

        # ----------------------------------------LOOK AT--------------------------------------------------------------------------
        # when the user enters 'look at item', first the inventory is checked for that item, and then the room is checked for
        # that item. If it is found, the item's description is printed.
        if user_input[0] == "look" and user_input[1] == "at":
            if len(user_input) < 3:
                print("invalid input")
                input("Press Enter to return")
                return
            for items in self.inventory:
                if items.name == user_input[2]:
                    print(items.description)
                    input("Press Enter to return")
                    return
            for items in self.current_location.in_room:
                if items.name == user_input[2]:
                    print(items.description)
                    input("Press Enter to return")
                    return
            # iterate through your inventory
            if user_input[2] == "inventory":
                self.look_at_inventory()
                input("Press Enter to return")
                return
            for enemies in self.current_location.enemies:
                if enemies.name == user_input[2]:
                    print(enemies.description)
                    print("HP: " + str(enemies.HP))
                    input("Press Enter to return")
                    return
            print("Not found in current room or inventory")
            return
        # --------------------------------------PICK UP ---------------------------------------------------------------------------
        # checks room for item to pick up
        if user_input[0] == "pick" and user_input[1] == "up":
            if len(user_input) < 3:
                print("invalid input")
                input("Press Enter to return")
                return
            for items in self.current_location.in_room:
                if items.can_pick_up == True and items.name == user_input[2]:
                    self.add_to_inventory(items)
                    input("Press Enter to return")
                    return
                if items.name == user_input[2] and items.can_pick_up == False:
                    print("item cannot be picked up")
                    input("Press Enter to return")
                    return
            print("Item not found in room")
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
        if user_input[0] == "activate":
            for items in self.inventory:
                if items.name == user_input[1] and items.can_activate_ability == True:
                    items.toggle_ability()
                    print(items.name + " activated")
                    if items.ability:
                        print(items.ability_on_description)
                    if not items.ability:
                        print(items.ability_off_description)
                    input("Press Enter to return")
                    return
                if items.name == user_input[1] and items.can_activate_ability == False:
                    print(items.name + " cannot be activated")
                    input("Press Enter to return")
                    return
            for items in self.current_location.in_room:
                if items.name == user_input[1] and items.can_activate_ability == True:
                    items.toggle_ability()
                    print(items.name + " activated")
                    if items.ability:
                        print(items.ability_on_description)
                    if not items.ability:
                        print(items.ability_off_description)
                    input("Press Enter to return")
                    return
                if items.name == user_input[1] and items.can_activate_ability == False:
                    print(items.name + " cannot be activated")
                    input("Press Enter to return")
                    return

        # -----------------------------------CONSUME----------------------------------------------------------------------------
        # this will check to see if there are any consumables in your inventory. If there are, it will have
        # an effect on your HP
        if user_input[0] == "consume":
            for items in self.inventory:
                if items.name == user_input[1] and items.can_consume == True:
                    self.HP = self.HP + items.HP_gain_or_loss
                    print("consumed " + items.name)
                    self.inventory.remove(items)
                    return
                if items.name == user_input[1] and items.can_consume == False:
                    print(items.name + " cannot be consumed")
                    return

        # ---------------------------- EQUIP ------------------------------------------------------------------------------
        # this will equip a weapon to the player with a power that will take away from an enemy HP

        if user_input[0] == "equip":
            for items in self.inventory:
                if items.name == user_input[1] and items.is_weapon == True:
                    self.equipped = items
                    print("equipped " + items.name)
                    return
                if items.name == user_input[1] and items.is_weapon == False:
                    print(items.name + " is not a weapon")
                    return

        # -------------------------- ATTACK -----------------------------------------------------------------------------
        # this will use whatever the player has equipped to attack and enemy object. If nothing is equipped the player
        # will fight with his hands, which will do very little damage

        if user_input[0] == "attack":
            for enemies in self.current_location.enemies:
                if enemies.name == user_input[1]:
                    if self.equipped is not None:
                        enemies.HP = enemies.HP - self.equipped.weapon_power
                        print(enemies.name + " took " + str(self.equipped.weapon_power) + "damage!")
                        if enemies.HP == 0 or enemies.HP < 0:
                            print(enemies.name + " was defeated!")
                            self.current_location.enemies.remove(enemies)
                            return
                        return
                    if self.equipped is None:
                        enemies.HP = enemies.HP - 5         # unarmed combat damage
                        print(enemies.name + " took 5 damage!")
                        if enemies.HP == 0 or enemies.HP < 0:
                            print(enemies.name + " was defeated!")
                            self.current_location.enemies.remove(enemies)
                            return
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
            if self.current_location.north_wall is not None and user_input[
                2] == self.current_location.north_wall.name:
                direction = "north"
                self.move_to_new_room(direction)
                return
            elif self.current_location.south_wall is not None and user_input[
                2] == self.current_location.south_wall.name:
                direction = "south"
                self.move_to_new_room(direction)
                return
            elif self.current_location.east_wall is not None and user_input[
                2] == self.current_location.east_wall.name:
                direction = "east"
                self.move_to_new_room(direction)
                return
            elif self.current_location.west_wall is not None and user_input[
                2] == self.current_location.west_wall.name:
                direction = "west"
                self.move_to_new_room(direction)
                return
            else:
                print("room does not exist")
                input("Press Enter to return")
                return
        print("invalid command")

    def save_game(self, player, save_name):
        new_save_name = save_name + ".pickle"
        with open(new_save_name, 'wb') as f:
            pickle.dump(player, f)
        return

    def help_screen(self):
        print("Welcome to Treasure Tomb, a text-based treasure hunting game!")
        print("The objective of this game is to get to the treasure by making your way through a dangerous, haunted tomb.")
        print("If you make the wrong decision or your HP goes to 0, you will die, so be careful!")
        print("\n")
        print("In each room, you will be presented with a description of your surroundings.")
        print("Items and Enemies that may be interacted with are color-coded: ")
        print("regular items are white")
        print("consumable items are blue")
        print("weapon items are magenta")
        print("rooms are yellow")
        print("enemies are red")
        print("\n")
        print("You may interact with certain objects in your environment using player-inputted commands.")
        print("Warning: commands must be inputted exactly as they are listed here")
        print("List of supported commands:") #look at, pick up, go to , drop, activate, equip, consume, attack
        print("look at _____  :  Allows you to see a description of any item or enemy in the room.")
        print("pick up _____  : Allows you to pick up an item, as long as that item can be picked up. It "
              "will be placed in your inventory")
        print("go to _____ : Allows you to go into a new room, which will be highlighted yellow")
        print("drop _____   : Allows you to drop an item from your inventory onto the floor")
        print("activate ______   : Allows you to interact with any item in your current room or in your inventory.")
        print("equip ______    :  Allows you to equip an item, only if it is a weapon. Equipped weapons can be used to attack enemies")
        print("attack ______  :   Must be directed towards an enemy, which is highlighted in red. If a weapon is not equipped, you will attack with your hands")
        print("consume _____ :  Allows you to consume a consumable item, which is highlighted in blue. Consumable items have an effect on your HP  ")


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
                item.toggle_on_floor()
            self.current_location.add_item_to_room(item)
            self.inventory.remove(item)
            print("dropped " + item.name)
        else:
            print("item not in inventory")

    def look_at_inventory(self):
        """
        Prints all of the items in your inventory
        """
        for items in self.inventory:
            print(items.name)

    def look_at_item_in_room(self, item):
        """
        Look at an item in the room and see its description
        """
        if item in self.current_location.in_room:
            print(item.description)
        else:
            print("item not in room")

    def move_to_new_room(self, direction):
        """
        This function is used when the Player enters one of the adjacent rooms. It sets the player's current location
        to the new room, and then it uses the entering_room() function from the Player class to print the description
        of the new room and list what is on the floor. It also adds the new room to the "rooms_visited" list of the
        Player
        """
        if direction == "north":
            self.current_location = self.current_location.north_wall
            self.rooms_visited.append(self.current_location)
        if direction == "south":
            self.current_location = self.current_location.south_wall
            self.rooms_visited.append(self.current_location)
        if direction == "east":
            self.current_location = self.current_location.east_wall
            self.rooms_visited.append(self.current_location)
        if direction == "west":
            self.current_location = self.current_location.west_wall
            self.rooms_visited.append(self.current_location)


class Item:
    """
    Initialize an instance of an Item object. Each item has a name and description. The item may have an ability that
    it can toggle on or off, and may be on the floor if dropped.
    """

    def __init__(self, name):
        self.name = name
        self.description = None
        self.e_description = None
        self.on_floor = False
        self.can_pick_up = False

        self.ability = False
        self.can_activate_ability = False
        self.ability_on_description = None
        self.ability_off_description = None


        self.can_consume = False
        self.HP_gain_or_loss = None

        self.is_weapon = False
        self.weapon_power = None

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

    def toggle_ability(self):
        """
        Toggles the ability
        """
        if not self.ability:
            self.ability = True
        else:
            if self.ability:
                self.ability = False

    def toggle_on_floor(self):
        """ Toggles whether an item is on the floor"""
        if not self.on_floor:
            self.on_floor = True
        else:
            if self.on_floor:
                self.on_floor = False

    def toggle_can_pick_up(self):
        """ Toggles whether or not you can pick up an item"""
        if not self.can_pick_up:
            self.can_pick_up = True


class Enemy:
    """
       Initialize an instance of an Enemy object. Each item has a name and description. The item may have an ability that
       it can toggle on or off, and may be on the floor if dropped.
       """

    def __init__(self, name):
        self.name = name
        self.description = None
        self.e_description = None
        self.HP = None
        self.power = None

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

    def set_HP(self, int):
        """
        Used to add a description
        """
        self.HP = int

    def set_power(self, int):
        """
        Used to add an environmental description
        """
        self.power = int
