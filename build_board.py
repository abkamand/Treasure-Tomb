from classes_and_functions import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()


#  regular items are white
#  consumable items are blue
#  weapon items are magenta
#  rooms are yellow
#  enemies are red

def build_the_board():
    # -----------------------------------------------MAIN CHAMBER---------------------------------------------------

    Main_Chamber = Room("Main Chamber")

    description = "After hours of trekking through the dank and dangerous caverns, you finally arrive at the tomb  you've been looking for.\nYou walk into a large chamber, filled with ornate decorations and paintings on the ceiling.\nThere appears to be giant " + (
            Fore.WHITE + "mosaic") + '\033[39m' + " on the floor.\nOn the eastern wall, there is a heavy,golden door with a depiction of a eagle on it (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ").\nOn the northern wall, there is a staircase leading into the depths of the tomb, with a carving of a crocodile at the top of the stairs (" + (
                          Fore.YELLOW + "northern staircase") + '\033[39m' + ").\nOn the western wall, there is another golden door. This one has the image of a sphinx carved into it (" + (
                          Fore.YELLOW + "western door") + '\033[39m' + ").\nWhat appears to be the " + (
                          Fore.WHITE + "corpse") + '\033[39m' + " of a man lays in the center of the room."

    Main_Chamber.add_long_description(description)

    description = "A vast room full of ornate decorations.\nThere appears to be giant " + (
            Fore.WHITE + "mosaic") + '\033[39m' + " on the floor.\nOn the eastern wall, there is a heavy,golden door with a depiction of a eagle on it (" + (
                          Fore.YELLOW + "eastern door") + '\033[39m' + ").\nOn the northern wall, there is a staircase leading into the depths of the tomb, with a carving of a crocodile at the top of the stairs (" + (
                          Fore.YELLOW + "northern staircase") + '\033[39m' + ").\nOn the western wall, there is another golden door. This one has the image of a sphinx carved into it (" + (
                          Fore.YELLOW + "western door") + '\033[39m' + ").\nWhat appears to be the " + (
                          Fore.WHITE + "corpse") + '\033[39m' + " of a man lays in the center of the room."

    Main_Chamber.add_shorter_description(description)

    mosaic = Item("mosaic")

    mosaic.add_description(
        " This mosaic depicts a pharaoh standing on a stage above his subordinates.\nHe his holding a large, red diamond above his head.\nThe crowd amassed at his feet appears to be worshiping him.\nAbove the diamond, there are 3 indentations in the shape of an eagle, a crocodile, and a sphinx.\nIt looks like you could fill in those indentations with the right piece of the mosaic...")

    corpse = Item("corpse")
    corpse.add_description(
        "The corpse appears to have been here for a long time.\nThe body has rotten and all that remains is a skeleton.\nI hope I don't end up like that guy.")

    note = Item("note")
    note.add_description(
        "This is a note that was laying next to the corpse in the Main Chamber.\nIt says TURN BACK OR YOU WILL DIE! ")
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
    torch.add_description("This is a torch that can be used to illuminate rooms that are dark")
    torch.add_env_description(
        "There is a " + (Fore.WHITE + "torch") + '\033[39m' + " on the ground next to the corpse.")
    torch.toggle_can_activate_ability()
    torch.add_ability_on_description("The torch has been lit and is glowing brightly.")
    torch.add_ability_off_description("The torch has been put out.")
    torch.toggle_can_pick_up()

    painkillers = Item("pink painkillers")
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
                                                              "there is a door leading back into the " + (
                          Fore.YELLOW + "Main Chamber") + '\033[39m' + "."
    Water_Room.add_long_description(description)

    description = "A damp room containing a " + (
            Fore.WHITE + "statue") + '\033[39m' + " in the center of the room.\nThere is a " + (
                          Fore.WHITE + "sink") + '\033[39m' + " at the base of the statue.\n" + (
                          Fore.WHITE + "Carvings") + '\033[39m' + " decorate the walls.\nThere is a door high above " \
                                                                  "you on the southern wall, with no way to get to " \
                                                                  "it. On the western wall, there is a door leading " \
                                                                  "back into the " + (
                          Fore.YELLOW + "Main Chamber") + '\033[39m' + "."
    Water_Room.add_shorter_description(description)

    statue = Item("statue")
    statue.add_description(
        "A statue of a man with the head of a ram.\nHis mouth is open and his jaws are outstretched, exposing large, "
        "jagged teeth.\nHe is wearing a gold tunic and holds spear-like object.\nBased on your research, this is the "
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
        "A golden chalice. Looks like it used to be fit for a king, but now its old and rusted.")
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

    description = "You're in a large chamber covered, with vegetation and grass covering every inch of the floor and walls.\nHow are all of these things growing down here?\nThere is a large oak " + (
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
        " The first picture depicts a king and a queen ruling over their subjects.\n The following scenes show a man dismembering the king and scattering the remains.\nFalcons search for the remains and after finding them, they put them back together as a mummy.\n The king rises again. Based on your research, these hieroglyphs are showing the myth of the resurrection and death of Osiris, the god of fertility and agriculture.\nThe last scene says 'ONLY THROUGH DEATH CAN YOU PASS'.\nThat doesn't sound good.")

    shovel = Item("shovel")
    shovel.add_description(
        "A standard shovel. It's in decent shape considering it's been down here for hundreds of years.")
    shovel.add_env_description("There is a " + (Fore.MAGENTA + "shovel") + '\033[39m' + " leaning against the tree.")
    shovel.toggle_can_pick_up()
    shovel.is_weapon = True
    shovel.set_weapon_power(10)

    onion = Item("onion")
    onion.add_description(
        "An onion. I usually wouldn't eat this plain, but desperate times call for desperate measures.")
    onion.add_env_description(
        "Around the tree, there are " + (Fore.BLUE + "onion") + '\033[39m' + " roots scattered on the ground.")
    onion.toggle_can_pick_up()
    onion.toggle_can_consume()
    onion.set_consumable_effect(5)

    tomato = Item("tomato")
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
                Fore.WHITE + "furnace") + '\033[39m' + ' at the far end of the room. Behind you is the underground ' + (Fore.YELLOW + "passageway") + '\033[39m' + '.  A beautiful ' + (
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





    # ------------------------------ ASHWIN ROOM 4: RIDDLE ROOM -----------------------------------------------------
    # a plain room
    # there is a mummy standing at the far end
    # he speaks to you. He warns you not to fight him because he is unkillable
    # he says that he is supposed to give you a riddle, but really just wants a warm, homecooked meal
    # in exchange he will give you the eagle key
    # you have to use the recipe you got from the buried traveler
    # get the water from the water room pool
    # get the plants from the green room
    # use the furnace in the furnace room
    # this results in a nice stew you can give the guy
    # if you do, he gives you the eagle key and opens a door back to the main chamber

    player = Player()

    player.current_location = Main_Chamber

    return player
