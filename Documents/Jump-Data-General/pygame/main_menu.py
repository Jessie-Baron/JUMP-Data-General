from rps import play_rps
from tictactoe import play_t3
from guess_the_number import play_gtn
from chess import play_chess
'''
This is the main file. Run this file to select and play a particular
game.
'''

game_live = True
while game_live == True:

    print(
        """
        Your game library:
        1: Tic-Tac-Toe
        2: Guess the Number!
        3: Rock, Paper, Scissors
        4: Chess
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
        play_gtn()
        game_choice = None

    elif game_choice == '3':
        play_rps()

    elif game_choice == '4':
        play_chess()

    elif game_choice == 'exit':
        game_choice = False
        break
