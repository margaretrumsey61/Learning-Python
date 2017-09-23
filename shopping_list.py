import os
import sys


# Function to clear screen
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Function to show help for user
def show_help():
    print("Type DONE to finish")
    print("Type SHOW to show current list")
    print("Type CLEAR to clear whole list")
    print("Type HELP to display this help")


# Printing out all items on the list
def show_list():
    clear_screen()
    print("Here is the full list:")
    for product in shopping_list:
        print(f"{shopping_list.index(product) + 1} {product}")


def add_to_list():
    clear_screen()
    # Add new items to the list
    shopping_list.append(new_item)
    print(f"Item '{new_item}' added. "
          f"Now list have {len(shopping_list)} items")


# Creating empty shopping list
shopping_list = []

# Show initial HELP message
show_help()

# Entering new items
while True:
    new_item = input("> ")  # Ask for new items

    # Process "DONE" request
    if new_item.lower() == "done":
        show_list()
        print("______________________")
        exit_sign = input("For exit type any key: ")
        if exit_sign:
            sys.exit()

    # Process "HELP" request
    elif new_item.lower() == "help":
        show_help()
        continue

    # Process "SHOW" request
    elif new_item.lower() == "show":
        show_list()
        continue

    add_to_list()
