import pickle


class Room:
    def __init__(self, name):
        """
        Initialize an instance of a Room. Each room has a name and description. It also has a list of items that are
        currently found in the room. This list (self.in_room) can have item objects added and removed from it. An item
        will be added to the list if the player drops an item from their inventory in a room. An item will be removed
        when the player picks up an item and puts it into their inventory. Every room has 4 walls (north, south, east,
        west), and each wall can contain the entry to an adjacent room, if needed. The status of whether the room has
        been visited or not will also be kept track of, so that we know when to use the shorter description of the room.
        """
        self.name = name
        self.long_description = None
        self.shortened_description = None
        self.in_room = []
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
         Finally, it will list all of the items that are on the floor and set the room as visited"""

        # print the correct description
        if not self.visited:
            print(self.long_description)
        if self.visited:
            print(self.shortened_description)
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
        # attack, consume,
        # DONE:
        # look at, pick up, go to , drop, activate
#----------------------------------------------------------------------------------------------------------------------------
        # checking if input is at least one word
        if len(user_input) < 1:
            print("Please enter an input")
            input("Press Enter to return")
            return
#------------------------------------------SAVE GAME-------------------------------------------------------------------------
        # when user enters 'savegame' the game state is pickled into a file
        if user_input[0] == "savegame":
            self.save_game(player, save_name)
            return
#-----------------------------------------INVENTORY--------------------------------------------------------------------------
        # when the user enters 'inventory' a list of the items in the inventory is displayed
        if user_input[0] == "inventory":
            self.look_at_inventory()
            input("Press Enter to return")
            return
#----------------------------------------LOOK AT--------------------------------------------------------------------------
        # when the user enters 'look at item', first the inventory is checked for that item, and then the room is checked for
        # that item. If it is found, the item's description is printed.
        if user_input[0] == "look" and user_input[1] == "at":
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
            print("Item not found in current room or inventory")
            return
        # checks room for item to pick up
        if user_input[0] == "pick" and user_input[1] == "up":
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
#----------------------------------------------DROP---------------------------------------------------------------------------
        # if the user enters 'drop item', the items is dropped from inventory onto the floor. It is added to the room's
        # item list, and its on_floor status is toggled
        if user_input[0] == "drop":
            for items in self.inventory:
                if items.can_pick_up == True and items.name == user_input[1]:
                    self.drop_item(items)
                    input("Press Enter to return")
                    return


#-------------------------------------------ACTIVATE-------------------------------------------------------------------------
        #if the user enters 'activate item' this will toggle the item's ability attribute to True or False. Whatever the
        # consequences of this action are will be determined by conditions.py file. First, we will check to see if the item
        # is in your inventory. Then we will check to see if the item is in the room.
        if user_input[0] == "activate":
            for items in self.inventory:
                if items.name == user_input[1] and items.can_activate_ability == True:
                    items.toggle_ability()
                    print(items.name + " activated")
                    return
                if items.name == user_input[1] and items.can_activate_ability == False:
                    print(items.name + " cannot be activated")
                    return

#-----------------------------------CONSUME----------------------------------------------------------------------------
        # this will check to see if there are any consumables in your inventory and in the room. If there are, it will have
        # an effect on your HP
        if user_input[0] == "consume":
            for items in self.inventory:
                if items.name == user_input[1] and items.can_consume == True:
                    self.HP = self.HP + items.power
                    self.inventory.remove(items)
                    print("consumed" + items.name)
                    return









#--------------------------------------------GO TO ----------------------------------------------------------------------------

        # If the user enters "go to room" they will enter a new room. This will check to see if that room exists on the
        # specified wall and then check if the name of the room matches the input. If it does, the current location will
        # be changed to the new room
        if user_input[0] == "go" and user_input[1] == "to":
            if self.current_location.north_wall is not None and user_input[
                2] == self.current_location.north_wall.name:
                direction = "north"
                self.move_to_new_room(direction)
            elif self.current_location.south_wall is not None and user_input[
                2] == self.current_location.south_wall.name:
                direction = "south"
                self.move_to_new_room(direction)
            elif self.current_location.east_wall is not None and user_input[
                2] == self.current_location.east_wall.name:
                direction = "east"
                self.move_to_new_room(direction)
            elif self.current_location.west_wall is not None and user_input[
                2] == self.current_location.west_wall.name:
                direction = "west"
                self.move_to_new_room(direction)
            else:
                print("room does not exist")
                input("Press Enter to return")
        print("invalid command")

    def save_game(self, player, save_name):
        new_save_name = save_name + ".pickle"
        with open(new_save_name, 'wb') as f:
            pickle.dump(player, f)
        return

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

        self.can_consume = False
        self.is_enemy = False
        self.power = None
        self.HP = None

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
