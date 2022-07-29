def darkness_puzzle():
    def valid(curr, prev, mov, board):
        update_row = curr[0] + mov[0]
        update_col = curr[1] + mov[1]
        prev = curr
        curr = (update_row, update_col)

        curr_row = curr[0]
        curr_col = curr[1]

        if curr_row < 0 or curr_col < 0 or board[curr_row][curr_col] == 1:
            print("You run into something hard, ouch! Can't move that way.")
            curr = prev
            return curr

        elif board[curr_row][curr_col] == 0:
            print(
                "You successfully move a few paces into the darkness. How will you move next?"
            )
            return curr

        elif board[curr_row][curr_col] == 2:
            print("You successfully move a few paces into the darkness.")
            return curr

    # how to accomplis this "solved", perhaps create a hidden item in the room that activates when puzzle is complete, check if that item is active,
    # if so, return
    solved = False

    # if the player has already completed the puzzle once, the room is illuminated
    if solved == True:
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

    # create variable for current player location, previous, destination
    prev_location = (0, 0)
    curr_location = (0, 0)
    destination = (4, 4)

    while curr_location != destination:
        response = input()

        if response == "move right":
            curr_location = valid(curr_location, prev_location, right, board)

        elif response == "move left":
            curr_location = valid(curr_location, prev_location, left, board)

        elif response == "move down":
            curr_location = valid(curr_location, prev_location, down, board)

        elif response == "move up":
            curr_location = valid(curr_location, prev_location, up, board)

        else:
            print("Invalid movement.")

    print("Suddenly, you hear a clicking noise. The room is suddenly illuminated.")
    solved = True


if __name__ == "__main__":
    darkness_puzzle()
