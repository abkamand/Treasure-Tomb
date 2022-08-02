from classes_and_functions import *
from build_board import *
from Andrew_rooms import *
import colorama
from colorama import Fore, Back, Style
import random

colorama.init()


def check_conditions(player):

    # Andrew's Rooms conditions
    darkness_puzzle(player)
    explode_boulder(player)
    jump_puzzle(player)
    animal_puzzle(player)
    dead_to_dynamite(player)
    blow_out_torch(player)

    return


# ------------------------------Andrew's CLUSTER CONDITIONS ------------------------------------------------------
def dead_to_dynamite(player):
    """If a player lights dynamite in a location outside of Andrew room 1, they will have nowhere to place/throw it and it will blow up in
    their face, killing them."""
    # check if player is in Andrew room 1
    if player.current_location.name != "Andrew 1":
        # check if dynamite is lit
        for i in player.inventory:
            if i.name == "dynamite" and i.ability == True:
                print(
                    "You lit the dynamite in a room with nothing to place it in or on to effectively shield the blast. Any last words...?"
                )
                # kill the player
                player.HP = 0


def blow_out_torch(player):
    """If a player activates their torch in Andrew room 2 or has it active while entering said room, a mystical
    gust of wind will de-activate it to ensure the integrity of the darkness puzzle :)"""
    # check if player is in Andrew room 2
    if player.current_location.name != "Andrew 2":
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
            if items.name == "python pedestal" and python_puzzle == False:
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
                            "The eagle's eyes light up and it locks in place the second you placed it on the python pedestal... seems like you did something right."
                        )
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
                            "The alligator's eyes light up and it locks in place the second you placed it on the python pedestal... seems like you did something right."
                        )
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
                            "The python's eyes light and it locks in place up the second you placed it on the python pedestal... seems like you did something right."
                        )
                        alligator_solved = Item("alligator_solved")
                        player.current_location.add_item_to_room(alligator_solved)
                        alligator_puzzle = True
                        i.toggle_can_pick_up()

    # check if all 3 puzzles have been solved, if so, give the player the diamond key and update room description
    if alligator_puzzle == True and python_puzzle == True and eagle_puzzle == True:
        print(
            "A hole in the ceiling appears and a diamond key falls right into the palm of your hand. Seems useful... but where? Better keep it for now"
        )
        diamond_key_one = Item("Diamond Key 1")
        diamond_key_one.toggle_can_pick_up()
        player.add_to_inventory(diamond_key_one)

        description = (
            "You spot what appears to be an "
            + (Fore.CYAN + "animal carving")
            + "\033[39m on the wall. Perhaps you should inspect this further?"
            + "\nPedestals lie across the room with animal figures that you placed on top of each. Every figurine has glowing eyes, seemingly indicating your accomplishment."
            + "\nTo the south lies a passage to the coffin room ("
            + (Fore.YELLOW + "southern hole")
            + "\033[39m )."
        )
        player.current_location.add_shorter_description(description)


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
        if curr_row < 0 or curr_col < 0 or board[curr_row][curr_col] == 1:
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
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 2],
        ]

        # create directional movement representations
        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # create tuples representing current player location, previous, destination
        prev_location = (0, 0)
        curr_location = (0, 0)
        destination = (4, 4)

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
            "A stick of explosive dynamite. Looks like its still active, better be careful with fire around it and where I place it..."
        )

        # create environmental description
        dynamite.add_env_description(
            "A stick of explosive "
            + (Fore.GREEN + "dynamite")
            + "\033[39m lies on the floor in front of you. Better be careful not to accidentally light it without a purpose... "
        )

        # allow dynamite to be picked up
        dynamite.toggle_can_pick_up()
        # add ability to dynamite
        dynamite.can_activate_ability = True
        dynamite.ability_on_description = (
            "The dynamite is lit, quick, place it on something!"
        )
        dynamite.ability_off_description = "The dynamite is unlit... perhaps that's for the best unless I find something that needs blowing up. A giant rock maybe?"
        player.current_location.add_item_to_room(dynamite)

        # create darkness puzzle item to act as a pseudo breakout of the function so player doesn't have to replay this minigame
        darkness_solved = Item("darkness_solved")
        player.current_location.add_item_to_room(darkness_solved)

        # update room description post-gameplay completion, room is now illuminated
        description = (
            "You are in the previously darkened chamber, which is now illuminated by a mystical light source... weird."
            + "There appears to be a "
            + (Fore.CYAN + "mural")
            + "\033[39m on the wall. I should probably inspect it before leaving."
            + "\nTo the south lies a doorway to the coffin room ("
            + (Fore.YELLOW + "southern corridor")
            + "\033[39m)."
        )
        player.current_location.add_long_description(description)

        description = (
            "You're in a room illuminated by a mystical light source."
            + "There appears to be a "
            + (Fore.CYAN + "mural")
            + "\033[39m on the wall. I should probably inspect it before leaving."
            + "\nTo the south lies a doorway to the coffin room ("
            + (Fore.YELLOW + "southern corridor")
            + "\033[39m)."
        )
        player.current_location.add_shorter_description(description)

        # create boulder carving item and add to room, essentially a mural that depicts how they should use the dynamite should they inspect it
        # create boulder_carving
        boulder_carving = Item("mural")

        # give boulder_carving a description
        boulder_carving.add_description(
            "There are two murals on the wall, one, on the left, depicts a stick of dynamite placed on a giant boulder on the left, \nand on the right a mural depicts an open doorway with the boulder shattered to smithereens. Something to keep in mind..."
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
        if items.name == "short_pillar" and items.ability == True:
            short_pillar = True
        elif items.name == "medium_pillar" and items.ability == True:
            medium_pillar = True
        elif items.name == "large_pillar" and items.ability == True:
            large_pillar = True

    if in_room == True and (
        short_pillar == True or medium_pillar == True or large_pillar == True
    ):
        # if player's first move is not to jump to short pillar, print message and subtract hp
        if short_pillar == False:
            print("You jump and fall back to the floor, ouch (-5 HP).")
            # lower player HP
            player.HP -= 5
            return

        # else, print message and receive user input for next jump
        print("You are standing on top of the short pillar")
        print("What will you do next?")
        response = input()
        # if player fails to jump to medium pillar, print fall message and subtract hp, repeat for large pillar jump next
        if response != "activate medium_pillar":
            print("You jump and fall back to the floor, ouch (-7 HP)")
            player.HP -= 7
            return

        print("You are standing on top of the medium pillar")
        print("What will you do next?")
        response = input()
        if response != "activate large_pillar":
            print("You jump and fall back to the floor, ouch (-10 HP)")
            player.HP -= 10
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
                            + "\nDefying the laws of physics, there's almost no damage in your current room, but you hear rumblings in the northern room..."
                            + "\nit must be in complete disarray."
                        )
                        # remove the boulder from the room
                        player.current_location.in_room.remove(items)

                        # CONNECT west_three to west_one now that the boulder is gone
                        # create the shortened description for the room, will be displayed when you are visiting a room you have been to
                        description = (
                            "You enter a dark room with a pile of coffins and treaures in the corner.\nOne appears"
                            + (Fore.MAGENTA + " wooden")
                            + "\033[39m"
                            + " and ripped open, one appears"
                            + (Fore.MAGENTA + " metallic")
                            + "\033[39m"
                            + ", and the third appears to be"
                            + (Fore.MAGENTA + " small")
                            + "\033[39m"
                            + " and molded over."
                            + "\nPerhaps you should take a closer look at the coffins for anything useful?"
                            + "\nOn the northern wall, there is a narrow passage that leads into a pitch black corridor ("
                            + (Fore.YELLOW + "northern corridor")
                            + "\033[39m"
                            + ").\nOn the eastern wall, where the boulder used to be, you spot a newly revealed eastern passage ("
                            + (Fore.YELLOW + "eastern corridor")
                            + "\033[39m)."
                        )
                        # now add the description to the shortened_description attribute of the room
                        player.current_location.add_shorter_description(description)
