from classes_and_functions import *
from build_board import *
import colorama
from colorama import Fore, Back, Style
import random

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
                            Fore.WHITE + "water") + '\033[39m' + ". You can now swim to the door on the southern wall(" + (
                                                                       Fore.YELLOW + "southern door") + '\033[39m' + ")."
                    player.current_location.shortened_description = "The room has been flooded. All that remains is a pool of glistening " + (
                            Fore.WHITE + "water") + '\033[39m' + ". You can now swim to the door on the southern wall(" + (
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
                    "A powerful axe that fell from a vanquished mummy. Might come in handy. \n Power: 35")
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
        if items.name == "tomato":
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
        tomato = Item("tomato")
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
                        player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up. Where the tree stood, there is now a " + (Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                        player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up. Where the tree stood, there is now a " + (Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                        for p in player.current_location.in_room:
                            if p.name == "tree":
                                player.current_location.remove_item_from_room(p)
                                return
                player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nOn the ground, there is a " + (Fore.WHITE + "patch") + '\033[39m' + " of grass covered in dirt. Looks like something is buried there.\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). Where the tree stood, there is now a " + (Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
                player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere is a " + (Fore.WHITE + "patch") + '\033[39m' + " of grass covered in dirt that looks like you can dig it up.\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). Where the tree stood, there is now a " + (Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
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
        "It looks like a letter is attached to the packet. It's from the adventurer's grandma. It reads:\nMy dearest Jacob,\nI hope you are doing well. I know you are going on a very dangerous exploration, and I'm worried for you.\nWhile you are gone, I want you to be able to remember the taste of home.\nSo, in this packet I'm sending you the spices that go into my famous stew that you always love.\nRemember, all you need to do is add some tomatoes and onions into a bowl with water.\nThen, just add the spices in and put the bowl in the oven for 5 minutes.\n I hope you make it back safely, please come back soon!\n Love,\nGrandma")
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
            player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere is a large oak " + (Fore.WHITE + "tree") + '\033[39m' + " in the center of the room.\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up."
            player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere is a large oak " + (Fore.WHITE + "tree") + '\033[39m' + " in the center of the room.\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up."
            return
    player.current_location.shortened_description = "A large room filled with grass and vegetation.\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up.\nWhere the tree stood, there is now a " + (Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."
    player.current_location.long_description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere are " + (Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (Fore.YELLOW + "northern door") + '\033[39m' + "). On the ground lies the body of an " + (Fore.WHITE + "adventurer") + '\033[39m' + " that you dug up.\nWhere the tree stood, there is now a " + (Fore.YELLOW + "passageway") + '\033[39m' + " leading underground."

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
                Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room. Behind you is the underground ' + (Fore.YELLOW + "passageway") + '\033[39m' + '.  A beautiful ' + (
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
                print("You shoot your fiery arrows into the chandelier, lighting the candle at the center")
                print("Suddenly, the room begins shaking! From the blazing furnace, an creature emerges!")
                print("The creature has the head of an eagle, but the body of a man. He towers over you menacingly.")
                print(
                    '"You should be proud of yourself, human. You have survived where none of your kind ever could," the creature says.')
                print(
                    '"However, your journey ends here. I am a guardian of this tomb, and a representative of the great goddess Nekhbet"')
                print(
                    '"While your courage has been admirable, I must perform my duty and slay you where you stand. Unless..."')
                print("The guardian pauses for a moment.")
                print('"By any chance do you know how to cook?" he asks curiously.')
                print(
                    '"I have been performing my duties defending this tomb for hundreds of years. Other than the occasional adventurer, I have not had real food in a long time"')
                print(
                    '"If you can get me some good food, I will gladly allow you to live. I will also give you the key that you seek to find the treasure."')
                print('"Return to me when you have what I want."')
                input("Press Enter to return")
                Guardian = Enemy("Guardian")
                Guardian.description = "This guardian has been tasked with guarding this tomb for hundreds of years.\nHe is a represetnative of Nekhbet, a patron god of Upper Egypt.\nHe looks pretty powerful.I shouldn't mess with him."
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
                        if p.name == "tomato":
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
        print("Granny's stew has been added to your inventory")
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
            print("On the ground where the Guardian was standing, the ground collapses, revealing what looks like a " + (Fore.YELLOW + "slide") + '\033[39m' + ". I wonder where it leads to.")
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
            player.current_location.long_description = 'You enter a sweltering chamber with a stone ' + (Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room. Behind you is the underground ' + (Fore.YELLOW + "passageway") + '\033[39m' + '. In the center of the room, there is a ' + (Fore.YELLOW + "slide") + '\033[39m' + ' leading somewhere. A beautiful ' + (Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nThese weapons are hanging on the wall beside you: '
            player.current_location.shortened_description = 'A sweltering room with a stone ' + (Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room.\nBehind you is the underground ' + (Fore.YELLOW + "passageway") + '\033[39m' + '. In the center of the room, there is a ' + (Fore.YELLOW + "slide") + '\033[39m' + ' leading somewhere. A beautiful ' + (Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nThese weapons are hanging on the walls: '


