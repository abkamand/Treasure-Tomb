from classes_and_functions import *
from build_board import *
import colorama
from colorama import Fore, Back, Style
import random
import time

colorama.init()


# This is the conditions file that will be run during every gameplay loop in order to change the board
# if anything happens. The function check_conditions is the main function in this file. Since there will
# undoubtedly be many,many conditions that can happen in this game, we will be putting each condition in
# its own function, which will then be run within check_conditions (similar to the main function of a C program).

# If you look at check_conditions, you will see an example of a function diamond_from_dead_mummy that is an example of
# this structure.

# This is just one example, but using similar strategies that are tons of different things you can do by manipulating
# different objects. For example, you can make a room dark to begin with, and then check to see if the player has
# activated a torch. If he/she has, you can change the description of the room to have more information.


def check_conditions(player):
    # Ashwin Room Conditions
    water_room_mummy(player)
    water_room_create_water(player)
    water_room_statue(player)
    green_room_mummy(player)
    green_room_patch(player)
    green_room_cut_tree(player)
    green_room_replenish_ingredients(player)
    blacksmith_room_mummy_helmet(player)
    blacksmith_room_chandelier(player)
    blacksmith_room_fire_arrows(player)
    blacksmith_room_make_stew(player)
    blacksmith_room_stew_success(player)

    # Andrew's Rooms conditions
    darkness_puzzle(player)
    explode_boulder(player)
    jump_puzzle(player)
    animal_puzzle(player)
    light_dynamite(player)
    dead_to_dynamite(player)
    blow_out_torch(player)

    # Mere conditions
    solve_sphinx_riddle(player)
    light_candles(player)
    check_for_dark_room(player)
    item_under_soil(player)
    jackal_from_fish(player)
    give_jackal_fish(player)
    cross_chasm(player)
    item_under_tile(player)
    return


# ------------------------------ASH's CLUSTER CONDITIONS ------------------------------------------------------

def water_room_mummy(player):
    """
    When you enter the water room, you will immediately be attacked by the mummy with the axe. When he dies, he will
    drop the axe.
    """
    if player.current_location.name == "Water Room" and player.current_location.visited == True:
        for enemies in player.current_location.enemies:  # iterate through enemies to see if the mummy is dead
            if enemies.name == "mummy" and enemies.is_dead == False:
                player.in_combat = enemies
            if enemies.name == "mummy" and enemies.is_dead == True:
                print('The defeated mummy vanishes into dust.')
                print("Press Enter to return")
                input()
                player.current_location.enemies.remove(enemies)
                return


def water_room_create_water(player):
    """
    If you have the chalice in your inventory and you activate the sink, the chalice will be filled with water
    Then, if you activate the statue with the chalice that now has water in it, you will pour water into the mouth of
    the statue.
    If this happens, the room will fill with water and you can swim to the southern door.

    """

    if player.current_location.name == "Water Room":
        for items in player.current_location.in_room:
            if items.name == "sink" and items.ability == True:
                for i in player.current_location.in_room:
                    if i.name == "water":
                        return
                water = Item("water")
                water.add_description("Water has collected at the bottom of the sink")
                water.add_env_description(
                    "At the bottom of the sink, a pool of " + (Fore.WHITE + "water") + '\033[39m' + " has accumulated.")
                water.toggle_can_pick_up()
                player.current_location.add_item_to_room(water)


def water_room_statue(player):
    if player.current_location.name != "Water Room":
        return
    for items in player.current_location.in_room:
        if items.name == "statue":
            for i in items.contains:
                if i.name == "water":
                    items.contains = []
                    print("You pour the water from the chalice into the mouth of the statue of Khnum.")
                    print(
                        "Suddenly, you hear a rush of water coming from beneath you! The sink begins to overflow with water! ")
                    print("Water begins pouring through the cracks of the limestone walls, flooding the room!")
                    print("The flooding causes the water level of the room to rise, taking you with it.")
                    print("Finally, the flooding stops. You are now able to reach the door on the southern wall (" + (
                            Fore.YELLOW + "southern door") + '\033[39m' + ").")
                    input("Press Enter to return")
                    player.current_location.long_description = "The room has been flooded. All that remains is a pool of glistening " + (
                            Fore.WHITE + "water") + '\033[39m' + ". You can now swim to the door on the southern wall (" + (
                                                                       Fore.YELLOW + "southern door") + '\033[39m' + ")."
                    player.current_location.shortened_description = "The room has been flooded. All that remains is a pool of glistening " + (
                            Fore.WHITE + "water") + '\033[39m' + ". You can now swim to the door on the southern wall (" + (
                                                                            Fore.YELLOW + "southern door") + '\033[39m' + ")."
                    player.current_location.in_room = []
                    water = Item("water")
                    water.add_description("A pool of water in the flooded room.")
                    water.add_env_description("")
                    water.toggle_can_pick_up()
                    player.current_location.add_item_to_room(water)


def green_room_mummy(player):
    """
    When you enter the green room, you will immediately be attacked by the mummy with the axe. When he dies, he will
    drop the axe.
    """
    if player.current_location.name == "Green Room" and player.current_location.visited == True:
        for enemies in player.current_location.enemies:  # iterate through enemies to see if the mummy is dead
            if enemies.name == "mummy" and enemies.is_dead == False:
                player.in_combat = enemies
            if enemies.name == "mummy" and enemies.is_dead == True:
                print('The defeated mummy vanishes into dust. As he disintegrates, he drops his axe on the ground.')
                print("Press Enter to return")
                input()
                player.current_location.enemies.remove(enemies)
                axe = Item("axe")
                axe.add_description(
                    "A powerful axe that fell from a vanquished mummy. Might come in handy.\nPower: 35")
                axe.toggle_can_pick_up()
                axe.toggle_on_floor()
                axe.toggle_is_weapon()
                axe.set_weapon_power(35)
                player.current_location.add_item_to_room(axe)
                return


def green_room_replenish_ingredients(player):
    o_count = 0
    t_count = 0
    if player.current_location.name != "Green Room":
        return
    for items in player.current_location.in_room:
        if items.name == "onion":
            o_count = o_count + 1
        if items.name == "tomatoes":
            t_count = t_count + 1
    if o_count == 0:
        onion = Item("onion")
        onion.add_description(
            "An onion. I usually wouldn't eat this plain, but desperate times call for desperate measures.")
        onion.add_env_description(
            "Around the tree, there are " + (Fore.BLUE + "onion") + '\033[39m' + " roots scattered on the ground.")
        onion.toggle_can_pick_up()
        onion.toggle_can_consume()
        onion.set_consumable_effect(5)
        player.current_location.add_item_to_room(onion)
    if t_count == 0:
        tomato = Item("tomatoes")
        tomato.add_description("A juicy tomato")
        tomato.add_env_description((Fore.BLUE + "Tomatoes") + '\033[39m' + " hang from vines on the ceiling.")
        tomato.toggle_can_pick_up()
        tomato.toggle_can_consume()
        tomato.set_consumable_effect(5)
        player.current_location.add_item_to_room(tomato)


def green_room_cut_tree(player):
    """
    check if an axe is eqiupped. check if tree ability is activated. if it is, print that it was cut down. Change the
    descriptions. Connect the rooms. remove tree
    """
    if player.current_location.name != "Green Room":
        return
    for items in player.current_location.in_room:
        if items.name == "tree":
            if items.ability and player.equipped.name != "axe":
                items.ability = False
    if player.equipped.name != "axe":
        return
    for items in player.current_location.in_room:
        if items.name == "tree":
            if items.ability:
                print("You swing your axe at the tree, chopping it down bit by bit.")
                print("The tree finally falls, revealing its hollow interior.")
                print("You peer inside, and can see the entrance to an underground passage.")
                input("Press Enter to return")
                for i in player.current_location.in_room:
                    if i.name == "packet":
                        player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere are " + (
                                    Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                                    Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (
                                                                                    Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up. Where the tree stood, there is now a " + (
                                                                                    Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                        player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere are " + (
                                    Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                               Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (
                                                                               Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up. Where the tree stood, there is now a " + (
                                                                               Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                        for p in player.current_location.in_room:
                            if p.name == "tree":
                                player.current_location.remove_item_from_room(p)
                                return
                player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nOn the ground, there is a " + (
                            Fore.WHITE + "patch") + '\033[39m' + " of grass covered in dirt. Looks like something is buried there.\nThere are " + (
                                                                       Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                       Fore.YELLOW + "northern door") + '\033[39m' + "). Where the tree stood, there is now a " + (
                                                                       Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere is a " + (
                            Fore.WHITE + "patch") + '\033[39m' + " of grass covered in dirt that looks like you can dig it up.\nThere are " + (
                                                                            Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                            Fore.YELLOW + "northern door") + '\033[39m' + "). Where the tree stood, there is now a " + (
                                                                            Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                for i in player.current_location.in_room:
                    if i.name == "tree":
                        player.current_location.remove_item_from_room(i)
                        return


def green_room_patch(player):
    """
    check if the shovel is in the players inventory. Then check if the patch's ability was activated. If both true,
    then create the dead traveler and his spice mix and recipe. Then we need to remove the patch from the room so it
    never happens again.
    """
    if player.current_location.name != "Green Room":
        return
    for items in player.current_location.in_room:
        if items.name == "patch":
            if items.ability and player.equipped.name != "shovel":
                items.ability = False
    has_shovel = False
    patch_on = False
    if player.current_location.name != "Green Room":
        return
    if player.equipped.name == "shovel":
        has_shovel = True
    if not has_shovel:
        return
    for items in player.current_location.in_room:
        if items.name == "patch":
            if items.ability:
                patch_on = True
    if not patch_on:
        return
    print(
        "You dig up the suspicious patch of dirt, only to find the rotting remains of an body. Looks like the guy was looking for the fabled treasure, just like you.")
    input("Press Enter to return")
    adventurer = Item("adventurer")
    adventurer.add_description("The rotting corpse of an unlucky traveler.")
    packet = Item("packet")
    packet.add_description(
        "It looks like a letter is attached to the packet. It's from the adventurer's grandma. It reads:\nMy dearest Jacob,\nI hope you are doing well. I know you are going on a very dangerous exploration, and I'm worried for you.\nWhile you are gone, I want you to be able to remember the taste of home.\nSo, in this packet I'm sending you the spices that go into my famous stew that you always love.\nRemember, all you need to do is add some tomatoes and onions into a bowl with water.\nThen, just add the spices in and put the bowl in the oven for 5 minutes.\nI hope you make it back safely, please come back soon!\nLove,\nGrandma")
    packet.add_env_description("There is a small " + (
            Fore.WHITE + "packet") + '\033[39m' + " sticking out of the pocket of the dead adventurer's vest")
    packet.toggle_can_pick_up()
    player.current_location.add_item_to_room(adventurer)
    player.current_location.add_item_to_room(packet)
    for items in player.current_location.in_room:
        if items.name == "patch":
            player.current_location.remove_item_from_room(items)
    for items in player.current_location.in_room:
        if items.name == "tree":
            player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere is a large oak " + (
                        Fore.WHITE + "tree") + '\033[39m' + " in the center of the room.\nThere are " + (
                                                                        Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                        Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (
                                                                        Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up."
            player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere is a large oak " + (
                        Fore.WHITE + "tree") + '\033[39m' + " in the center of the room.\nThere are " + (
                                                                   Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                   Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (
                                                                   Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up."
            return
    player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere are " + (
                Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                                Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (
                                                                Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up.\nWhere the tree stood, there is now a " + (
                                                                Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
    player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere are " + (
                Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                                                           Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (
                                                           Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up.\nWhere the tree stood, there is now a " + (
                                                           Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."

    return


def blacksmith_room_mummy_helmet(player):
    if player.current_location.name != "Blacksmith Room":
        return
    for enemies in player.current_location.enemies:
        if enemies.name == "mummy" and enemies.is_dead == True:
            print("As the slain mummy disintegrates, his helmet falls from his rotting corpse onto the floor.")
            input("Press Enter to return")
            player.current_location.enemies.remove(enemies)
            dome_helmet = Item("dome helmet")
            dome_helmet.description = "A helmet in the shape of a dome."
            dome_helmet.on_floor = True
            dome_helmet.can_contain = True
            dome_helmet.container_type = "holding:"
            dome_helmet.can_pick_up = True
            player.current_location.add_item_to_room(dome_helmet)
            player.current_location.long_description = 'You enter a sweltering chamber with a stone ' + (
                    Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room. Behind you is the underground ' + (
                                                                   Fore.YELLOW + "passageway") + '\033[39m' + '.  A beautiful ' + (
                                                               Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (
                                                               Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nThese weapons are hanging on the wall beside you: '


def blacksmith_room_fire_arrows(player):
    if player.current_location.name != "Blacksmith Room":
        return
    for items in player.current_location.in_room:
        if items.name == "furnace":
            for i in items.contains:
                if i.name == "bow and arrows":
                    print("You light an arrow on fire.")
                    print("You have equipped the bow with fire arrows")
                    input("Press Enter to return")
                    fire_bow = Item("fire bow")
                    fire_bow.add_description("A bow with arrows that are on fire. Power: 30")
                    fire_bow.is_weapon = True
                    fire_bow.set_weapon_power(30)
                    fire_bow.can_pick_up = True
                    player.inventory.append(fire_bow)
                    player.equipped = fire_bow
                    items.contains = []


def blacksmith_room_chandelier(player):
    if player.current_location.name != "Blacksmith Room":
        return
    for items in player.current_location.in_room:
        if items.name == "chandelier":
            if items.ability == True and player.equipped.name != "fire bow":
                items.ability = False
    if player.equipped.name != "fire bow":
        return
    for items in player.current_location.in_room:
        if items.name == "chandelier":
            if items.ability == True:
                print("You shoot your fiery arrows into the chandelier, lighting the candle at the center.")
                print("Suddenly, the room begins shaking! From the blazing furnace, a creature emerges!")
                print("The creature has the head of an eagle, but the body of a man. He towers over you menacingly.")
                print(
                    '"You should be proud of yourself, human. You have survived where none of your kind ever could," the creature says.')
                print(
                    '"However, your journey ends here. I am a guardian of this tomb, and a representative of the great goddess Nekhbet."')
                print(
                    '"While your courage has been admirable, I must perform my duty and slay you where you stand. Unless..."')
                print("The guardian pauses for a moment.")
                print('"By any chance do you know how to cook?" he asks curiously.')
                print(
                    '"I have been performing my duties defending this tomb for hundreds of years. Other than the occasional adventurer, I have not had real food in a long time."')
                print(
                    '"If you can get me some good food, I will gladly allow you to live. I will also give you the key that you seek to find the treasure."')
                print('"Return to me when you have what I want."')
                input("Press Enter to return")
                Guardian = Enemy("Guardian")
                Guardian.description = "This guardian has been tasked with defending this tomb for hundreds of years.\nHe is a representative of Nekhbet, a patron god of Upper Egypt.\nHe looks pretty powerful. I shouldn't mess with him."
                Guardian.e_description = "The " + (
                        Fore.RED + "Guardian") + '\033[39m' + " patiently waits for you to retrive what he has requested."
                Guardian.can_activate_ability = True
                Guardian.set_HP(2000000000)
                # set its moves and the moves'
                Guardian.set_moves_and_power(1,
                                             "The Guardian rips your head off with his talons!",
                                             100000)
                Guardian.set_moves_and_power(2, "The Guardian rips your head off with his talons!", 1000000)
                Guardian.set_moves_and_power(3, "The Guardian rips your head off with his talons!", 1000000)
                Guardian.set_moves_and_power(4, "The Guardian rips your head off with his talons!", 10000000)
                player.current_location.add_enemy_to_room(Guardian)
                items.ability = False


def blacksmith_room_make_stew(player):
    tom = False
    on = False
    wat = False
    pack = False
    if player.current_location.name != "Blacksmith Room":
        return
    for items in player.current_location.in_room:
        if items.name == "furnace":
            for i in items.contains:
                if i.name == "dome helmet":
                    for p in i.contains:
                        if p.name == "tomatoes":
                            tom = True
                        if p.name == "onion":
                            on = True
                        if p.name == "water":
                            wat = True
                        if p.name == "packet":
                            pack = True
    if tom == True and on == True and wat == True and pack == True:
        grannys_stew = Item("Granny's stew")
        grannys_stew.description = "A delicious stew made with a special spice packet. Served in a helmet"
        grannys_stew.can_pick_up = True
        print("You cook the stew in the furnace for 5 minutes, just like that dead guy's granny said to do.")
        print("Granny's stew has been added to your inventory.")
        input("Press Enter to return")
        player.inventory.append(grannys_stew)
        for items in player.current_location.in_room:
            if items.name == "furnace":
                items.contains = []


def blacksmith_room_stew_success(player):
    has_stew = False
    if player.current_location.name != "Blacksmith Room":
        return
    for items in player.inventory:
        if items.name == "Granny's stew":
            has_stew = True
    for enemies in player.current_location.enemies:
        if enemies.name == "Guardian" and enemies.ability == True and has_stew == False:
            print('"You do not have any delicious food for me," the Guardian says. "Please go away."')
            input("Press Enter to return")
            enemies.ability = False
        if enemies.name == "Guardian" and enemies.ability == True and has_stew == True:
            print('"What is that delicious smell coming from you, my dear human friend?" asks the Guardian.')
            print('"You have finally brought me what I asked of you. I am eternally grateful."')
            print('"Here, take this key and leave me alone. I want to savor this beautiful creation."')
            print("\n")
            print("The Eagle Key has been added to your inventory!")
            print("The Guardian vanishes, presumably to enjoy his meal in peace.")
            print(
                "On the ground where the Guardian was standing, the ground collapses, revealing what looks like a " + (
                            Fore.YELLOW + "slide") + '\033[39m' + ". I wonder where it leads to.")
            input("Press Enter to return")
            for items in player.inventory:
                if items.name == "Granny's stew":
                    player.inventory.remove(items)
            eagle_key = Item("Eagle Key")
            eagle_key.description = "An intricately-carved, bronze key in the shape of an eagle."
            eagle_key.can_pick_up = True
            eagle_key.can_activate_ability = True
            player.inventory.append(eagle_key)
            for e in player.current_location.enemies:
                if e.name == "Guardian":
                    player.current_location.enemies.remove(e)
            player.current_location.long_description = 'You enter a sweltering chamber with a stone ' + (
                        Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room. Behind you is the underground ' + (
                                                                   Fore.YELLOW + "passageway") + '\033[39m' + '. In the center of the room, there is a ' + (
                                                                   Fore.YELLOW + "slide") + '\033[39m' + ' leading somewhere. A beautiful ' + (
                                                                   Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (
                                                                   Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nThese weapons are hanging on the wall beside you: '
            player.current_location.shortened_description = 'A sweltering room with a stone ' + (
                        Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room.\nBehind you is the underground ' + (
                                                                        Fore.YELLOW + "passageway") + '\033[39m' + '. In the center of the room, there is a ' + (
                                                                        Fore.YELLOW + "slide") + '\033[39m' + ' leading somewhere. A beautiful ' + (
                                                                        Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (
                                                                        Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nThese weapons are hanging on the walls: '


# ------------------------------------------ANDREW CONDITIONS ------------------------------------------------------


def dead_to_dynamite(player):
    """If a player lights dynamite in a location outside of Andrew room 1, they will have nowhere to place/throw it and it will blow up in
    their face, killing them."""
    # check if player is in Andrew room 1
    if player.current_location.name != "Andrew 1":
        # check if dynamite is lit
        for i in player.inventory:
            if i.name == "dynamite" and i.ability == True:
                print(i.ability)
                print(
                    "You lit the dynamite in a room with nothing to place it in or on to effectively shield the blast. Any last words...?"
                )
                # kill the player
                player.HP = 0


def blow_out_torch(player):
    """If a player activates their torch in Andrew room 2 or has it active while entering said room, a mystical
    gust of wind will de-activate it to ensure the integrity of the darkness puzzle :)"""
    # check if player is in Andrew room 2
    if player.current_location.name == "Andrew 2":
        # check if torch is active
        for i in player.inventory:
            if i.name == "torch" and i.ability == True:
                print(
                    "A mystical gust of wind blows out your torch... creepy. You'll just have to feel your way through the darkness."
                )
                # de-activate torch
                i.ability = False


def animal_puzzle(player):
    """In Andrew Room 4, player must pick up the python, alligator, and eagle figurine, and place them on the correct pedestal, solving
    an ouroboros predator trifecta of sorts. The correct pairings: Python Pedestal: Eagle Figurine | Eagle Pedestal: Alligator Figurine |
    Alligator Pedestal: Python Figurine. Upon completion, player is rewarded with a diamond key item."""
    # used to track puzzle status since player can independently solve each pedestal
    python_puzzle = False
    eagle_puzzle = False
    alligator_puzzle = False

    # check if player is in Andrew room 4
    if player.current_location.name == "Andrew 4":
        for items in player.current_location.in_room:
            # check which puzzles have been solved already by scanning for hidden items added to room that indicate puzzle status
            if items.name == "python_solved":
                python_puzzle = True
            if items.name == "eagle_solved":
                eagle_puzzle = True
            if items.name == "alligator_solved":
                alligator_puzzle = True

    if player.current_location.name == "Andrew 4":
        for items in player.current_location.in_room:
            # check if python pedestal is solved or if the player has placed a figurine upon it
            if items.name == "snake pedestal" and python_puzzle == False:
                for i in items.contains:
                    # if the player places the wrong figurine, print message, add figurine back to room, subtract hp from player
                    if i.name == "python figurine" or i.name == "alligator figurine":
                        print(
                            "The room shakes and a sharp dart seems to strike you out of nowhere. Ouch!\nSome supernatural force clearly did not like your choice of pedestal... Perhaps you should pick up the figurine from the pedestal and try another?"
                        )
                        print("You lost 5 HP points.")
                        player.HP -= 5
                        player.current_location.add_item_to_room(i)
                        items.remove_item_from_container(i)
                    # if the player places the correct figurine, print message, add hidden item to room to indicate completion and toggle off pick-up
                    # on eagle figurine to prevent player from picking it up again
                    elif i.name == "eagle figurine":
                        print(
                            "The eagle's eyes light up and it locks in place the second you placed it on the snake pedestal... seems like you did something right."
                        )
                        time.sleep(1)
                        python_solved = Item("python_solved")
                        player.current_location.add_item_to_room(python_solved)
                        python_puzzle = True
                        i.toggle_can_pick_up()

            # check if eagle pedestal is solved or figurine placed
            if items.name == "eagle pedestal" and eagle_puzzle == False:
                for i in items.contains:
                    # if the player places the wrong figurine, print message, add figurine back to room, subtract hp from player
                    if i.name == "python figurine" or i.name == "eagle figurine":
                        print(
                            "The room shakes and a sharp dart seems to strike you out of nowhere. Ouch!\nSome supernatural force clearly did not like your choice of pedestal... Perhaps you should pick up the figurine from the pedestal and try another?"
                        )
                        print("You lost 5 HP points.")
                        player.HP -= 5
                        player.current_location.add_item_to_room(i)
                        items.remove_item_from_container(i)
                    # if the player places the correct figurine, print message, add hidden item to room to indicate completion and toggle off pick-up
                    # on eagle figurine to prevent player from picking it up again
                    elif i.name == "alligator figurine":
                        print(
                            "The alligator's eyes light up and it locks in place the second you placed it on the snake pedestal... seems like you did something right."
                        )
                        time.sleep(1)
                        eagle_solved = Item("eagle_solved")
                        player.current_location.add_item_to_room(eagle_solved)
                        eagle_puzzle = True
                        i.toggle_can_pick_up()

            # check if eagle pedestal is solved or figurine placed
            if items.name == "alligator pedestal" and alligator_puzzle == False:
                for i in items.contains:
                    # if the player places the wrong figurine, print message, add figurine back to room, subtract hp from player
                    if i.name == "alligator figurine" or i.name == "eagle figurine":
                        print(
                            "The room shakes and a sharp dart seems to strike you out of nowhere. Ouch!\nSome supernatural force clearly did not like your choice of pedestal... Perhaps you should pick up the figurine from the pedestal and try another?"
                        )
                        print("You lost 5 HP points.")
                        player.HP -= 5
                        player.current_location.add_item_to_room(i)
                        items.remove_item_from_container(i)
                    # if the player places the correct figurine, print message, add hidden item to room to indicate completion and toggle off pick-up
                    # on eagle figurine to prevent player from picking it up again
                    elif i.name == "python figurine":
                        print(
                            "The python's eyes light and it locks in place up the second you placed it on the snake pedestal... seems like you did something right."
                        )
                        time.sleep(1)
                        alligator_solved = Item("alligator_solved")
                        player.current_location.add_item_to_room(alligator_solved)
                        alligator_puzzle = True
                        i.toggle_can_pick_up()

    # check if all 3 puzzles have been solved, if so, give the player the diamond key and update room description
    if alligator_puzzle == True and python_puzzle == True and eagle_puzzle == True:
        print(
            "A hole in the ceiling appears and a key in the shape of a crocodile falls right into the palm of your hand.\nSeems useful... but where? Better keep it for now"
        )
        time.sleep(1)
        crocodile_key = Item("Crocodile Key")
        crocodile_key.description = "a bronze key in the shape of a crocodile"
        crocodile_key.toggle_can_pick_up()
        player.add_to_inventory(crocodile_key)

        description = (
                "You spot what appears to be an "
                + (Fore.CYAN + "animal carving")
                + "\033[39m on the wall. Perhaps you should inspect this further?"
                + "\nPedestals lie across the room with animal figures that you placed on top of each. Every figurine has glowing eyes, seemingly indicating your accomplishment."
                + "\nTo the south lies a rope leading to the pillar room ("
                + (Fore.YELLOW + "southern hole")
                + "\033[39m)."
        )
        player.current_location.add_shorter_description(description)

def light_dynamite(player):
    for i in player.inventory:
        if i.name == "matches":
            for items in player.inventory:
                if items.name == "dynamite":
                    # add ability to dynamite
                    items.can_activate_ability = True
                    items.ability_on_description = (
                        "You need matches to light the dynamite..."
                    )
                    items.ability_off_description = "The dynamite is unlit... perhaps that's for the best unless I find something that needs blowing up. A giant rock maybe?"
                    items.ability_on_description = ("The dynamite is lit... quick, place it on something!")


def darkness_puzzle(player):
    """When the player enters Andrew room 2, a darkness puzzle minigame fires off. Essentially the player must input 'move right', 'move left',
    'move up', or 'move down' to make their way through a dark labrynth represented by a 2d matrix. Certain indeces are blocked which means
    the player cannot traverse that direction. It simulates a player fumbling through darkness, feeling their way through. Upon completion
    when the player reaches the correct index, the room lights up and the minigame ends."""

    def valid(curr, prev, mov, board):
        """Checks if a player movement is valid or not, to be used down below in the crux of the darkness_puzzle gameplay loop."""
        update_row = curr[0] + mov[0]
        update_col = curr[1] + mov[1]
        prev = curr
        curr = (update_row, update_col)

        curr_row = curr[0]
        curr_col = curr[1]

        # movement is invalid, player hits a wall
        if curr_row < 0 or curr_col < 0 or board[curr_row][curr_col] == 1 or curr_row > 3 or curr_col > 3:
            print("You run into something hard, ouch! Can't move that way.")
            curr = prev
            return curr

        # movement is valid, player makes progress
        elif board[curr_row][curr_col] == 0:
            print(
                "You successfully move a few paces into the darkness. How will you move next?"
            )
            return curr

        # player completes the labrynth
        elif board[curr_row][curr_col] == 2:
            print("You successfully move a few paces into the darkness.")
            return curr

    # check if player is in Andrew room 2
    if player.current_location.name == "Andrew 2":
        for items in player.current_location.in_room:
            # check if player has already completed the darkness puzzle, if so, break out of function
            if items.name == "darkness_solved":
                return

        # create board to represent player position
        # 0 = can move, 1 = wall, 2 = destination
        # start = (0, 0)
        board = [
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 1, 0, 2],
            [1, 1, 1, 1]
        ]

        # create directional movement representations
        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # create tuples representing current player location, previous, destination
        prev_location = (0, 0)
        curr_location = (0, 0)
        destination = (3, 3)

        # print gameplay prompt for the user
        print(
            "You enter a pitch black chamber. Darkness is everywhere. Is it even a chamber? Hallway? Death trap?\nYou hear the doorway slam shut behind you."
        )
        print(
            "Perhaps you can make your way through the black labrynth off touch, feeling alone. You're blinded, not deaf or immaterial."
            + "\nShould I"
            + (Fore.YELLOW + " move")
            + "\033[39m to the "
            + (Fore.YELLOW + "right")
            + "\033[39m, "
            + (Fore.YELLOW + "left")
            + "\033[39m, "
            + (Fore.YELLOW + "up")
            + "\033[39m, or"
            + (Fore.YELLOW + " down")
            + "\033[39m to begin?"
        )

        # core darkness puzzle gameplay loop, loops until they reach destination
        while curr_location != destination:
            response = input()

            # player moves right
            if response == "move right":
                curr_location = valid(curr_location, prev_location, right, board)

            # player moves left
            elif response == "move left":
                curr_location = valid(curr_location, prev_location, left, board)

            # player moves down
            elif response == "move down":
                curr_location = valid(curr_location, prev_location, down, board)

            # player moves up
            elif response == "move up":
                curr_location = valid(curr_location, prev_location, up, board)

            # player input is invalid
            else:
                print("Invalid movement.")

        # labrynth complete
        print(
            "\nYou hear a clicking noise. Suddenly, a bright light blinds you and the room is illuminated and you hear the southern doorway rumble open once more."
        )

        # create dynamite
        dynamite = Item("dynamite")

        # give dynamite a description
        dynamite.add_description(
            "A stick of explosive dynamite. Looks like it's still active, but I'll need matches in my inventory to light it."
        )

        # create environmental description
        dynamite.add_env_description(
            "A stick of explosive "
            + (Fore.GREEN + "dynamite")
            + "\033[39m lies on the floor in front of you. Better be careful not to accidentally light it without a purpose... "
        )

        # allow dynamite to be picked up
        dynamite.toggle_can_pick_up()

        player.current_location.add_item_to_room(dynamite)

        # create darkness puzzle item to act as a pseudo breakout of the function so player doesn't have to replay this minigame
        darkness_solved = Item("darkness_solved")
        player.current_location.add_item_to_room(darkness_solved)

        # update room description post-gameplay completion, room is now illuminated
        description = (
                "You are in the previously darkened chamber, which is now illuminated by a mystical light source... weird.\n"
                + "There appears to be a "
                + (Fore.CYAN + "mural")
                + "\033[39m on the wall. I should probably inspect it before leaving."
                + "\nTo the south lies a doorway to the coffin room ("
                + (Fore.YELLOW + "southern corridor")
                + "\033[39m)."
        )
        time.sleep(1)
        player.current_location.add_long_description(description)

        description = (
                "You're in a room illuminated by a mystical light source."
                + " There appears to be a "
                + (Fore.CYAN + "mural")
                + "\033[39m on the wall. I should probably inspect it before leaving.\n"
                + "To the south lies a doorway to the coffin room ("
                + (Fore.YELLOW + "southern corridor")
                + "\033[39m)."
        )
        player.current_location.add_shorter_description(description)

        # create boulder carving item and add to room, essentially a mural that depicts how they should use the dynamite should they inspect it
        # create boulder_carving
        boulder_carving = Item("mural")

        # give boulder_carving a description
        boulder_carving.add_description(
            "There are two murals on the wall. One, on the left, depicts a stick of dynamite placed on a giant boulder, \nand on the right a mural depicts an open doorway with the boulder shattered to smithereens. Something to keep in mind..."
        )

        player.current_location.add_item_to_room(boulder_carving)


def jump_puzzle(player):
    """In Andrew Room 3, the player must jump to pillars in the correct order to make it to the next room. There is a short pillar, medium pillar,
    and large pillar. The jump puzzle is fairly straight forward, the player must jump to the short pillar, then the medium, then the large. Upon
    doing so, they will transition to the next room. If they jump in the incorrect order, they will fall and take some damage."""

    # create variables to check pillar jump status
    in_room = False
    short_pillar = False
    medium_pillar = False
    large_pillar = False

    # check if player is in Andrew room 3
    if player.current_location.name == "Andrew 3":
        in_room = True
    # check if player has jumped onto a pillar
    for items in player.current_location.in_room:
        if items.name == "short pillar" and items.ability == True:
            short_pillar = True
        elif items.name == "medium pillar" and items.ability == True:
            medium_pillar = True
        elif items.name == "large pillar" and items.ability == True:
            large_pillar = True

    if in_room == True and (
            short_pillar == True or medium_pillar == True or large_pillar == True
    ):
        # if player's first move is not to jump to short pillar, print message and subtract hp
        if short_pillar == False:
            print("You jump and miss your target, falling back to the floor, ouch (-5 HP).")
            # lower player HP
            player.HP -= 5

            for items in player.current_location.in_room:
                if items.name == "short pillar" and items.ability == True:
                    items.ability = False
                elif items.name == "medium pillar" and items.ability == True:
                    items.ability = False
                elif items.name == "large pillar" and items.ability == True:
                    items.ability = False

            return

        # else, print message and receive user input for next jump
        print("You are standing on top of the short pillar.")
        time.sleep(.25)
        print("What will you do next?")
        response = input()
        # if player fails to jump to medium pillar, print fall message and subtract hp, repeat for large pillar jump next
        valid_list_medium = ["activate medium pillar", "jump to medium pillar", "jump medium pillar", "jump on medium pillar"]
        valid_list_large = ["activate large pillar", "jump to large pillar", "jump large pillar", "jump on large pillar"]
        if response not in valid_list_medium:
            print(response)
            print("You jump and miss your target, falling back to the floor, ouch (-7 HP).")
            player.HP -= 7

            for items in player.current_location.in_room:
                if items.name == "short pillar" and items.ability == True:
                    items.ability = False
                elif items.name == "medium pillar" and items.ability == True:
                    items.ability = False
                elif items.name == "large pillar" and items.ability == True:
                    items.ability = False
            return

        print("You are standing on top of the medium pillar")
        time.sleep(.25)
        print("What will you do next?")
        response = input()
        if response not in valid_list_large:
            print(response)
            print("You jump and miss your target, falling back to the floor, ouch (-10 HP).")
            player.HP -= 10

            for items in player.current_location.in_room:
                if items.name == "short pillar" and items.ability == True:
                    items.ability = False
                elif items.name == "medium pillar" and items.ability == True:
                    items.ability = False
                elif items.name == "large pillar" and items.ability == True:
                    items.ability = False
            return

        print(
            "You made it to the roof chamber. You find a rope nearby and lower it so you can slide down quickly..."
            + " not sure you have the strength to climb back up the rope though."
        )
        # move the player into the next room
        for items in player.current_location.in_room:
            items.ability = False
        player.current_location = player.current_location.north_wall


def explode_boulder(player):
    """If the player is in Andrew room 1 and activates dynamite, then places it in or on the boulder, the boulder will explode and reveal
    a door to a new room (Andrew room 3)."""
    # check if the player is in Andrew room 1
    if player.current_location.name == "Andrew 1":
        for items in player.current_location.in_room:
            if items.name == "boulder":
                for i in items.contains:
                    # if the player placed the dynamite in the boulder without lighting it, print message and return dynamite to room
                    if i.name == "dynamite" and i.ability == False:
                        print(
                            "There's not much point in placing unlit dynamite on the boulder, perhaps I should pick it up and light it..."
                        )
                        player.current_location.add_item_to_room(i)
                        items.remove_item_from_container(i)
                        return

                    # if the player correctly lights the dynamite and places it on the boulder, update room description to reveal the door
                    if i.name == "dynamite" and i.ability == True:
                        print(
                            "You place the stick of dynamite near the rock, and run. The rock explodes, leaving an open doorway."
                            + "\nDefying the laws of physics, there's almost no damage in your current room, but you hear rumblings to the east..."
                            + "\nIt must be in complete disarray."
                        )
                        # remove the boulder from the room
                        time.sleep(1)
                        player.current_location.in_room.remove(items)

                        # CONNECT west_three to west_one now that the boulder is gone
                        # create the shortened description for the room, will be displayed when you are visiting a room you have been to
                        description = (
                                "You enter a dark room with a pile of coffins and treaures in the corner.\nOne appears wooden ("
                                + (Fore.MAGENTA + "wooden coffin")
                                + "\033[39m)"
                                + " and ripped open, one appears metallic ("
                                + (Fore.MAGENTA + "metallic coffin")
                                + "\033[39m)"
                                + ", and the third appears to be small ("
                                + (Fore.MAGENTA + "small coffin")
                                + "\033[39m)"
                                + " and molded over."
                                + "\nOn the northern wall, there is a narrow passage that leads into a pitch black corridor ("
                                + (Fore.YELLOW + "northern corridor")
                                + "\033[39m"
                                + ").\nOn the eastern wall, where the boulder used to be, you spot a newly revealed eastern passage ("
                                + (Fore.YELLOW + "eastern corridor")
                                + "\033[39m).\nIn the southern corner of the room, lies a staircase leading back to Main Chamber (" + (
                                        Fore.YELLOW + "southern staircase") + "\033[39m" + ")."
                        )
                        # now add the description to the shortened_description attribute of the room
                        player.current_location.add_shorter_description(description)


# ------------------------------MERE's CLUSTER CONDITIONS ------------------------------------------------------
def light_candles(player):
    """
    When the user activates the candles in "mere cluster room 1", it triggers a puzzle
    the player must light the candles in a certain order to make a hidden item appear
    """
    if player.current_location.name == "mere cluster room 1":  # check to see if the player is in the right room
        for item in player.current_location.in_room:
            if item.name == "candles" and item.ability == True:
                # print(player.current_location.long_description)
                # print("")
                print("You see a small plaque below the candles. It reads:")
                print("Light the green candle first.")
                print("The second candle is somewhere to the left of the orange candle.")
                print("The third candle is not directly next to the red candle.")
                print("Light the blue candle last.")
                correct_answer = ["green", "red", "orange", "blue"]
                correct_count = 0
                print("You strike the match and look at the candles.")
                # loop for the number of candles
                for candle in range(0, 4):
                    # make sure the answer is only one word
                    choice = input("Which candle do you want to light?")
                    check_choice_len = choice.split()
                    while (len(check_choice_len) > 1 or len(check_choice_len) < 1):
                        # prompt again if the answer is not 1 word
                        print("Your answer should be 1 word!")
                        choice = input("Which candle do you want to light?")
                        check_choice_len = choice.split()

                    # check that the answer matches
                    # if the answer is correct, print the message and continue
                    if choice.lower() == correct_answer[candle]:
                        print("The candle flares to life. The flame dances cheerfully.")
                        # choice = input("Which candle do you want to light next?")
                        correct_count += 1
                    else:
                        print(
                            "The candles briefly flicker, then all go out. It appears you didn't light them in the correct order.")
                        item.toggle_ability()
                        return

                # if the user got all correct guesses, the candles should be disabled
                if correct_count == 4:
                    print(
                        "The candles flare up, then you hear a small click. A drawer slides open in the wall below the candles.")
                    player.current_location.remove_item_from_room(item)
                    description = "This is the room to the west of the Main Chamber.\nThere is a " + (
                                Fore.WHITE + "black patch") + '\033[39m' + " on the floor in the corner.\nThere is a row of " + (
                                              Fore.WHITE + "candles") + '\033[39m' + " along the southern wall.\nThey are burning cheerfully and light up the room.\nThere is a blue door on the northern wall (" + (
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
    # set the 3 riddles
    riddle1 = "A box without hinges, keys, or a lid\nYet inside, a golden treasure is hid."
    riddle2 = "I create my lair with silken string, and dispatch my prey with a biting sting."
    riddle3 = "I can run, but never walk\nI have a mouth, but never talk\nI have a head, but never weep\nI have a bed, but never sleep."
    # save the riddles paired with the correct answer
    riddle_list = [(riddle1, "egg"), (riddle2, "spider"), (riddle3, "river")]

    if player.current_location.name == "mere cluster room 2":  # check to see if the player is in the right room
        for enemies in player.current_location.enemies:  # iterate through enemies to find the sphinx
            if enemies.name == "sphinx" and enemies.is_dead != True:  # name must match and must not be dead
                print(enemies.e_description)
                print("The sphinx says 'You must answer my riddle to pass.'")
                answer = input('Do you wish to answer the riddle? (Y/N)')
                # prompt the user to answer a riddle
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    pass
                else:
                    print(
                        "You decide not to answer the sphinx's riddle.\nShe hisses and lashes her tail.\nYou think it would be best to leave.")
                    player.move_to_new_room("south")
                    input("Press Enter to return")
                    return
                choice = random.randrange(0, 3)
                riddle = riddle_list[choice]
                print(riddle[0])
                print("What is the correct answer?\n(Answer should be one word)")
                answer = input()
                # check the answer
                # if the answer is correct, sphinx should disappear from room
                if answer.lower() == riddle[1]:
                    enemies.is_dead = True
                    sapphire_from_sphinx(player)
                # if the answer is wrong, game is over
                else:
                    print(
                        "The sphinx whips her tail angrily and flexes her claws.\n'WRONG!' She yells, and lunges towards you.\nAs she spreads her wings, your vision fades to black.")
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
                print(
                    'The sphinx squawks, "You are correct" and flaps its wings, raising a large cloud of dust.\nYou cough and cover your eyes.\nWhen you look back up, she has vanished.')
                print('There is a smooth blue sphere resting on the floor where the sphinx was standing.')

                # now remove the sphinx from the room so that this condition does not trigger again next time you
                # enter this room
                player.current_location.enemies.remove(enemies)
                # create the sapphire that came from the sphinx
                blue_orb = Item("blue orb")
                blue_orb.add_description(
                    "A blue orb left behind when you solved the sphinx's riddle.\nIt looks like a sapphire. It's as big as your fist!")
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
    if player.current_location.name == "mere cluster room 3":  # check to see if the player is in the right room
        for item in player.inventory:  # check all the items in the player inventory
            if item.name == "torch" and item.ability == True:  # if the torch item is found, check if it's turned on
                # if the torch item is found and turned on, then the room description should print
                player.current_location.add_long_description(
                    "The torch lights up the darkness and illuminates the room.\nIt seems to have a rocky floor, and water drips down the walls.\nIt smells a bit dank and unpleasant.\n"
                    "There is a dark doorway on the southern wall, leading back the way you came (" + (
                                Fore.YELLOW + "southern door") + '\033[39m' + ").")
                player.current_location.add_shorter_description(
                    "The torch lights up the darkness and illuminates the room.\nThere is a dark doorway on the southern wall, leading back the way you came (" + (
                                Fore.YELLOW + "southern door") + '\033[39m' + ").")
                return
        # if the torch item is not found or is not turned on, then only an error message about the darkness
        # also need to show the room they previously came from so they can leave again
        player.current_location.add_long_description(
            "It is very dark and oppressive. You can't go further without a light.\nThere is a dark doorway on the southern wall, leading back the way you came (" + (
                        Fore.YELLOW + "southern door") + '\033[39m' + ").")
        player.current_location.add_shorter_description(
            "It is very dark and oppressive. You can't go further without a light.\nThere is a dark doorway on the southern wall, leading back the way you came (" + (
                        Fore.YELLOW + "southern door") + '\033[39m' + ").")
        return


def item_under_soil(player):
    """
    When the user picks up the soil in "mere cluster room 3", they find a buried fish
    """
    if player.current_location.name == "mere cluster room 3":  # check to see if the player is in the right room
        for item in player.inventory:  # check all the items in the player inventory
            if item.name == "soil":  # if the soil has been picked up
                # print some description about the soil falling to the ground
                print(
                    "The soil is damp and slips through your fingers. You don't have any way to hold it. You decide not to carry it.")
                print(
                    "While digging in the soil, you uncover something. You scrape the soil to the side and find a rotten fish.\nIt looks like it's been buried for awhile. It smells terrible.")
                input("Press Enter to return")
                player.inventory.remove(item)

                # create the rotten fish. it's a consumable (but why!)
                fish = Item("fish")
                # give the fish a description, including affect on HP if consumed
                fish.add_description(
                    "It's a smelly, rotten fish. You could eat it, but it wouldn't taste very good.\nHP -10")
                # give the fish an environmental description
                fish.add_env_description("There is a rotten " + (
                            Fore.BLUE + "fish") + '\033[39m' + " lying in a hollow. It was buried under some wet soil.")
                # set it as a consumable
                fish.toggle_can_consume()
                # set the effect of the consumable
                fish.set_consumable_effect(-15)
                # make it so you can pick up the fish
                fish.toggle_can_pick_up()
                # add the fish to the room
                player.current_location.add_item_to_room(fish)


def jackal_from_fish(player):
    """
    If the user picks up the rotten fish in "mere cluster room 3", they must fight a jackal
    """
    if player.current_location.name == "mere cluster room 3":  # check to see if the player is in the right room
        for item in player.inventory:  # check all the items in the player inventory
            if item.name == "fish":  # if the fish has been picked up
                for enemy in player.current_location.enemies:  # check if the jackal is already in the room
                    if enemy.name == "jackal":
                        return

                # create the jackal enemy
                jackal = Enemy("jackal")
                # add description
                jackal.add_description("A fierce jackal, with bared teeth. He looks angry.")
                # add an environmental description
                jackal.add_env_description("A " + (
                            Fore.RED + "jackal") + '\033[39m' + " lurks in the shadows. He is growling. Was the fish his?")
                # set HP
                jackal.set_HP(25)
                # set moves and their power/descriptions
                jackal.set_moves_and_power(1, "The jackal jumps at your leg and bites your foot!", 10)
                jackal.set_moves_and_power(2, "The jackal lunges at you, but missed", 0)
                jackal.set_moves_and_power(3, "The jackal extends his claws and scratches you!", 5)
                jackal.set_moves_and_power(4, "The jackal howls and charges into you!", 5)
                # add the enemy into the room
                player.current_location.add_enemy_to_room(jackal)


def give_jackal_fish(player):
    """
    If the user drops the rotten fish in "mere cluster room 3", the jackal will take it and leave
    """
    if player.current_location.name == "mere cluster room 3":  # check to see if the player is in the right room
        for item in player.current_location.in_room:  # check all the items in the room
            if item.name == "fish":  # if the fish has been dropped
                for enemy in player.current_location.enemies:  # check if the jackal is already in the room
                    if enemy.name == "jackal":
                        print(
                            "The jackal sniffs the air. He looks at you suspiciously.\nThen he trots over to the fish and picks it up in his mouth.")
                        print(
                            "The jackal slinks back into the shadows and disappears.\nAs he runs away, you notice something glint from beneath his feet.")
                        input("Press Enter to return")

                        # remove the fish from the room
                        player.current_location.remove_item_from_room(item)
                        # remove the jackal from the room
                        enemy.is_dead = True

                        # create the coin
                        coin = Item("coin")
                        # add description
                        coin.add_description(
                            "A shiny gold coin. It looks old and valuable. It was buried in the jackal's room.")
                        # add an environmental description
                        coin.add_env_description("A gold " + (
                                    Fore.WHITE + "coin") + '\033[39m' + " glitters in the dirt. It was uncovered when the jackal left.")
                        # add the item into the room
                        player.current_location.add_item_to_room(coin)
                        coin.toggle_can_pick_up()

                        if player.in_combat != None:
                            player.in_combat = None


def cross_chasm(player):
    """
    When the user encounters the "chasm" in "mere cluster room 4", they must equip the whip to cross
    """
    if player.current_location.name == "mere cluster room 4":  # check to see if the player is in the right room
        for item in player.inventory:
            if item.name == "whip" and player.equipped == item:
                for item in player.current_location.in_room:  # room check if bridge then return if found
                    if item.name == "bridge":
                        return
                # if the whip item is found, check if the bridge is in the room
                # if the whip is equipped, and bridge not present, the player can cross the chasm
                print(
                    "You carefully heft the whip in your hand, then take aim at the wooden bar above you.\nThe end of the whip coils around the bar, and you pull it tight.\n"
                    "You back up a few steps, then run foreward and swing across the chasm.\nYou land safely on the other side, and pull the whip back down behind you.")
                # brass sphinx should be added to room (on floor?)
                # maybe a door on the far side of chasm - fake treasure room?

                input("Press Enter to return")
                print(
                    "When you land on the far side of the chasm, you hear a click and the tile beneath your feet sinks slightly lower.\nYou hear a loud grinding sound, and a bridge slowly extends from the side of the chasm."
                    "\nOnce it reaches the other side, it locks into place. The noise stops, and the room is quiet.")
                input("Press Enter to return")

                # update the shortened description for the room
                description = "You hear the wind somewhere high overhead.\nThere is a large " + (
                        Fore.WHITE + "chasm") + '\033[39m' + " in the middle of the room. There is a thin " + (
                                      Fore.WHITE + "bridge") + '\033[39m' + " stretching from one side to the other.\nThere is a small wooden door on the eastern wall (" + (
                                      Fore.YELLOW + "eastern door") + '\033[39m' + ")."
                player.current_location.add_shorter_description(description)

                # add the bridge
                bridge = Item("bridge")
                # add description
                bridge.add_description(
                    "A thin bridge stretching across the chasm. It was operated by some hidden mechanism.\nYou're not sure what it's made of, but it seems strong.")
                # add the chasm to the room
                player.current_location.add_item_to_room(bridge)

                # add the tile
                tile = Item("tile")
                # add description
                tile.add_description(
                    "A ceramic tile, with a navy and gray pattern. It seems slightly different from all the others.\nIt feels a bit loose. You wonder if you could pick it up.")
                # We need to give the tile an environmental description, since it can be picked up
                tile.add_env_description("On the ground at your feet there is a " + (
                        Fore.WHITE + "tile") + '\033[39m' + " that seems to wobble a little when you step on it.")
                # make it so we can pick up the tile
                tile.toggle_can_pick_up()
                # add the tile to the room
                player.current_location.add_item_to_room(tile)


def item_under_tile(player):
    """
    When the user picks up the tile in "mere cluster room 4", they find a sphinx medallion
    """
    if player.current_location.name == "mere cluster room 4":  # check to see if the player is in the right room
        for item in player.inventory:  # check all the items in the player inventory
            if item.name == "tile":  # if the soil has been picked up
                # print some description about the tile revealing the sphinx medallion used in Main Chamber
                print(
                    "The tile is stuck to the floor, but wiggles when you touch it. You hear something rattle underneath.")
                print(
                    "You pull harder. With a jolt, the tile comes off. The force sends it flying out of your fingers and into the chasm.\nThere is a hole where the tile was. You see something metal inside.")
                input("Press Enter to return")
                player.inventory.remove(item)

                # create the brass sphinx, for the Main Chamber puzzle
                medallion = Item("medallion")
                # give the medallion a description
                medallion.add_description(
                    "It's a medallion in the shape of a sphinx. It looks like it's made of brass. You found it across the chasm, under a tile.")
                # give the fish an environmental description
                medallion.add_env_description("There is a brass " + (
                            Fore.WHITE + "medallion") + '\033[39m' + " in a shallow hole. It was buried underneath the tile.")
                # make it so you can pick up the medallion
                medallion.toggle_can_pick_up()
                # add the fish to the room
                player.current_location.add_item_to_room(medallion)
