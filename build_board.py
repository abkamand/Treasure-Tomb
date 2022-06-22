from classes_and_functions import *


def build_the_board():
    # create the room, using the name of the room as the argument
    Test_Room = Room("Test_Room")

    # create the long description of the room you just made, and then add it to the room
    description = "This is a test room. On the eastern wall there is a painting of a man on a horse.  There is a door " \
                  "on the western wall. This is the long-form description that will appear the first time the player " \
                  "is in this room.  "
    Test_Room.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = "Room with a painting of man on a horse. Door on western wall"
    Test_Room.add_shorter_description(description)

    # need to create the Item objects first before they can be added to the room

    # first we will create the book
    book = Item("book")
    # give the book a description
    book.add_description("This is a fake description for the book that was found on the table")
    # give the book an environmental description
    book.add_env_description("There is a book laying on a table")
    # make it so we can pick up the book
    book.toggle_can_pick_up()

    # now create the coffee mug
    mug = Item("mug")
    # give mug a description
    mug.add_description("This is a test description for the coffee mug in the test room. Mug with carving of a dog on "
                        "it")
    # give the book an environmental description
    mug.add_env_description("There is a mug sitting on the table in the room")
    # make it so we can pick up the mug
    mug.toggle_can_pick_up()

    # now create the painting
    painting = Item("painting")
    # give the painting a description
    painting.add_description("This is a test description fo the painting of a man on a horse in the test room")
    # we don't need to give the painting an environmental description since we can't pick it up

    # now add the items into the room
    Test_Room.add_item_to_room(book)
    Test_Room.add_item_to_room(mug)
    Test_Room.add_item_to_room(painting)









    # create the room to the west of the test room
    West_Room = Room("West_Room")

    # create the long description of the room you just made, and then add it to the room
    description = "This is the room to the west of the test room. There is a sarcophagus in the middle of the room. " \
                  "It looks too heavy to carry. The room is full of gold and smells terrible." \
                  " There are pictures carved in the walls depicting something."
    West_Room.add_long_description(description)

    # create the shortened description for the room, will be displayed when you are visiting a room you have been to
    description = "Room containing a sarcophagus and carvings in the wall"
    West_Room.add_shorter_description(description)

    # need to create the Item objects first before they can be added to the room

    # first we will create the sarcophagus
    sarcophagus = Item("sarcophagus")
    # give the sarcophagus a description
    sarcophagus.add_description("This is a fake description for the sarcophagus that was found in the western room")
    # since we can't pick it up we don't need an env description

    # now create the gold chalice
    chalice = Item("chalice")
    # give chalice a description
    chalice.add_description(
        "This is a test description for the chalice that you can pick up in the western room. Made of solid gold and "
        "found next to the sarcophagus")
    # give the book an environmental description
    chalice.add_env_description("There is a chalice on the ground next to the sarcophagus. Looks like solid gold")
    # make it so we can pick up the mug
    chalice.toggle_can_pick_up()

    # now create the wall carvings
    carvings = Item("carvings")
    # give the carvings a description
    carvings.add_description(
        "This is a test description for the wall carvings. The carvings depict a pharaoh holding up a glowing "
        "diamond. People are worshipping him")
    # we don't need to give the carvings an environmental description since we can't pick it up

    # now add the items into the room
    West_Room.add_item_to_room(sarcophagus)
    West_Room.add_item_to_room(chalice)
    West_Room.add_item_to_room(carvings)

    # now we need to connect the Test Room and West Room
    Test_Room.add_adjacent_room("west", West_Room)
    West_Room.add_adjacent_room("east", Test_Room)

    # now add the player to the room
    player = Player()
    player.current_location = Test_Room

    return player
