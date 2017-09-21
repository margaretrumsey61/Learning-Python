import random


library = [
    "apple",
    "lemon",
    "watermelon",
    "strawberry",
    "pineapple",
    "blueberry",
    "orange",
    "banana",
    "coconut",
    "lime",
    "grapefruit"
    ]

while True:
    start = input("Press any key to start, press Q to end game now: ")
    if start.lower() == 'q':
        print("See ya!")
        break

    secret_word = random.choice(library)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end="")
            else:
                print("_", end="")
        print("\n")
        print(f"Strikes: {len(bad_guesses)} / 7")
        print("\n")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess 1 letter at the time!")
            continue
        elif guess in good_guesses or guess in bad_guesses:
            print("You already guess that letter!")
            continue
        elif not guess.isalpha():
            print("You could guess only letters!")
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print(f"You win! {secret_word} is my right answer")
                break
        else:
            bad_guesses.append(guess)
    else:
        print(f"You didn't guess it! {secret_word} was my secret word!")
