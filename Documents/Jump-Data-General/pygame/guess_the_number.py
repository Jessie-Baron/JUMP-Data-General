import random

# This is passed if the player guesses the number
def victory_message(name, round):
    print(f"{name} guessed the number in {round} guesses")

# every round a hint will be given. Some aren't very helpful lol
def give_hint(num, guess):
    if abs(num - guess) <= 5:
        print('You are REALLY close to the number')
    elif abs(num - guess) <= 10:
        print('You are close to the number')

    hints = [
        f'The number is greater than {num - 10}',
        f"The number is less than {num + 25}",
        f"The number is in between {num - 35} and {num + 25}",
        f"The number is 12! ......jk",
        f"The number isn't {guess}"
    ]

    hint = random.randint(0, 4)

    # a hint will be chosen at random by looping through the indexes of the hints list
    # and looking for the matching number chosen at random
    for i in hints:
        if hints.index(i) == (hint):
            print(i)

def play_gtn():
    round = 1
    print("Guess the Number is starting...")

    game_over = False

    # same loop format as my other games
    while not game_over:

        if round == 1:
            num = random.randint(1, 100)

        if round == 1:
            name = input("name: ")

        guess = input("Guess a number between 1 and 100: ")

        if int(guess) == num:
            victory_message(name, round)

            message = f"{name} guessed the number in {round} guesses in GTN!"
            my_file = open('score_log.txt', 'a')
            my_file.write(message + "\n")
            my_file.close()

            game_end = False

            while game_end == False:

                # if a player selects to play again the rounds are reset and the game is launched again
                # otherwise the game returns to the main menu
                play_again = input("Would you like to play again (Please enter 'yes' or 'no') : ")

                if play_again == 'yes':
                        round = 1
                        play_gtn()
                elif play_again == 'no':
                        game_over = True
                        game_end = True
                else:
                        print("Please enter a valid response: ")

        else:
            print(f"Wrong! You have {5 - round} guesses left. Here is a hint...")
            give_hint(num, int(guess))

        round += 1
        if 5 - round == 0:
            print("You lose!")
            message = f"{name} lost to the computer in GTN!"
            my_file = open('score_log.txt', 'a')
            my_file.write(message + "\n")
            my_file.close()
            game_end = False

            while game_end == False:

                # if a player selects to play again the rounds are reset and the game is launched again
                # otherwise the game returns to the main menu
                play_again = input("Would you like to play again (Please enter 'yes' or 'no') : ")

                if play_again == 'yes':
                        round = 1
                        play_gtn()
                elif play_again == 'no':
                        game_over = True
                        game_end = True
                else:
                        print("Please enter a valid response: ")
