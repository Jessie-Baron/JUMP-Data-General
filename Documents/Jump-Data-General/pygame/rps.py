import random

def play_rps():
    # start a while loop with variables to keep track of score
    player_one_score = 0
    player_two_score = 0
    ties = 0
    round = 1

    game_alive = True
    while game_alive == True:

        if round == 1:
            name = input("name: ")

        selection = False
        while selection == False and round == 1:

            try:
                opponent = input(
                    "Would you like to play against a computer or a human (type 'c' or 'h'): ")
                if opponent == 'c' or opponent == 'h':
                    selection = True
                else:
                    raise Exception
            except:
                print("Please enter a valid response: ")

        if opponent == 'h' and round == 1:
            name2 = input("name: ")

        # human players select a name
        elif opponent == 'c':
            name2 = 'computer'

        move_completed = False

        while move_completed == False:
            try:
                # ask player 1 for input
                print(f"round {round}!")
                player_one = input("Rock, Paper, or Scissors (type r, p or s): ")

                # ask player 2 for input
                if name2 == 'computer':
                    player_two = random.sample(['r', 'p', 's'], 1)
                else:
                    player_two = input("Rock, Paper, or Scissors (type r, p or s): ")
                move_completed = True
            except:
                 print("invalid response. Try again: ")

        # use process of elimination to build logic for each case
        round += 1
        if player_one == player_two:
            print("it's a tie!")
            ties += 1
        elif player_one == "r":
            if player_two == "p":
                print("player two wins!")
                player_two_score += 1
            else:
                print("player one wins!")
                player_one_score += 1
        elif player_one == "p":
            if player_two == "r":
                print("player one wins!")
                player_one_score += 1
            else:
                print("player two wins!")
                player_two_score += 1
        elif player_one == "s":
            if player_two == "p":
                print("player one wins!")
                player_one_score += 1
            else:
                print("player two wins!")
                player_two_score += 1

        message = None

        if player_one_score >= 3:
            message = f"{name} beat {name2} {player_one_score} to {player_two_score} with {ties} ties in RPS!"
            my_file = open('score_log.txt', 'a')
            my_file.write(message + "\n")
            my_file.close()

            print(message)

        elif player_two_score >= 3:
            message = f"{name2} beat {name} {player_two_score} to {player_one_score} with {ties} ties in RPS!"
            my_file = open("score_log.txt", '+a')
            my_file.write(message)
            my_file.close()

            print(message)

        elif ties >= 3:
            message = f"{name} and {name2} tied with a score of {player_one_score} to {player_two_score} with {ties} ties in RPS!"

            my_file = open("score_log.txt", '+a')
            my_file.write(message)
            my_file.close()

            print(message)


        if message != None:
                game_end = False

                while game_end == False:

                    # if a player selects to play again the rounds are reset and the game is launched again
                    # otherwise the game returns to the main menu
                    play_again = input("Would you like to play again (Please enter 'yes' or 'no') : ")

                    if play_again == 'yes':
                            round = 0
                            player_one_score = 0
                            player_two_score = 0
                            ties = 0
                            message = None

                            play_rps()
                    elif play_again == 'no':
                            game_alive = False
                            game_end = True
                            break
                    else:
                            print("Please enter a valid response: ")
