import random

# initial board state
BOARD = {'A1': 'wr', 'B1': 'wk',  'C1': 'wb',  'D1': 'wq', 'E1': 'wk',  'F1': 'wb',  'G1': 'wk', 'H1': 'wr',
         'A2': 'wp', 'B2': 'wp',  'C2': 'wp',  'D2': 'wp', 'E2': 'wp',  'F2': 'wp',  'G2': 'wp', 'H2': 'wp',
         'A3': '--',  'B3': '--',   'C3': '--',   'D3': '--',  'E3': '--',   'F3': '--',   'G3': '--',  'H3': '--',
         'A4': '--',  'B4': '--',   'C4': '--',   'D4': '--',  'E4': '--',   'F4': '--',   'G4': '--',  'H4': '--',
         'A5': '--',  'B5': '--',   'C5': '--',   'D5': '--',  'E5': '--',   'F5': '--',   'G5': '--',  'H5': '--',
         'A6': '--',  'B6': '--',   'C6': '--',   'D6': '--',  'E6': '--',   'F6': '--',   'G6': '--',  'H6': '--',
         'A7': 'bp', 'B7': 'bp',  'C7': 'bp',  'D7': 'bp', 'E7': 'bp',  'F7': 'bp',  'G7': 'bp', 'H7': 'bp',
         'A8': 'br', 'B8': 'bk',  'C8': 'bb',  'D8': 'bq', 'E8': 'bk',  'F8': 'bb',  'G8': 'bk', 'H8': 'br'}

# render the board
def render(board):
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

    # use 3 dictionaries to create a 3x3 render
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    dict5 = {}
    dict6 = {}
    dict7 = {}
    dict8 = {}

    # the count will kepp track of the key during the for loop so that the correct 'x' and '0'
    # are placed in the correct dictionary.

    count = 0
    for key in board:
        if count < 8:
                dict1[key] = board[key]
        if count >= 8 and count < 16:
                dict2[key] = board[key]
        if count >= 16 and count < 24:
                dict3[key] = board[key]
        if count >= 24 and count < 32:
                dict4[key] = board[key]
        if count >= 32 and count < 40:
                dict5[key] = board[key]
        if count >= 40 and count < 48:
                dict6[key] = board[key]
        if count >= 48 and count < 56:
                dict7[key] = board[key]
        if count >= 56 and count < 64:
                dict8[key] = board[key]
        count += 1
    print(dict1)
    print(dict2)
    print(dict3)
    print(dict4)
    print(dict5)
    print(dict6)
    print(dict7)
    print(dict8)




# dictates the player moves
def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

    move_completed = False

    # the combination of while loop and try/exception ensures that the user inputs the correct strings
    # or that the computer randoms a valid int

    while move_completed == False:

            try:
                action = input(f"{player['name']}'s turn! Pick a piece to move (enter a key ex: 'D2'): ")
                action2 = input("What square would you like to move the piece to (enter a key ex: 'D2'): ")

                if BOARD[action] == '--':
                    raise Exception
                if BOARD[action2] != '--':
                    print("taking Piece!")
                BOARD[action2] = BOARD[action]
                BOARD[action] = '--'
                render(BOARD)
                move_completed = True

            except:
                print("invalid move. Try again: ")

# initiates and manages the game
def play_chess():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''
    print("Chess is starting...")
    print("Rules are not enforced in this game, we rely on the honor system to play correct moves.")

    name = input("name: ")

    game_choice = False

    # another while = try/except loop to ensure the user submits x or 0 without breaking the game for an exception raised
    while game_choice == False:

        try:
            choice = input("Would you like White or Black (type 'w' or 'b'): ")
            if choice == 'w' or choice == 'b':
                 game_choice = True
            else:
                 raise Exception
        except:
            print("Please enter a valid choice :")

    # player 2 becomes whatever player 1 didn't select
    choice2 = None
    if choice == 'w':
        choice2 = 'b'
    else:
        choice2 = 'w'

    name2 = input("name: ")
    player2 ={
        "name": name2,
        "choice": choice2
    }

    # player info is stored in an object
    player = {
        "name": name,
        "choice": choice
    }

    game_round = 0
    game_over = False

    while not game_over:


        # the 9x9 board is rendered after each round
        render(BOARD)
        game_round += 1
        print(f"Round {game_round}!")

        # each player will select their action
        get_action(player)

        get_action(player2)

        check_in = input("continue (type 'no' to exit)? ")
        if check_in == 'no':
              game_over = True
