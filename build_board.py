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
                          Fore.WHITE + "Carvings") + '\033[39m' + "adorn the walls of the room, depicting a map of a " \
                                                                  "large river and several inscriptions. Below the " \
                                                                  "statue, there is an ornate " + (
                          Fore.WHITE + "sink") + '\033[39m' + "with a faucet in the shape of a waterfall.\nHigh above " \
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

    sink = Item("sink")
    sink.add_description(
        "A sink located at the base of the statue of Khnum. The faucet is in the shape of a waterfall, and is slowly "
        "dripping water. How is there even water down here?")
    sink.toggle_can_activate_ability()

    carvings = Item("carvings")
    carvings.add_description(
        'The carvings show a map of the Nile River. Along the river, there are several hieroglyphs.\nAccording to '
        'your research, the translation is : "Quench the Gods".\nWonder what that means.')

    chalice = Item("chalice")
    chalice.add_description(
        "A golden chalice. Looks like it used to be fit for a king, but now its old and rusted.")
    chalice.add_env_description("In the sink there is a golden " + (Fore.WHITE + "chalice") + '\033[39m' + ".")
    chalice.toggle_can_pick_up()
    chalice.toggle_can_activate_ability()

    # create the mummy
    mummy = Enemy("mummy")
    # add description
    mummy.add_description("A terrifying mummy wrapped in cloth.")
    # add an environmental description
    mummy.add_env_description(
        "In the corner a " + (
                Fore.RED + "mummy") + '\033[39m' + "rises from what looks like a sarcophagus. The mummy's dry and "
                                                   "rotting skin falls from his face as he removes a large axe from "
                                                   "the wall.\nHis body is wrapped in decaying cloth and rusted "
                                                   "armor. He walks menacingly towards you.")
    # set its HP
    mummy.set_HP(100)
    # set its moves and the moves'
    mummy.set_moves_and_power(1, "The mummy lunges at you with his axe, slashing downward with its withered hands!", 10)
    mummy.set_moves_and_power(2, "The mummy throws you against the wall!", 5)
    mummy.set_moves_and_power(3, "The mummy swings his axe at you, but you manage to dodge him!", 0)
    mummy.set_moves_and_power(4, "The mummy bashes you on head with the handle of his axe!", 10)

    Water_Room.add_item_to_room(statue)
    Water_Room.add_item_to_room(sink)
    Water_Room.add_item_to_room(carvings)
    Water_Room.add_item_to_room(chalice)
    Water_Room.add_enemy_to_room(mummy)

    Main_Chamber.add_adjacent_room("east", Water_Room)
    Water_Room.add_adjacent_room("west", Main_Chamber)

    #-----------------------------------------------------------------------------------------------------------------
    #----------------------------------- ASHWIN ROOM 2 : GREEN ROOM --------------------------------------------------
    # this is the room connected to the water room from the south

    # room has vegetation with plenty of fruits and vegetables
    # a massive tree stands in the middle of the room.
    # carvings on the wall. ONLY THROUGH DEATH CAN YOU PROCEED
    # you get attacked by a mummy gardener with a shovel. He will drop the shovel
    # if you use the shovel, you will dig up dead bodies of adventurers. That's what is making everything grow.
    # on the body of one of the dead adventurers, there is a recipe for stew and a new sword
    # if you use the axe in the room, you will cut down the tree. This will reveal a new room, since the tree is hollow
    # this reveals the next room





    #-------------------------------- ASHWIN ROOM 3 : FURNACE ROOM ---------------------------------------------------
    # this is the room connected to the green room from the east
    # the room is really hot
    # made of stone and brick
    # furnace at the far end with the mummy
    # a large chandelier made of unlit candles hangs from the ceiling
    # there are carvings depicting Ra traveling across the sky in his solar bark, illuminating the world
    # there is a heavily armored mummy in here, working at the furnace to create weapons
    # he doesn't attack you outright, allows you to choose your weapons and then challenge him
    # there are weapons scattered around the room
    # when you defeat him, he drops his bowl-shaped helmet
    # in order to open the room, you need to light a bow and arrow on fire and shoot it at the chandelier to light it
    # next door opens


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


