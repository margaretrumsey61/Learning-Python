import random


def show_help():
    print("Hi, my name is Mr. Robot!\n"
          "I want you to play my game.\n"
          "You have 5 attempts to guess what number i picked for you (from 1 to 10 \n")


def new_game():
    show_help()
    secret_number = random.randint(1, 10)
    guesses = []
    while len(guesses) < 5:
        players_guess = input("Please, guess secret number from 1 to 10: ")
        try:
            players_guess = int(players_guess)
        except ValueError:
            print("I need number, man! Number! '{}' is not the number".format(players_guess))
        else:
            if players_guess == secret_number:
                print("Hooray, you guessed right!")
                break
            else:
                print("Not, my secret number is not {}".format(players_guess))

            guesses.append(players_guess)
    else:
        print("You ran out of guesses. {} was the right answer".format(secret_number))


new_game()
