import random


def generate_secret_number():
    return random.randint(1, 10)


def show_help():
    print("Hi, my name is Mr. Robot!\n"
          "I want you to play my game.\n"
          "You have 5 attempts to guess what number i picked for you (from 1 to 10 \n")


def check_for_delta():
    if players_guess - secret_number >= 3 or players_guess - secret_number <= - 3:
        return True


secret_number = generate_secret_number()

show_help()

while True:
    players_guess = int(input("Please, guess secret number from 1 to 10: "))
    if players_guess == secret_number:
        print("Hoorah, you guessed right!")
        break
    elif check_for_delta():
        print("Way too far away!")
    else:
        print("Not, my secret number is not {}".format(players_guess))
