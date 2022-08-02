def build_the_board():
    # -------------------------------------------------------------------------------------------------
    # --------------------CODE FOR MERES CLUSTER STARTING HERE-----------------------------------------
    #create the first room
    Mere_Room_1 = Room("mere cluster room 1")

    #create the long description
    description = "This is the room to the west of the Main Chamber. It smells dusty and damp.\nThere are large pillars lining the walls.\nIt feels like the entrance to an ancient temple.\nThere is a " + (Fore.WHITE + "black patch") + '\033[39m' + " on the floor in the corner." \
                  "\nThere is a row of " + (Fore.WHITE + "candles") + '\033[39m' + " along the southern wall.\nThere is a blue door on the northern wall (" + (
                              Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a small wooden door on the western wall (" + (
                              Fore.YELLOW + "western door") + '\033[39m' + ").\nThere is a door on the eastern wall leading back to the Main Chamber (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_1.add_long_description(description)

    #create the shortened description for the room
    description = "This is the room to the west of the Main Chamber. \nThere is a " + (Fore.WHITE + "black patch") + '\033[39m' + " on the floor in the corner.\nThere is a row of " + (Fore.WHITE + "candles") + '\033[39m' + " along " \
                              "the southern wall. \nThere is a blue door on the northern wall (" + (Fore.YELLOW + "northern door") + '\033[39m' + ").\n" \
                              "There is a small wooden door on the western wall (" + (Fore.YELLOW + "western door") + '\033[39m' + ").\nThere is a door on the eastern wall leading back to the Main Chamber (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_1.add_shorter_description(description)

    #add the candles to the room
    candles = Item("candles")
    #give them a description
    candles.add_description(
        "There is a shallow alcove with 4 candles arranged in a line. \nEach candle is a different color: red, blue, green, and orange.\nThere is a long match nearby."
    )
    #the candles can be activated to trigger a puzzle
    candles.toggle_can_activate_ability()
    candles.add_ability_on_description("You stare at the row of candles, studying them thoughtfully. Something prompts you to pick up the matchstick.")
    candles.add_ability_off_description("You decide to put the matchstick back. You aren't sure if you should light the candles.")

    #add the firepit to the room
    firepit = Item("black patch")
    #give it a description
    firepit.add_description(
        "The floor is scorched, and has small particles of soot all around. It smells faintly smoky.\nYou think there was probably a fire here."
    )


    #add the items to the room
    Mere_Room_1.add_item_to_room(candles)
    Mere_Room_1.add_item_to_room(firepit)

    #connect the main chamber with Mere_Room_1
    # use the add_adjacent_room function to add Mere_Room_1 as the room on the west wall of the Main Chamber
    Main_Chamber.add_adjacent_room("west", Mere_Room_1)
    # since Mere_Room_1 is on the west wall of the main chamber, that means the Main Chamber is east of Mere_Room_1
    Mere_Room_1.add_adjacent_room("east", Main_Chamber)

    #this is the code for mere's room 2
    #create the room
    Mere_Room_2 = Room("mere cluster room 2")

    #create the long description
    description = "This room is littered with small sticks and feathers.\nThere is a dark doorway on the northern wall (" + (
                              Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a blue door on the southern wall (" + (
                              Fore.YELLOW + "southern door") + '\033[39m' + ")."
    Mere_Room_2.add_long_description(description)

    #create the shortened description for the room
    description = "This room is littered with sticks and feathers. \nThere is a dark doorway on the northern wall (" + (
                              Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a blue door on the southern wall (" + (
                              Fore.YELLOW + "southern door") + '\033[39m' + ")."
    Mere_Room_2.add_shorter_description(description)

    #create the sphinx
    sphinx = Enemy("sphinx")
    #add description
    sphinx.add_description("A fierce sphinx with golden fur.\nShe has black hair and amber eyes.")
    #add environmental description
    sphinx.add_env_description("A fierce " + (Fore.RED + "sphinx") + '\033[39m' + " reclines in the center of the room.\nShe has the body of a lion, the wings of an eagle, and the head of a woman.\nShe rises as you enter the room")
    #set its HP
    sphinx.set_HP(10000)
    #set its moves and their descriptions and damage
    sphinx.set_moves_and_power(1, "The sphinx slashes at you with her claws!", 500)
    sphinx.set_moves_and_power(2, "The sphinx slashes at you with her claws!", 500)
    sphinx.set_moves_and_power(3, "The sphinx slashes at you with her claws!", 500)
    sphinx.set_moves_and_power(4, "The sphinx slashes at you with her claws!", 500)
    #add the enemy into the room
    Mere_Room_2.add_enemy_to_room(sphinx)

    #connect Mere_Room_2 with Mere_Room_1
    # use the add_adjacent_room function to add Mere_Room_2 as the room on the north wall of Mere_Room_1
    Mere_Room_1.add_adjacent_room("north", Mere_Room_2)
    # since Mere_Room_2 is on the north wall of Mere_Room_1, that means Mere_Room_1 is south of Mere_Room_2
    Mere_Room_2.add_adjacent_room("south", Mere_Room_1)

    # this is the code for mere's room 3
    # create the room
    Mere_Room_3 = Room("mere cluster room 3")

    # create the long description
    description = "It is very dark and oppressive.\nYou can't go further without a light."
    Mere_Room_3.add_long_description(description)

    # create the shortened description for the room
    description = "It is very dark and oppressive.\nYou can't go further without a light."
    Mere_Room_3.add_shorter_description(description)

    #create the rocks
    rocks = Item("rocks")
    #add description
    rocks.add_description("A bunch of rocks. They are smooth, grey, and a bit damp.")
    #add environmental description
    rocks.add_env_description("There is a pile of " + (
                Fore.WHITE + "rocks") + '\033[39m' + " in the corner. It looks like it was placed there on purpose.")
    rocks.toggle_can_pick_up()
    #add the rocks into the room
    Mere_Room_3.add_item_to_room(rocks)

    #create the soil
    soil = Item("soil")
    #add description
    soil.add_description("A patch of wet earth. It looks like it was recently disturbed.")
    #add environmental description
    soil.add_env_description("There is a wet patch of " + (
                Fore.WHITE + "soil") + '\033[39m' + " near the wall. It looks like it was recently disturbed.")
    soil.toggle_can_pick_up()
    #add the soil into the room
    Mere_Room_3.add_item_to_room(soil)

    #create the figurine
    figurine = Item("figurine")
    #add description
    figurine.add_description("A small figure of a cat. It is black, with a gold necklace.")
    #add environmental description
    figurine.add_env_description("There is a small " + (
                Fore.WHITE + "figurine") + '\033[39m' + " lying on the floor. It looks like a black cat.")
    figurine.toggle_can_pick_up()
    #add the figurine into the room
    Mere_Room_3.add_item_to_room(figurine)

    #connect Mere_Room_3 with Mere_Room_2
    # use the add_adjacent_room function to add Mere_Room_3 as the room on the north wall of Mere_Room_2
    Mere_Room_2.add_adjacent_room("north", Mere_Room_3)
    # since Mere_Room_3 is on the north wall of Mere_Room_2, that means Mere_Room_2 is south of Mere_Room_3
    Mere_Room_3.add_adjacent_room("south", Mere_Room_2)

    #this is the code for mere's room 4
    #create the room
    Mere_Room_4 = Room("mere cluster room 4")

    #create the long description
    description = "This room is very long and skinny. It looks twice as long as the other rooms.\nYou smell fresh air and hear a breeze far above you.\nYou can barely make out the shapes of bats fluttering far overhead.\nThere must be an opening to the outside somewhere.\n" \
                  "There is a large " + (
                Fore.WHITE + "chasm") + '\033[39m' + " in the middle of the room stretching from wall to wall.\nThere is a wooden bar above the chasm, but it's too high to reach.\nThere is a small wooden door on the eastern wall (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_4.add_long_description(description)

    #create the shortened description for the room
    description = "You hear the wind somewhere high overhead.\nThere is a large " + (
                Fore.WHITE + "chasm") + '\033[39m' + " in the middle of the room.\nThere is a small wooden door on the eastern wall (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_4.add_shorter_description(description)

    #create the whip
    whip = Item("whip")
    #add description
    whip.add_description("A long leather whip. It looks strong and flexible.\nYou could use it to attack, or to grab something far away.\nPower: 15")
    #add environmental description
    whip.add_env_description("There is a coiled " + (
                Fore.MAGENTA + "whip") + '\033[39m' + " on the floor. Perhaps it was left behind by some other explorer.")
    whip.toggle_can_pick_up()
    # we need to set it as a weapon
    whip.toggle_is_weapon()
    # we need to set the power of the whip
    whip.set_weapon_power(15)
    #add the whip into the room
    Mere_Room_4.add_item_to_room(whip)

    #create the chasm
    chasm = Item("chasm")
    #add description
    chasm.add_description("A dark chasm. You can't see the bottom.\nIt's too large to jump across.")
    #add the chasm to the room
    Mere_Room_4.add_item_to_room(chasm)

    #connect Mere_Room_4 with Mere_Room_1
    # use the add_adjacent_room function to add Mere_Room_4 as the room on the west wall of Mere_Room_1
    Mere_Room_1.add_adjacent_room("west", Mere_Room_4)
    # since Mere_Room_4 is on the west wall of Mere_Room_1, that means Mere_Room_1 is east of Mere_Room_4
    Mere_Room_4.add_adjacent_room("east", Mere_Room_1)


    # STEP 9: ADD THE PLAYER TO THE STARTING LOCATION

    player = Player()

    player.current_location = Main_Chamber

    return player
