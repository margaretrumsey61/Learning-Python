import random

# Setup library of words
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

# Start new game
while True:
    # Ask about start new game
    start = input("Press any key to start, press Q to end game now: ")

    # If player typed 'q', we exit game
    if start.lower() == 'q':
        print("See ya!")
        break

    # Initiate new variables
    secret_word = random.choice(library)
    bad_guesses = []
    good_guesses = []

    # We continue until we find all letters or less 7 strikes
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):

        # Printing out current status of secret word with _
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end="")
            else:
                print("_", end="")
        print("\n")

        # Printing out number of strices
        print(f"Strikes: {len(bad_guesses)} / 7")
        print("\n")

        # Request input from player
        guess = input("Guess a letter: ").lower()

        # Wrong input handling, 1) 1 letter at the time
        if len(guess) != 1:
            print("You can only guess 1 letter at the time!")
            continue

        # Checking if we already guess that
        elif guess in good_guesses or guess in bad_guesses:
            print("You already guess that letter!")
            continue

        # Checking if we input letters, not numbers
        elif not guess.isalpha():
            print("You could guess only letters!")
            continue

        # Comparing guess vs secret word
        if guess in secret_word:

            # If yes - add letter to good guesses
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print(f"You win! {secret_word} is my right answer")
                break

        # if not - add letter to bad guesses
        else:
            bad_guesses.append(guess)

    # Print unfortunate result
    else:
        print(f"You didn't guess it! {secret_word} was my secret word!")
