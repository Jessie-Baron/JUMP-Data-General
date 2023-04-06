BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}

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
    dict1 = {}
    dict2 = {}
    dict3 = {}
    count = 0
    for key in board:
        if count < 3:
            dict1[count + 1] = board[key]
        if count >= 3 and count < 6:
            dict2[count + 1] = board[key]
        if count >= 6:
            dict3[count + 1] = board[key]
        count += 1
    print(dict1)
    print(dict2)
    print(dict3)
def is_valid(action):
    for i in range(1, 10):
        if int(action) == i:
            return True
    return False

def is_available(action):
    if BOARD[action] == ' ':
        return True
    return False

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

    while move_completed == False:

            try:
                action = int(input(f"{player['name']}'s turn! Pick a number between 1 and 9: "))
                if action > 9 or action < 1:
                    raise Exception
                BOARD[action] = player['choice']
                move_completed = True
            except:
                print("invalid response. Try again: ")

def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------
    print(f"{player['name']} wins!")

def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------
    if BOARD[1] == player['choice'] and BOARD[2] == player['choice'] and BOARD[3] == player['choice']:
        return True
    if BOARD[4] == player['choice'] and BOARD[5] == player['choice'] and BOARD[6] == player['choice']:
        return True
    if BOARD[7] == player['choice'] and BOARD[8] == player['choice'] and BOARD[9] == player['choice']:
        return True
    if BOARD[1] == player['choice'] and BOARD[5] == player['choice'] and BOARD[9] == player['choice']:
        return True
    if BOARD[3] == player['choice'] and BOARD[5] == player['choice'] and BOARD[7] == player['choice']:
        return True

def play_t3():
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
    print("Tic Tac Toe starting...")

    name = input("name: ")
    choice = input("Would you like X or 0 (type 'x' or '0'): ")
    opponent = input("Would you like to play against a computer or a human (type 'c' or 'h'): ")

    choice2 = None
    if choice == 'x':
        choice2 == '0'
    else:
        choice2 == 'x'

    if opponent == 'h':
        name2 = input("name: ")
        player2 = {
            "name": name2,
            "choice": choice2
        }
    else:
        name2 = 'computer'
        player2 = {
            "name": name2,
            "choice": choice2
        }


    player = {
        "name": name,
        "choice": choice
    }

    game_round = 0
    game_over = False

    while not game_over:

        render(BOARD)
        game_round += 1
        print(f"Round {game_round}!")

        get_action(player)
        if check_win(player):
            victory_message(player)

            game_end = False

            while game_end == False:

                play_again = input("Would you like to play again (Please enter 'yes' or 'no') : ")

                if play_again == 'yes':
                    game_round = 0
                elif play_again == 'no':
                    game_over = True
                else:
                    print("Please enter a valid response: ")


        # game_over = True # Delete this line when you're ready to run the loop.

        # Print the current state of the board

        # Get the current player's action and assign it to a variable called 'action'.

        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.

        # Increment the game round by 1.

        # Check if the game is winnable (game_round >= 4),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).

        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.

        # switch players with a quick conditional loop.


    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop

        # and reinitiate the game loop (play_t3()).
