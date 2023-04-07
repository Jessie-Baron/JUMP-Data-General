import random

# initial board state
BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}

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

    # the count will kepp track of the key during the for loop so that the correct 'x' and '0'
    # are placed in the correct dictionary.

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
                if player['name'] == 'computer':
                    action = random.randint(1, 9)
                else:
                    action = int(input(f"{player['name']}'s turn! Pick a number between 1 and 9: "))

                if action > 9 or action < 1:
                    raise Exception
                elif BOARD[action] != ' ':
                    raise Exception
                BOARD[action] = player['choice']
                move_completed = True

            except:
                print("invalid response. Try again: ")

# declares victory for a player
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

    # we must render the board so that it prints 3x3
    render(BOARD)
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

    # a series of if state,ents can be hardcoded to check for valid victories
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
    if BOARD[1] == player['choice'] and BOARD[4] == player['choice'] and BOARD[7] == player['choice']:
        return True
    if BOARD[2] == player['choice'] and BOARD[5] == player['choice'] and BOARD[8] == player['choice']:
        return True
    if BOARD[3] == player['choice'] and BOARD[6] == player['choice'] and BOARD[9] == player['choice']:
        return True

# initiates and manages the game
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

    # clears the board from the last game
    for key in BOARD:
        BOARD[key] = ' '

    name = input("name: ")

    game_choice = False

    # another while = try/except loop to ensure the user submits x or 0 without breaking the game for an exception raised
    while game_choice == False:

        try:

            choice = input("Would you like X or 0 (type 'x' or '0'): ")
            if choice == 'x' or choice == '0':
                 game_choice = True
            else:
                 raise Exception
        except:
            print("Please enter a valid choice :")

    selection = False

    while selection == False:

        try:
            opponent = input("Would you like to play against a computer or a human (type 'c' or 'h'): ")
            if opponent == 'c' or opponent == 'h':
                selection = True
            else:
                raise Exception
        except:
             print("Please enter a valid response: ")

    # player 2 becomes whatever player 1 didn't select
    choice2 = None
    if choice == 'x':
        choice2 = '0'
    else:
        choice2 = 'x'

    if opponent == 'h':
        name2 = input("name: ")
        player2 = {
            "name": name2,
            "choice": choice2
        }

    # human players select a name
    elif opponent == 'c':
        name2 = 'computer'
        player2 = {
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

        # the 3x3 board is rendered after each round
        render(BOARD)
        game_round += 1
        print(f"Round {game_round}!")

        # each player will select their action then the game will check if either player has won
        get_action(player)
        if check_win(player):
            victory_message(player)
            my_file = open('score_log.txt', 'a')
            my_file.write(f"{player['name']} beat {player2['name']} in TicTacToe in {game_round} rounds!" + "\n")
            my_file.close()

            game_end = False

            while game_end == False:

                # if a player selects to play again the rounds are reset and the game is launched again
                # otherwise the game returns to the main menu
                play_again = input("Would you like to play again (Please enter 'yes' or 'no') : ")

                if play_again == 'yes':
                        game_round = 0
                        play_t3()
                elif play_again == 'no':
                        game_over = True
                        game_end = True
                else:
                        print("Please enter a valid response: ")
        if check_win(player) != True:
            get_action(player2)
            if check_win(player2):
                victory_message(player2)

                # each game will be recorded in the master game log
                my_file = open('score_log.txt', 'a')
                my_file.write(f"{player2['name']} beat {player['name']} in TicTacToe in {game_round} rounds!" + "\n")
                my_file.close()


                game_end = False

                while game_end == False:

                    play_again = input("Would you like to play again (Please enter 'yes' or 'no') : ")

                    if play_again == 'yes':
                            game_round = 0
                            play_t3()
                    elif play_again == 'no':
                        game_over = True
                    else:
                        print("Please enter a valid response: ")

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
