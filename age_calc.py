# Step 1
# Ask the user for their name and the year they were born.
try:
    date_of_birth = int(input("Hey, Player, what is your date of birth \n"))
except ValueError:
    print("No-no-no, years only!")
else:
    current_age = 2017 - date_of_birth
    if current_age <= 25:
        print("You will turn 25 in {}".format(date_of_birth + 25))
        print("You will turn 55 in {}".format(date_of_birth + 55))
        print("You will turn 75 in {}".format(date_of_birth + 75))
        print("You will turn 100 in {}".format(date_of_birth + 100))
    elif current_age <= 50:
        print("You will turn 55 in {}".format(date_of_birth + 55))
        print("You will turn 75 in {}".format(date_of_birth + 75))
        print("You will turn 100 in {}".format(date_of_birth + 100))
    elif current_age <= 75:
        print("You will turn 75 in {}".format(date_of_birth + 75))
        print("You will turn 100 in {}".format(date_of_birth + 100))
    elif current_age <= 100:
        print("You will turn 100 in {}".format(date_of_birth + 100))
# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.

# Step 3
# If they're already past any of these ages, skip them.
