
# start a while loop with variables to keep track of score
player_one_score = 0
player_two_score = 0
ties = 0
while True:

    # ask player 1 for input
    player_one = input("Rock, Paper, or Scissors: ")

    # ask player 2 for input
    player_two = input("Rock, Paper, or Scissors: ")

    # use process of elimination to build logic for each case
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

    if player_one_score >= 3:
        print("player one wins!")
        break
    elif player_two_score >= 3:
        print("player two wins!")
        break
    elif player_one_score >= 3:
        print("its a tie!")
        break

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("player one:" + player_one_score, "player two" + player_two_score, "ties:" + ties)
        break
