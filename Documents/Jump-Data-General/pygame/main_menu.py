from rps import play_rps
from tictactoe import play_t3
'''
This is the main file. Run this file to select and play a particular
game.
'''

game_library = {
    "Rock, Paper, Scissors",
    "Number Guess Game",
    "Tic Tac Toe",
    "Connect 4",
    "Chess"
}

game_live = True
while game_live == True:

    print(
        """
        Your game library:
        1: Tic-Tac-Toe
        2: Connect Four
        3: Checkers
        4: Rock, Paper, Scissors
        5. Chess
        """
        )

    game_choice = input(
        """
        What game would you like to play?
        Input the game ID, or type 'exit' to exit.
        """
        )

    if game_choice == '1':
        play_t3()
        game_choice = None

    elif game_choice == '2':
        play_c4()
        game_choice = None

    elif game_choice == '3':
        play_checkers()

    elif game_choice == '4':
        play_rps()

    elif game_choice == 'exit':
        game_choice = False
        break
