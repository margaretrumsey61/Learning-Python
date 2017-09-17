import random


def generate_secret_number():
    return random.randint(1, 10)


secret_number = generate_secret_number()

while True:
    players_guess = int(input("Please, guess secret number from 1 to 10: "))
    if players_guess == secret_number:
        print("Hoorah, you guessed right!")
        break
    else:
        print("Not, my secret number is not {}".format(players_guess))
