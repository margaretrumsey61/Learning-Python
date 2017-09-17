# Ask the user for their name and the year they were born.
try:
    date_of_birth = int(input("Hey, Player, what is your date of birth \n"))

# Handling ValueError if user enters not a number
except ValueError:
    print("No-no-no, years only!")
else:
    # Calculating current age
    current_age = 2017 - date_of_birth

    # Handle age <= 25
    if current_age <= 25:
        print("You will turn 25 in {}".format(date_of_birth + 25))
        print("You will turn 55 in {}".format(date_of_birth + 55))
        print("You will turn 75 in {}".format(date_of_birth + 75))
        print("You will turn 100 in {}".format(date_of_birth + 100))

    # Handle age <=50
    elif current_age <= 50:
        print("You will turn 55 in {}".format(date_of_birth + 55))
        print("You will turn 75 in {}".format(date_of_birth + 75))
        print("You will turn 100 in {}".format(date_of_birth + 100))

    # Handle age <=75
    elif current_age <= 75:
        print("You will turn 75 in {}".format(date_of_birth + 75))
        print("You will turn 100 in {}".format(date_of_birth + 100))

    # Handle age <=100
    elif current_age <= 100:
        print("You will turn 100 in {}".format(date_of_birth + 100))
