from classes_and_functions import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()


#  regular items that can be picked up = GREEN
#  item objects in rooms that can't be picked up = CYAN
#  consumable items = BLUE
#  weapon items = MAGENTA
#  rooms = YELLOW
#  enemies = RED

def build_the_board():
    # -----------------------------------------------MAIN CHAMBER---------------------------------------------------

    Main_Chamber = Room("Main Chamber")

    description = "After hours of trekking through the dank and dangerous caverns, you finally arrive at the tomb you've been looking for.\nYou walk into a large chamber, filled with ornate decorations and paintings on the ceiling.\nThere appears to be a giant " + (
            Fore.WHITE + "mosaic") + '\033[39m' + " on the floor.\nOn the eastern wall, there is a heavy golden door with a depiction of an eagle on it (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ").\nOn the northern wall, there is a staircase leading into the depths of the tomb, with a carving of a crocodile at the top of the stairs (" + (
                          Fore.YELLOW + "northern staircase") + '\033[39m' + ").\nOn the western wall, there is another golden door. This one has the image of a sphinx carved into it (" + (
                          Fore.YELLOW + "western door") + '\033[39m' + ").\nWhat appears to be the " + (
                          Fore.WHITE + "corpse") + '\033[39m' + " of a man lays in the center of the room."

    Main_Chamber.add_long_description(description)

    description = "A vast room full of ornate decorations.\nThere appears to be a giant " + (
            Fore.WHITE + "mosaic") + '\033[39m' + " on the floor.\nOn the eastern wall, there is a heavy golden door with a depiction of an eagle on it (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ").\nOn the northern wall, there is a staircase leading into the depths of the tomb, with a carving of a crocodile at the top of the stairs (" + (
                          Fore.YELLOW + "northern staircase") + '\033[39m' + ").\nOn the western wall, there is another golden door. This one has the image of a sphinx carved into it (" + (
                          Fore.YELLOW + "western door") + '\033[39m' + ").\nWhat appears to be the " + (
                          Fore.WHITE + "corpse") + '\033[39m' + " of a man lays in the center of the room."

    Main_Chamber.add_shorter_description(description)

    mosaic = Item("mosaic")

    mosaic.add_description(
        "This mosaic depicts a pharaoh standing on a stage above his subordinates.\nHe is holding a large, red diamond above his head.\nThe crowd amassed at his feet appears to be worshipping him.\nAbove the diamond, there are 3 indentations in the shape of an eagle, a crocodile, and a sphinx.\nIt looks like you could fill in those indentations with the right piece of the mosaic...")

    corpse = Item("corpse")
    corpse.add_description(
        "The corpse appears to have been here for a long time.\nThe body has rotten and all that remains is a skeleton.\nI hope I don't end up like that guy.")

    note = Item("note")
    note.add_description(
        "This is a note that was next to the corpse in the Main Chamber.\nIt says TURN BACK OR YOU WILL DIE! ")
    note.add_env_description("On the ground next to the corpse there is a " + (
            Fore.WHITE + "note") + '\033[39m' + " written on a piece of paper.")
    note.toggle_can_pick_up()

    sword = Item("sword")
    sword.add_description(
        "This is a sword. Kind of outdated, but it looks like it could do some serious damage.\nPower: 25")
    sword.add_env_description(
        "There is a " + (Fore.MAGENTA + "sword") + '\033[39m' + " impaled in the skeleton of the corpse.")
    sword.toggle_is_weapon()
    sword.set_weapon_power(25)
    sword.toggle_can_pick_up()

    torch = Item("torch")
    torch.add_description("This is a torch that can be used to illuminate rooms that are dark.")
    torch.add_env_description(
        "There is a " + (Fore.WHITE + "torch") + '\033[39m' + " on the ground next to the corpse.")
    torch.toggle_can_activate_ability()
    torch.add_ability_on_description("The torch has been lit and is glowing brightly.")
    torch.add_ability_off_description("The torch has been put out.")
    torch.toggle_can_pick_up()

    painkillers = Item("painkillers")
    painkillers.add_description("Looks like a bottle of painkillers.\nHP +15")
    painkillers.add_env_description(
        "Looks like there is a bottle of " + (Fore.BLUE + "painkillers") + '\033[39m' + " in the corpse's pocket.")
    painkillers.toggle_can_consume()
    painkillers.set_consumable_effect(15)
    painkillers.toggle_can_pick_up()

    Main_Chamber.add_item_to_room(mosaic)
    Main_Chamber.add_item_to_room(corpse)
    Main_Chamber.add_item_to_room(sword)
    Main_Chamber.add_item_to_room(torch)
    Main_Chamber.add_item_to_room(painkillers)
    Main_Chamber.add_item_to_room(note)

    # ----------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------ ASHWIN ROOM 1 : WATER ROOM --------------------------------------------
    #  this is the first room down the eastern door with the eagle

    Water_Room = Room("Water Room")

    description = "You're in a dim and damp room with white limestone walls surrounding you on all sides. The smell " \
                  "of mildew and death lingers in the air. \nAs the door closes behind you, you hear a low-pitched " \
                  "moan emanate from the corner of the room.\nYou scan the room, making out a large " + (
                          Fore.WHITE + "statue") + '\033[39m' + " in the center of the room.\n" + (
                          Fore.WHITE + "Carvings") + '\033[39m' + " adorn the walls of the room, depicting a map of a " \
                                                                  "large river and several inscriptions. Below the " \
                                                                  "statue, there is an ornate " + (
                          Fore.WHITE + "sink") + '\033[39m' + " with a faucet in the shape of a waterfall.\nHigh above " \
                                                              "you, there is a door on the southern wall. There " \
                                                              "appears to be no way to reach it. On the western wall, " \
                                                              "there is a door leading back to the " + (
                          Fore.YELLOW + "Main Chamber") + '\033[39m' + "."
    Water_Room.add_long_description(description)

    description = "A damp room containing a " + (
            Fore.WHITE + "statue") + '\033[39m' + " in the center of the room.\nThere is a " + (
                          Fore.WHITE + "sink") + '\033[39m' + " at the base of the statue.\n" + (
                          Fore.WHITE + "Carvings") + '\033[39m' + " decorate the walls.\nThere is a door high above " \
                                                                  "you on the southern wall, with no way to get to " \
                                                                  "it. On the western wall, there is a door leading " \
                                                                  "back to the " + (
                          Fore.YELLOW + "Main Chamber") + '\033[39m' + "."
    Water_Room.add_shorter_description(description)

    statue = Item("statue")
    statue.add_description(
        "A statue of a man with the head of a ram.\nHis mouth is open and his jaws are outstretched, exposing large, "
        "jagged teeth.\nHe is wearing a gold tunic and holds a spear-like object.\nBased on your research, this is the "
        "Egyptian deity Khnum.\nKhnum was the god of water and procreation, and was believed to be the source of the "
        "Nile River.")
    statue.toggle_can_activate_ability()
    statue.can_contain = True
    statue.container_type = "contains"

    sink = Item("sink")
    sink.add_description(
        "A sink located at the base of the statue of Khnum. The faucet is in the shape of a waterfall, and is slowly "
        "dripping water. How is there even water down here?")
    sink.toggle_can_activate_ability()
    sink.ability_on_description = "You turn the knob and water begins to flow out of the faucet."
    sink.ability_off_description = "You turn the knob and close the faucet."

    carvings = Item("carvings")
    carvings.add_description(
        'The carvings show a map of the Nile River. Along the river, there are several hieroglyphs.\nAccording to '
        'your research, the translation is : "Quench the Gods".\nWonder what that means.')

    chalice = Item("chalice")
    chalice.add_description(
        "A golden chalice. Looks like it used to be fit for a king, but now it's old and rusted.")
    chalice.add_env_description("In the sink there is a golden " + (Fore.WHITE + "chalice") + '\033[39m' + ".")
    chalice.toggle_can_pick_up()
    chalice.can_contain = True
    chalice.container_type = "holding"

    # create the mummy
    water_mummy = Enemy("mummy")
    # add description
    water_mummy.add_description("A terrifying mummy wrapped in cloth.")
    # add an environmental description
    water_mummy.add_env_description(
        "In the corner a " + (
                Fore.RED + "mummy") + '\033[39m' + " rises from what looks like a sarcophagus. The mummy's dry and "
                                                   "rotting skin falls from his face as he removes a large sword from "
                                                   "the wall.\nHis body is wrapped in decaying cloth and rusted "
                                                   "armor. He walks menacingly towards you.")
    # set its HP
    water_mummy.set_HP(25)
    # set its moves and the moves'
    water_mummy.set_moves_and_power(1,
                                    "The mummy lunges at you with his sword, slashing downward with its withered hands!",
                                    10)
    water_mummy.set_moves_and_power(2, "The mummy throws you against the wall!", 5)
    water_mummy.set_moves_and_power(3, "The mummy swings his sword at you, but you manage to dodge him!", 0)
    water_mummy.set_moves_and_power(4, "The mummy bashes you on head with the hilt of his sword!", 10)

    Water_Room.add_item_to_room(statue)
    Water_Room.add_item_to_room(sink)
    Water_Room.add_item_to_room(carvings)
    Water_Room.add_item_to_room(chalice)
    Water_Room.add_enemy_to_room(water_mummy)

    Main_Chamber.add_adjacent_room("east", Water_Room)
    Water_Room.add_adjacent_room("west", Main_Chamber)

    # -----------------------------------------------------------------------------------------------------------------
    # ----------------------------------- ASHWIN ROOM 2 : GREEN ROOM --------------------------------------------------
    # this is the room connected to the water room from the south

    # room has vegetation with plenty of fruits and vegetables
    # a massive tree stands in the middle of the room.
    # carvings on the wall. ONLY THROUGH DEATH CAN YOU PROCEED
    # you get attacked by a mummy gardener with a shovel. He will drop the shovel
    # if you use the shovel, you will dig up dead bodies of adventurers. That's what is making everything grow.
    # on the body of one of the dead adventurers, there is a recipe for stew and a new sword
    # if you use the axe in the room, you will cut down the tree. This will reveal a new room, since the tree is hollow
    # this reveals the next room

    Green_Room = Room("Green Room")

    description = "You're in a large chamber with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere is a large oak " + (
            Fore.WHITE + "tree") + '\033[39m' + " in the center of the room.\nOn the ground, there is a " + (
                          Fore.WHITE + "patch") + '\033[39m' + " of grass covered in dirt. Looks like something is buried there.\nThere are " + (
                          Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls. I should take a closer look.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                          Fore.YELLOW + "northern door") + '\033[39m' + ")."
    Green_Room.add_long_description(description)

    description = "A large room filled with grass and vegetation.\nThere is a large oak " + (
            Fore.WHITE + "tree") + '\033[39m' + " in the center of the room and a " + (
                          Fore.WHITE + "patch") + '\033[39m' + " of grass covered in dirt that looks like you can dig it up.\nThere are " + (
                          Fore.WHITE + "pictures") + '\033[39m' + " carved into the moss on the walls.\nOn the northern wall, there is a door that leads back to the flooded room (" + (
                          Fore.YELLOW + "northern door") + '\033[39m' + ")."
    Green_Room.add_shorter_description(description)

    tree = Item("tree")
    tree.add_description("A massive oak tree in the center of the room. Who knows how it's able to grow down here?")
    tree.toggle_can_activate_ability()

    patch = Item("patch")
    patch.add_description("This part of the ground has been disturbed. Looks like something was recently buried here.")
    patch.toggle_can_activate_ability()

    pictures = Item("pictures")
    pictures.add_description(
        "The first picture depicts a king and a queen ruling over their subjects.\nThe following scenes show a man dismembering the king and scattering the remains.\nFalcons search for the remains and after finding them, they put them back together as a mummy.\nThe king rises again. Based on your research, these hieroglyphs are showing the myth of the resurrection and death of Osiris, the god of fertility and agriculture.\nThe last scene says 'ONLY THROUGH DEATH CAN YOU PASS'.\nThat doesn't sound good.")

    shovel = Item("shovel")
    shovel.add_description(
        "A standard shovel. It's in decent shape considering it's been down here for hundreds of years.\nPower: 10")
    shovel.add_env_description("There is a " + (Fore.MAGENTA + "shovel") + '\033[39m' + " leaning against the tree.")
    shovel.toggle_can_pick_up()
    shovel.is_weapon = True
    shovel.set_weapon_power(10)

    onion = Item("onion")
    onion.add_description(
        "An onion. I usually wouldn't eat this plain, but desperate times call for desperate measures.")
    onion.add_env_description(
        "Around the tree, there are " + (Fore.BLUE + "onion") + '\033[39m' + " roots growing out of the ground.")
    onion.toggle_can_pick_up()
    onion.toggle_can_consume()
    onion.set_consumable_effect(5)

    tomato = Item("tomatoes")
    tomato.add_description("A juicy tomato")
    tomato.add_env_description((Fore.BLUE + "Tomatoes") + '\033[39m' + " hang from vines on the ceiling.")
    tomato.toggle_can_pick_up()
    tomato.toggle_can_consume()
    tomato.set_consumable_effect(5)

    # create the mummy
    green_mummy = Enemy("mummy")
    # add description
    green_mummy.add_description("A terrifying mummy wrapped in cloth.")
    # add an environmental description
    green_mummy.add_env_description("You hear a rumbling from underneath you, and a " + (
            Fore.RED + "mummy") + '\033[39m' + " emerges from the soil in front of you. He charges at you with an axe.")
    # set its HP
    green_mummy.set_HP(25)
    # set its moves and the moves'
    green_mummy.set_moves_and_power(1,
                                    "The mummy lunges at you with his axe, slashing downward with its withered hands!",
                                    10)
    green_mummy.set_moves_and_power(2, "The mummy throws you against the wall!", 5)
    green_mummy.set_moves_and_power(3, "The mummy swings his axe at you, but you manage to dodge him!", 0)
    green_mummy.set_moves_and_power(4, "The mummy bashes you on head with the handle of his axe!", 10)

    Green_Room.add_item_to_room(tree)
    Green_Room.add_item_to_room(patch)
    Green_Room.add_item_to_room(pictures)
    Green_Room.add_item_to_room(shovel)
    Green_Room.add_item_to_room(onion)
    Green_Room.add_item_to_room(tomato)
    Green_Room.add_enemy_to_room(green_mummy)

    Water_Room.add_adjacent_room("south", Green_Room)
    Green_Room.add_adjacent_room("north", Water_Room)

    # -------------------------------- ASHWIN ROOM 3 : BLACKSMITH'S ROOM ---------------------------------------------------
    # this is the room connected to the green room from the east
    # the room is really hot
    # made of stone and brick
    # furnace at the far end with the mummy
    # a large chandelier made of unlit candles hangs from the ceiling
    # there are carvings depicting Ra traveling across the sky in his solar bark, illuminating the world
    # there is a heavily armored mummy in here, working at the furnace to create weapons
    # he doesn't attack you outright, allows you to choose your weapons
    # there are weapons scattered around the room
    # when you defeat him, he drops his bowl-shaped helmet
    # in order to open the room, you need to light a bow and arrow on fire and shoot it at the chandelier to light it
    # next door opens

    # items:
    # furnace, chandelier, carvings
    # e items:
    # mace, spear, bow
    # enemy: armored mummy

    Blacksmith_Room = Room("Blacksmith Room")

    description = 'You enter a sweltering chamber with a stone ' + (
                Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room. Behind you is the underground ' + (Fore.YELLOW + "passageway") + '\033[39m' + '.\nA beautiful ' + (
                              Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (
                              Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nNext to the furnace, a massive armored figure with a dome-shaped helmet hammers a piece of steel on an anvil. As you enter, the figure turns towards you. Another ' + (Fore.RED + "mummy") + '\033[39m' + '. \nThe mummy bellows, "You have desecrated this sacred place! Choose your weapon and challenge me!\nWell, this is not good. Better choose a weapon.\nThese weapons are hanging on the wall beside you: '
    Blacksmith_Room.add_long_description(description)

    description = 'A sweltering room with a stone ' + (Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room.\nBehind you is the underground ' + (Fore.YELLOW + "passageway") + '\033[39m' + '. A beautiful ' + (
                              Fore.WHITE + "chandelier") + '\033[39m' + ' with a large, unlit candle hangs from the ceiling and intricate ' + (
                              Fore.WHITE + "carvings") + '\033[39m' + ' adorn the walls.\nThese weapons are hanging on the walls: '
    Blacksmith_Room.add_shorter_description(description)

    furnace = Item("furnace")
    furnace.add_description("A large furnace with a raging fire.")
    furnace.toggle_can_activate_ability()
    furnace.can_contain = True
    furnace.container_type = "holding"


    chandelier = Item("chandelier")
    chandelier.add_description("An ornate chandelier with a single, large candle sitting in the center.")
    chandelier.toggle_can_activate_ability()

    carvings2 = Item("carvings")
    carvings2.add_description(
        "The carvings depict a rebellion of humans against the king of gods, Ra.\nThe next scene shows Ra transforming into a lion that slaughters many of the humans.\nThe carving shows Ra repenting for his carnage by creating daylight, sailing across the sky each day.\nThe hieroglyphics translate to ILLUMINATE THE SKY.")

    mace = Item("mace")
    mace.add_description("A medieval style mace. Power: 40")
    mace.add_env_description("a " + (Fore.MAGENTA + "mace") + '\033[39m')
    mace.is_weapon = True
    mace.set_weapon_power(40)
    mace.can_pick_up = True

    spear = Item("spear")
    spear.add_description("A long spear. Power: 40")
    spear.add_env_description("a " + (Fore.MAGENTA + "spear") + '\033[39m')
    spear.is_weapon = True
    spear.set_weapon_power(40)
    spear.can_pick_up = True

    bow = Item("bow and arrows")
    bow.add_description("A bow and quiver of arrows. Power: 15")
    bow.add_env_description("a " + (Fore.MAGENTA + "bow and arrows") + '\033[39m')
    bow.is_weapon = True
    bow.set_weapon_power(15)
    bow.can_pick_up = True



    armored_mummy = Enemy("mummy")
    # add description
    armored_mummy.add_description("A terrifying mummy wearing plate armor")
    armored_mummy.add_env_description("The armored " + (Fore.RED + "mummy") + '\033[39m' + " waits for you to challenge him.")

    # set its HP
    armored_mummy.set_HP(25)
    # set its moves and the moves'
    armored_mummy.set_moves_and_power(1,
                                    "The mummy lunges at you with his broadsword, swinging widly and knocking you down!",
                                    20)
    armored_mummy.set_moves_and_power(2, "The mummy throws you against the wall!", 10)
    armored_mummy.set_moves_and_power(3, "The mummy swings his axe at you, but you manage to dodge him!", 0)
    armored_mummy.set_moves_and_power(4, "The mummy bashes you on head with the handle of his axe!", 15)

    Blacksmith_Room.add_item_to_room(furnace)
    Blacksmith_Room.add_item_to_room(chandelier)
    Blacksmith_Room.add_item_to_room(carvings2)
    Blacksmith_Room.add_item_to_room(bow)
    Blacksmith_Room.add_item_to_room(spear)
    Blacksmith_Room.add_item_to_room(mace)
    Blacksmith_Room.add_enemy_to_room(armored_mummy)

    Green_Room.add_adjacent_room("east", Blacksmith_Room)
    Blacksmith_Room.add_adjacent_room("west", Green_Room)
    Blacksmith_Room.add_adjacent_room("north", Main_Chamber)


#--------------------------------ANDREW ROOMS -----------------------------------------------------------------

    # create andrew room 1
    West_one = Room("Andrew 1")

    # create long description
    description = (
            "You find yourself in a dark chamber with coffins strewn about. There are cobwebs everywhere and the walls are covered with dust and mold. "
            + "\nSquinting at the coffins to get a better glimpse, you spot three total: One appears wooden ("
            + (Fore.CYAN + "wooden coffin")
            + "\033[39m)"
            + " and ripped open, one is metallic ("
            + (Fore.CYAN + "metallic coffin")
            + "\033[39m)"
            + ", and the third is small ("
            + (Fore.CYAN + "small coffin")
            + "\033[39m)"
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
            + " blocks the way to the eastern chamber.\nYou'll need some way of removing it... explosives maybe?\nIn the southern corner of the room, lies a staircase leading back to Main Chamber (" + (
                        Fore.YELLOW + "southern staircase") + "\033[39m" + ")."
    )
    # now add the description to the long_description attribute of the room. This is the description that will pop up the first time you enter the room
    West_one.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = (
            "You enter a dark room with a pile of coffins and treasures in the corner.\nOne appears wooden ("
            + (Fore.CYAN + "wooden coffin")
            + "\033[39m)"
            + " and ripped open, one appears metallic ("
            + (Fore.CYAN + "metallic coffin")
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
            + " blocks the way to the eastern chamber.\nIn the southern corner of the room, lies a staircase leading back to Main Chamber (" + (
                        Fore.YELLOW + "southern staircase") + "\033[39m" + ")."
    )
    # now add the description to the shortened_description attribute of the room
    West_one.add_shorter_description(description)

    # create wooden coffin
    wooden_coffin = Item("wooden coffin")
    # give the wooden coffin a description
    wooden_coffin.add_description(
        "A putrid smell surrounds the coffin, the wood is rotten, and there is a large hole in the cover revealing a half mummified corpse.\nThe mummy is holding a box of " 
        + (Fore.MAGENTA + "matches") + "\033[39m."
    )
    # since the wooden coffin cannot be picked up, we don't need to give it an e_description

    # create metallic coffin
    metallic_coffin = Item("metallic coffin")
    # give the metallic coffin a description
    metallic_coffin.add_description(
        "The coffin is coated in a metal of some sort... gold... silver... platinum?\nIt's difficult to discern in the dark, the metal is reflective, greeting you with a blurred silhouette of yourself.\nIt doesn't have a clear opening, a weapon of some sort may be needed to get inside..."
    )

    # create small coffin
    small_coffin = Item("small coffin")
    # give the small coffin a description
    small_coffin.add_description(
        "The coffin is similar in construction to the cracked, wooden coffin, albeit its much smaller... wait, does that mean its just a Box?\nIt appears to contain an assortment of golden platewear."
    )

    matches = Item("matches")
    matches.add_description("A box of matches that can be used to light dynamite.")
    matches.toggle_can_pick_up()
    matches.add_env_description("")

    # create boulder
    boulder = Item("boulder")
    boulder.add_description("A giant boulder.")
    # boulder.can_activate_ability = True
    boulder.can_contain = True

    # now add the items into the room
    # items are read in the order added
    West_one.add_item_to_room(wooden_coffin)
    West_one.add_item_to_room(metallic_coffin)
    West_one.add_item_to_room(small_coffin)
    West_one.add_item_to_room(boulder)
    West_one.add_item_to_room(matches)

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
            + " leading straight to the newly revealed chamber in the ceiling.\nYou'll have to make a series of jumps to get up there."
            + "\nTo the west lies a passage to the coffin room ("
            + (Fore.YELLOW + "western corridor")
            + "\033[39m)."
    )

    West_three.add_long_description(description)

    # create short description
    description = (
            "There's rubble and dust everywhere. "
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
            + " leading straight to the newly revealed chamber."
            + "\nTo the west lies a passage to the coffin room ("
            + (Fore.YELLOW + "western corridor")
            + "\033[39m)."
    )

    West_three.add_shorter_description(description)

    # Create room 3 items
    # create short pillar
    short_pillar = Item("short pillar")
    # add description
    short_pillar.add_description(
        "A short pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )
    # toggle ability for the puzzle in conditions, so can track if player jumps on it
    short_pillar.can_activate_ability = True

    # create medium pillar
    medium_pillar = Item("medium pillar")
    # add description
    medium_pillar.add_description(
        "A medium pillar stands out among the rubble, looks particularly sturdy if someone were to jump on..."
    )
    # toggle ability for the puzzle in conditions, so can track if player jumps on it
    medium_pillar.can_activate_ability = True

    # create large pillar
    large_pillar = Item("large pillar")
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
            + "\033[39m."
            + "\nTo the south lies a rope leading down into the pillar room ("
            + (Fore.YELLOW + "southern hole")
            + "\033[39m)."
    )

    West_four.add_long_description(description)

    # create short description
    description = (
            "You spot what appears to be an "
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
            + "\033[39m."
            + "\nTo the south lies a rope leading down into the pillar room ("
            + (Fore.YELLOW + "southern hole")
            + "\033[39m)."
    )

    West_four.add_shorter_description(description)

    # Create the item objects we will need for the Python, Alligator, Eagle puzzle to be implemented in conditions.py
    # Player must pick up the python, alligator, and eagle figurines. Player must place the eagle figurine on the Python pedestal,
    # the Alligator figurine on the eagle pedestal, and the Python figurine on the Alligator pedestal to unlock the diamond key.

    # create animal carving that depicts the solution
    animal_carving = Item("animal carving")
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
        + (Fore.GREEN + "python figurine")
        + "\033[39m)"
        + ", rests on the floor."
    )
    # allow figurine to be picked up
    python_figurine.toggle_can_pick_up()

    # create python pedestal
    python_pedestal = Item("snake pedestal")
    # add description
    python_pedestal.add_description(
        "A pedestal with an open space made for an object. The base of the pedestal depicts a dead python with a prominent skull front and center."
    )
    # allow items sto be placed in the pedestal
    python_pedestal.can_contain = True
    python_pedestal.container_type = "holding"
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
    alligator_pedestal.container_type = "holding"

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
    eagle_pedestal.container_type = "holding"

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

    # connect Main Chamber to room 1
    Main_Chamber.add_adjacent_room("north", West_one)
    West_one.add_adjacent_room("south", Main_Chamber)

    # room 1 to 3
    West_one.add_adjacent_room("east", West_three)

    # room 3 to 1
    West_three.add_adjacent_room("west", West_one)

    # 1 to 2
    West_one.add_adjacent_room("north", West_two)

    # 2 to 1
    West_two.add_adjacent_room("south", West_one)

    # 3 to 4
    West_three.add_adjacent_room("north", West_four)

    # 4 to 3
    West_four.add_adjacent_room("south", West_three)

    # -------------------------------------------------------------------------------------------------
    # --------------------------------- Mere ROOM 1 : CANDLE ROOM -------------------------------------
    #  this is the first room down the western door with the sphinx
    #  this room has a row of candles along the wall that must be lit in order
    #  connected to the Main Chamber to the east, sphinx room to the north, chasm room to the west

    # create the first room
    Mere_Room_1 = Room("mere cluster room 1")

    # create the long description
    description = "This is the room to the west of the Main Chamber. It smells dusty and damp.\nThere are large pillars lining the walls.\nIt feels like the entrance to an ancient temple.\nThere is a " + (
                Fore.WHITE + "black patch") + '\033[39m' + " on the floor in the corner." \
                                                           "\nThere is a row of " + (
                              Fore.WHITE + "candles") + '\033[39m' + " along the southern wall.\nThere is a blue door on the northern wall (" + (
                          Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a small wooden door on the western wall (" + (
                          Fore.YELLOW + "western door") + '\033[39m' + ").\nThere is a door on the eastern wall leading back to the Main Chamber (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_1.add_long_description(description)

    # create the shortened description for the room
    description = "This is the room to the west of the Main Chamber. \nThere is a " + (
                Fore.WHITE + "black patch") + '\033[39m' + " on the floor in the corner.\nThere is a row of " + (
                              Fore.WHITE + "candles") + '\033[39m' + " along " \
                                                                     "the southern wall. \nThere is a blue door on the northern wall (" + (
                              Fore.YELLOW + "northern door") + '\033[39m' + ").\n" \
                                                                            "There is a small wooden door on the western wall (" + (
                              Fore.YELLOW + "western door") + '\033[39m' + ").\nThere is a door on the eastern wall leading back to the Main Chamber (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_1.add_shorter_description(description)

    # add the candles to the room
    candles = Item("candles")
    # give them a description
    candles.add_description(
        "There is a shallow alcove with 4 candles arranged in a line. \nEach candle is a different color: red, blue, green, and orange.\nThere is a long match nearby."
    )
    # the candles can be activated to trigger a puzzle
    candles.toggle_can_activate_ability()
    candles.add_ability_on_description(
        "You stare at the row of candles, studying them thoughtfully. Something prompts you to pick up the matchstick.")
    candles.add_ability_off_description(
        "You decide to put the matchstick back. You aren't sure if you should light the candles.")

    # add the firepit to the room
    firepit = Item("black patch")
    # give it a description
    firepit.add_description(
        "The floor is scorched, and has small particles of soot all around. It smells faintly smoky.\nYou think there was probably a fire here."
    )

    # add the items to the room
    Mere_Room_1.add_item_to_room(candles)
    Mere_Room_1.add_item_to_room(firepit)

    # connect the main chamber with Mere_Room_1
    # use the add_adjacent_room function to add Mere_Room_1 as the room on the west wall of the Main Chamber
    Main_Chamber.add_adjacent_room("west", Mere_Room_1)
    # since Mere_Room_1 is on the west wall of the main chamber, that means the Main Chamber is east of Mere_Room_1
    Mere_Room_1.add_adjacent_room("east", Main_Chamber)


    # --------------------------------- Mere ROOM 2 : SPHINX ROOM -------------------------------------
    #  this is the second room down the western door with the sphinx
    #  this room has a sphinx that must be defeated by correctly answering a riddle
    #  connected to the candle room to the south, dark room to the north

    # create the room
    Mere_Room_2 = Room("mere cluster room 2")

    # create the long description
    description = "This room has a low ceiling and is littered with small sticks and feathers. It has an irregular floor, with dirt and debris scattered haphazardly around.\nThere is a huge " + (Fore.WHITE + "nest") + '\033[39m' + " in the corner.\nThere is an elaborate " + (Fore.WHITE + "painting") + '\033[39m' + " covering the western wall.\nThere is a dark doorway on the northern wall (" + (
            Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a blue door on the southern wall (" + (
                          Fore.YELLOW + "southern door") + '\033[39m' + ")."
    Mere_Room_2.add_long_description(description)

    # create the shortened description for the room
    description = "The room has a messy dirt floor. \nThere is a huge " + (Fore.WHITE + "nest") + '\033[39m' + " in the corner.\nThere is an elaborate " + (Fore.WHITE + "painting") + '\033[39m' + " covering the western wall.\nThere is a dark doorway on the northern wall (" + (
            Fore.YELLOW + "northern door") + '\033[39m' + ").\nThere is a blue door on the southern wall (" + (
                          Fore.YELLOW + "southern door") + '\033[39m' + ")."
    Mere_Room_2.add_shorter_description(description)

    # create the sphinx
    sphinx = Enemy("sphinx")
    # add description
    sphinx.add_description("A fierce sphinx with golden fur.\nShe has black hair and amber eyes.")
    # add environmental description
    sphinx.add_env_description("A fierce " + (
                Fore.RED + "sphinx") + '\033[39m' + " reclines in the center of the room.\nShe has the body of a lion, the wings of an eagle, and the head of a woman.\nShe rises as you enter the room")
    # set its HP
    sphinx.set_HP(10000)
    # set its moves and their descriptions and damage
    sphinx.set_moves_and_power(1, "The sphinx slashes at you with her claws!", 500)
    sphinx.set_moves_and_power(2, "The sphinx slashes at you with her claws!", 500)
    sphinx.set_moves_and_power(3, "The sphinx slashes at you with her claws!", 500)
    sphinx.set_moves_and_power(4, "The sphinx slashes at you with her claws!", 500)
    # add the enemy into the room
    Mere_Room_2.add_enemy_to_room(sphinx)

    # create the nest
    nest = Item("nest")
    # give it a description
    nest.add_description(
        "There is a large nest made of twigs and bits of cloth. There are many feathers lying in and around.\nYou think this must be where the sphinx slept.")
    # add the nest to the room
    Mere_Room_2.add_item_to_room(nest)

    # create the painting
    painting = Item("painting")
    # give it a description
    painting.add_description(
        "There is a colorful painting stretching across the wall. It depicts a sphinx standing in the desert, with people around her.\nYou think it's the same sphinx who had been in the room.")
    # add the painting to the room
    Mere_Room_2.add_item_to_room(painting)

    # connect Mere_Room_2 with Mere_Room_1
    # use the add_adjacent_room function to add Mere_Room_2 as the room on the north wall of Mere_Room_1
    Mere_Room_1.add_adjacent_room("north", Mere_Room_2)
    # since Mere_Room_2 is on the north wall of Mere_Room_1, that means Mere_Room_1 is south of Mere_Room_2
    Mere_Room_2.add_adjacent_room("south", Mere_Room_1)


    # --------------------------------- Mere ROOM 3 : DARK ROOM -------------------------------------
    #  this is the third room down the western door with the sphinx
    #  this room is very dark and must be illuminated with the torch activated
    #  connected to the sphinx room to the south

    # create the room
    Mere_Room_3 = Room("mere cluster room 3")

    # create the long description
    description = "It is very dark and oppressive.\nYou can't go further without a light."
    Mere_Room_3.add_long_description(description)

    # create the shortened description for the room
    description = "It is very dark and oppressive.\nYou can't go further without a light."
    Mere_Room_3.add_shorter_description(description)

    # connect Mere_Room_3 with Mere_Room_2
    # use the add_adjacent_room function to add Mere_Room_3 as the room on the north wall of Mere_Room_2
    Mere_Room_2.add_adjacent_room("north", Mere_Room_3)
    # since Mere_Room_3 is on the north wall of Mere_Room_2, that means Mere_Room_2 is south of Mere_Room_3
    Mere_Room_3.add_adjacent_room("south", Mere_Room_2)


    # --------------------------------- Mere ROOM 4 : CHASM ROOM -------------------------------------
    #  this is the fourth room down the western door with the sphinx
    #  this room has a chasm that can be crossed by equipping the whip
    #  connected to the candle room to the west

    # this is the code for mere's room 4
    # create the room
    Mere_Room_4 = Room("mere cluster room 4")

    # create the long description
    description = "This room is very long and skinny. It looks twice as long as the other rooms.\nYou smell fresh air and hear a breeze far above you.\nYou can barely make out the shapes of bats fluttering far overhead.\nThere must be an opening to the outside somewhere.\n" \
                  "There is a large " + (
                          Fore.WHITE + "chasm") + '\033[39m' + " in the middle of the room stretching from wall to wall.\nThere is a wooden bar above the chasm, but it's too high to reach.\nThere is a small wooden door on the eastern wall (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_4.add_long_description(description)

    # create the shortened description for the room
    description = "You hear the wind somewhere high overhead.\nThere is a large " + (
            Fore.WHITE + "chasm") + '\033[39m' + " in the middle of the room.\nThere is a small wooden door on the eastern wall (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ")."
    Mere_Room_4.add_shorter_description(description)

    # create the whip
    whip = Item("whip")
    # add description
    whip.add_description(
        "A long leather whip. It looks strong and flexible.\nYou could use it to attack, or to grab something far away.\nPower: 15")
    # add environmental description
    whip.add_env_description("There is a coiled " + (
            Fore.MAGENTA + "whip") + '\033[39m' + " on the floor. Perhaps it was left behind by some other explorer.")
    whip.toggle_can_pick_up()
    # we need to set it as a weapon
    whip.toggle_is_weapon()
    # we need to set the power of the whip
    whip.set_weapon_power(15)
    # add the whip into the room
    Mere_Room_4.add_item_to_room(whip)

    # create the chasm
    chasm = Item("chasm")
    # add description
    chasm.add_description("A dark chasm. You can't see the bottom.\nIt's too large to jump across.")
    # add the chasm to the room
    Mere_Room_4.add_item_to_room(chasm)

    # connect Mere_Room_4 with Mere_Room_1
    # use the add_adjacent_room function to add Mere_Room_4 as the room on the west wall of Mere_Room_1
    Mere_Room_1.add_adjacent_room("west", Mere_Room_4)
    # since Mere_Room_4 is on the west wall of Mere_Room_1, that means Mere_Room_1 is east of Mere_Room_4
    Mere_Room_4.add_adjacent_room("east", Mere_Room_1)







    player = Player()

    player.current_location = Main_Chamber

    return player