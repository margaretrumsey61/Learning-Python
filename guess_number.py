# Import standard library for random numbers
import random


# Define show_help function
def show_help():
    # Printing out introduction for the player
    print("Hi, my name is Mr. Robot!\n"
          "I want you to play my game.\n"
          "You have 5 attempts to guess what number I picked for you (from 1 to 10) \n")


# Define new_game function
def new_game():
    # Show help at the beginning
    show_help()

    # Randomize secret number
    secret_number = random.randint(1, 10)

    # Initiate empty list of guesses
    guesses = []

    # While we guess less than 5 times, loop ->
    while len(guesses) < 5:

        # Request Player's input
        players_guess = input("Please, guess secret number from 1 to 10: ")

        # Casting player input into integer
        try:
            players_guess = int(players_guess)

        # Exception handling (not number)
        except ValueError:
            print("I need number, man! Number! '{}' is not the number \n".format(players_guess))

        # main logic happens here =)
        else:

            # If player succeed - notify him about it
            if players_guess == secret_number:
                print("Hooray, you guessed right!")

                # Break loot to end game
                break

            # If player's guess > secret number - notify that
            elif players_guess > secret_number:
                print("Not, my secret number is less than {} \n".format(players_guess))

            # If player's guess is less - notify him
            else:
                print("Not, my secret number is higher than {} \n".format(players_guess))

            # Add 1 guess to the list
            guesses.append(players_guess)

    # If player is out of guesses (5) - notify with actual secret number
    else:
        print("You ran out of guesses. {} was the right answer \n".format(secret_number))

    # Ask player about new game with Y/n choose
    play_again = input("Do you want to play again? Y/n \n")

    # since we used Y (strong yes), any input except 'n' will be considered as 'Yes'
    if play_again != 'n':
        new_game()

    # Say goodbye if player decided to stop
    else:
        print("Bye!")


# Start of the script
new_game()

