from classes_and_functions import *
from build_board import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()

def check_conditions(player):
    solve_sphinx_riddle(player)
    light_candles(player)
    check_for_dark_room(player)
    item_under_soil(player)
    jackal_from_fish(player)
    give_jackal_fish(player)
    return
  
 # ------------------------------MERE's CLUSTER CONDITIONS ------------------------------------------------------
def light_candles(player):
    """
    When the user activates the candles in "mere cluster room 1", it triggers a puzzle
    the player must light the candles in a certain order to make a hidden item appear
    """
    if player.current_location.name == "mere cluster room 1":  # check to see if the player is in the right room
        for item in player.current_location.in_room:
            if item.name == "candles" and item.ability == True:
                #print(player.current_location.long_description)
                #print("")
                print("You see a small plaque below the candles. It reads:")
                print("Light the green candle first.")
                print("The second candle is somewhere to the left of the orange candle.")
                print("The third candle is not directly next to the red candle.")
                print("Light the blue candle last.")
                correct_answer = ["green", "red", "orange", "blue"]
                correct_count = 0
                print("You strike the match and look at the candles.")
                #loop for the number of candles
                for candle in range(0,4):
                    #make sure the answer is only one word
                    choice = input("Which candle do you want to light?")
                    check_choice_len = choice.split()
                    while (len(check_choice_len) > 1 or len(check_choice_len) < 1):
                        #prompt again if the answer is not 1 word
                        print("Your answer should be 1 word!")
                        choice = input("Which candle do you want to light?")
                        check_choice_len = choice.split()

                    #check that the answer matches
                    #if the answer is correct, print the message and continue
                    if choice.lower() == correct_answer[candle]:
                        print("The candle flares to life. The flame dances cheerfully.")
                        #choice = input("Which candle do you want to light next?")
                        correct_count += 1
                    else:
                        print("The candles briefly flicker, then all go out. It appears you didn't light them in the correct order.")
                        item.toggle_ability()
                        return

                #if the user got all correct guesses, the candles should be disabled
                if correct_count == 4:
                    print("The candles flare up, then you hear a small click. A drawer slides open in the wall below the candles.")
                    player.current_location.remove_item_from_room(item)
                    description = "This is the room to the west of the Main Chamber.\nThere is a " + (Fore.WHITE + "black patch") + '\033[39m' + " on the floor in the corner.\nThere is a row of " + (Fore.WHITE + "candles") + '\033[39m' + " along the southern wall.\nThey are burning cheerfully and light up the room.\nThere is a blue door on the northern wall (" + (
                              Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a door on the eastern wall leading back to the Main Chamber (" + (
                              Fore.YELLOW + "eastern door") + '\033[39m' + ")."
                    player.current_location.add_shorter_description(description)

                    # create the ruby that came from the candle puzzle
                    red_orb = Item("red orb")
                    red_orb.add_description(
                        "A red orb left behind when you lit the candles.\nIt looks like a ruby. It's as big as your fist!")
                    # We need to add an environmental description, since it can be picked up
                    red_orb.add_env_description("In the open drawer next to the candles, there is a " + (
                            Fore.WHITE + "red orb") + '\033[39m' + ". It is smooth and glitters in the candlelight.")
                    red_orb.toggle_can_pick_up()
                    # add the orb to the room
                    player.current_location.add_item_to_room(red_orb)

                    # make the 'candles' an examinable feature (but can't activate)
                    candles = Item("candles")
                    candles.add_description(
                        "The flames on the candles are burning steadily. They won't go out anytime soon.\nA small drawer is open in the wall beside the candles.")
                    # add the candles to the room
                    player.current_location.add_item_to_room(candles)

                    input("Press Enter to return")
                    return

def solve_sphinx_riddle(player):
    """
    When the user encounters the sphinx in "mere cluster room 2", they must answer a riddle in order to pass
    """
    #set the 3 riddles
    riddle1 = "A box without hinges, keys, or a lid\nYet inside, a golden treasure is hid."
    riddle2 = "I create my lair with silken string, and dispatch my prey with a biting sting."
    riddle3 = "I can run, but never walk\nI have a mouth, but never talk\nI have a head, but never weep\nI have a bed, but never sleep."
    #save the riddles paired with the correct answer
    riddle_list = [(riddle1, "egg"), (riddle2, "spider"), (riddle3, "river")]

    if player.current_location.name == "mere cluster room 2":       #check to see if the player is in the right room
        for enemies in player.current_location.enemies:             #iterate through enemies to find the sphinx
            if enemies.name == "sphinx" and enemies.is_dead != True: #name must match and must not be dead
                print(enemies.e_description)
                print("The sphinx says 'You must answer my riddle to pass.'")
                answer = input('Do you wish to answer the riddle? (Y/N)')
                #prompt the user to answer a riddle
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    pass
                else:
                    print("You decide not to answer the sphinx's riddle.\nShe hisses and lashes her tail.\nYou think it would be best to leave.")
                    player.move_to_new_room("south")
                    input("Press Enter to return")
                    return
                choice = random.randrange(0,3)
                riddle = riddle_list[choice]
                print(riddle[0])
                print("What is the correct answer?\n(Answer should be one word)")
                answer = input()
                #check the answer
                #if the answer is correct, sphinx should disappear from room
                if answer.lower() == riddle[1]:
                    enemies.is_dead = True
                    sapphire_from_sphinx(player)
                #if the answer is wrong, game is over
                else:
                    print("The sphinx whips her tail angrily and flexes her claws.\n'WRONG!' She yells, and lunges towards you.\nAs she spreads her wings, your vision fades to black.")
                    print("GAME OVER!")
                    input("Press Enter to return")
                    player.is_dead = True

def sapphire_from_sphinx(player):
    """
    Once you correctly solve the riddle from the sphinx that is in "mere cluster room 2", the sphinx will vanish
    a blue sphere is revealed on the floor. You can now pick up the blue sphere
    """
    if player.current_location.name == "mere cluster room 2":  # check to see if the player is in the right room
        for enemies in player.current_location.enemies:  # iterate through enemies to see if the sphinx is 'dead'
            if enemies.name == "sphinx" and enemies.is_dead == True:  # name must match and must be dead
                print('The sphinx squawks, "You are correct" and flaps its wings, raising a large cloud of dust.\nYou cough and cover your eyes.\nWhen you look back up, she has vanished.')
                print('There is a smooth blue sphere resting on the floor where the sphinx was standing.')

                # now remove the sphinx from the room so that this condition does not trigger again next time you
                # enter this room
                player.current_location.enemies.remove(enemies)
                # create the sapphire that came from the sphinx
                blue_orb = Item("blue orb")
                blue_orb.add_description("A blue orb left behind when you solved the sphinx's riddle.\nIt looks like a sapphire. It's as big as your fist!")
                blue_orb.toggle_can_pick_up()
                # We need to add an environmental description, since it can be picked up
                blue_orb.add_env_description("In the place where the sphinx was standing, there is a " + (
                        Fore.WHITE + "blue orb") + '\033[39m' + ". It is smooth and glitters faintly.")
                # add the orb to the room
                player.current_location.add_item_to_room(blue_orb)

                input("Press Enter to return")
                return

def check_for_dark_room(player):
    """
    When the user encounters the "dark room" in "mere cluster room 3", they must have the lantern activated to progress
    """
    if player.current_location.name == "mere cluster room 3":           # check to see if the player is in the right room
        for item in player.inventory:                                   #check all the items in the player inventory
            if item.name == "torch" and item.ability == True:           #if the torch item is found, check if it's turned on
                #if the torch item is found and turned on, then the room description should print
                player.current_location.add_long_description("The torch lights up the darkness and illuminates the room.\nIt seems to have a rocky floor, and water drips down the walls.\nIt smells a bit dank and unpleasant.\n"
                                                             "There is a dark doorway on the southern wall, leading back the way you came (" + (Fore.YELLOW + "southern door") + '\033[39m' + ").")
                player.current_location.add_shorter_description("The torch lights up the darkness and illuminates the room.\nThere is a dark doorway on the southern wall, leading back the way you came (" + (Fore.YELLOW + "southern door") + '\033[39m' + ").")
                return
        #if the torch item is not found or is not turned on, then only an error message about the darkness
        #also need to show the room they previously came from so they can leave again
        player.current_location.add_long_description("It is very dark and oppressive. You can't go further without a light.\nThere is a dark doorway on the southern wall, leading back the way you came (" + (Fore.YELLOW + "southern door") + '\033[39m' + ").")
        player.current_location.add_shorter_description("It is very dark and oppressive. You can't go further without a light.\nThere is a dark doorway on the southern wall, leading back the way you came (" + (Fore.YELLOW + "southern door") + '\033[39m' + ").")
        return

def item_under_soil(player):
    """
    When the user picks up the soil in "mere cluster room 3", they find a buried fish
    """
    if player.current_location.name == "mere cluster room 3":       #check to see if the player is in the right room
        for item in player.inventory:                               #check all the items in the player inventory
            if item.name == "soil":                                 #if the soil has been picked up
                #print some description about the soil falling to the ground
                print("The soil is damp and slips through your fingers. You don't have any way to hold it. You decide not to carry it.")
                print("While digging in the soil, you uncover something. You scrape the soil to the side and find a rotten fish.\nIt looks like it's been buried for awhile. It smells terrible.")
                input("Press Enter to return")
                player.inventory.remove(item)

                #create the rotten fish. it's a consumable (but why!)
                fish = Item("fish")
                #give the fish a description, including affect on HP if consumed
                fish.add_description("It's a smelly, rotten fish. You could eat it, but it wouldn't taste very good.\nHP -10")
                #give the fish an environmental description
                fish.add_env_description("There is a rotten " + (Fore.BLUE + "fish") + '\033[39m' + " lying in a hollow. It was buried under some wet soil.")
                #set it as a consumable
                fish.toggle_can_consume()
                #set the effect of the consumable
                fish.set_consumable_effect(-15)
                #make it so you can pick up the fish
                fish.toggle_can_pick_up()
                #add the fish to the room
                player.current_location.add_item_to_room(fish)

def jackal_from_fish(player):
    """
    If the user picks up the rotten fish in "mere cluster room 3", they must fight a jackal
    """
    if player.current_location.name == "mere cluster room 3":       #check to see if the player is in the right room
        for item in player.inventory:                               #check all the items in the player inventory
            if item.name == "fish":                                 #if the fish has been picked up
                for enemy in player.current_location.enemies:       #check if the jackal is already in the room
                    if enemy.name == "jackal":
                        return

                #create the jackal enemy
                jackal = Enemy("jackal")
                #add description
                jackal.add_description("A fierce jackal, with bared teeth. He looks angry.")
                #add an environmental description
                jackal.add_env_description("A " + (Fore.RED + "jackal") + '\033[39m' + " lurks in the shadows. He is growling. Was the fish his?")
                #set HP
                jackal.set_HP(25)
                #set moves and their power/descriptions
                jackal.set_moves_and_power(1, "The jackal jumps at your leg and bites your foot!", 10)
                jackal.set_moves_and_power(2, "The jackal lunges at you, but missed", 0)
                jackal.set_moves_and_power(3, "The jackal extends his claws and scratches you!", 5)
                jackal.set_moves_and_power(4, "The jackal howls and charges into you!", 5)
                #add the enemy into the room
                player.current_location.add_enemy_to_room(jackal)

def give_jackal_fish(player):
    """
    If the user drops the rotten fish in "mere cluster room 3", the jackal will take it and leave
    """
    if player.current_location.name == "mere cluster room 3":       #check to see if the player is in the right room
        for item in player.current_location.in_room:                #check all the items in the room
            if item.name == "fish":                                 #if the fish has been dropped
                for enemy in player.current_location.enemies:       #check if the jackal is already in the room
                    if enemy.name == "jackal":
                        print("The jackal sniffs the air. He looks at you suspiciously.\nThen he trots over to the fish and picks it up in his mouth.")
                        print("The jackal slinks back into the shadows and disappears.\nAs he runs away, you notice something glint from beneath his feet.")
                        input("Press Enter to return")

                        #remove the fish from the room
                        player.current_location.remove_item_from_room(item)
                        #remove the jackal from the room
                        enemy.is_dead = True

                        #create the coin
                        coin = Item("coin")
                        #add description
                        coin.add_description("A shiny gold coin. It looks old and valuable. It was buried in the jackal's room.")
                        #add an environmental description
                        coin.add_env_description("A gold " + (Fore.WHITE + "coin") + '\033[39m' + " glitters in the dirt. It was uncovered when the jackal left.")
                        #add the item into the room
                        player.current_location.add_item_to_room(coin)
                        coin.toggle_can_pick_up()

def cross_chasm(player):
    """
    When the user encounters the "chasm" in "mere cluster room 4", they must equip the whip to cross
    """
    if player.current_location.name == "mere cluster room 4":           # check to see if the player is in the right room
        if player.equipped == "whip":           #if the whip item is found, check if it's equipped
            #if the whip is equipped, the player can cross the chasm
            print("You carefully heft the whip in your hand, then take aim at the wooden bar above you.\nThe end of the whip coils around the bar, and you pull it tight.\n"
                  "You back up a few steps, then run foreward and swing across the chasm.\nYou land safely on the other side, and pull the whip back down behind you.")
                #brass sphinx should be added to room (on floor?)
                #maybe a door on the far side of chasm - fake treasure room?

            input("Press Enter to return")
            print("When you land on the far side of the chasm, you hear a click and the tile beneath your feet sinks slightly lower.\nYou hear a loud grinding sound, and a bridge slowly extends from the side of the chasm."
                  "\nOnce it reaches the other side, it locks into place. The noise stops, and the room is quiet.")
            input("Press Enter to return")

            # update the shortened description for the room
            description = "You hear the wind somewhere high overhead.\nThere is a large " + (
                    Fore.WHITE + "chasm") + '\033[39m' + " in the middle of the room, with a bridge stretching across.\nThe " + (
                    Fore.WHITE + "tile") + '\033[39m' + " at your feet seems a bit loose.\nThere is a small wooden door on the eastern wall (" + (
                                  Fore.YELLOW + "eastern door") + '\033[39m' + ")."
            player.current_location.add_shorter_description(description)

            # update the chasm description
            chasm = Item("chasm")
            # add description
            chasm.add_description("A dark chasm. You can't see the bottom.\nThere is a thin bridge stretching from one side to the other.\nYou're not sure what it's made of, but it seems strong.")
            # add the chasm to the room
            player.current_location.add_item_to_room(chasm)

            # add the tile description
            tile = Item("tile")
            # add description
            tile.add_description("A ceramic tile, with a navy and gray pattern. It seems slightly different from all the others.\nIt feels a bit loose. You wonder if you could pick it up.")
            # We need to give the tile an environmental description, since it can be picked up
            tile.add_env_description("On the ground at your feet there is a " + (
                    Fore.WHITE + "tile") + '\033[39m' + " that seems to wobble a little when you step on it.")
            # make it so we can pick up the tile
            tile.toggle_can_pick_up()
            # add the tile to the room
            player.current_location.add_item_to_room(tile)
