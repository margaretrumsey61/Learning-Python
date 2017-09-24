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


def add_to_list(item):
    clear_screen()
    # Add new items to the list
    try:
        position = int(input("Where (position) add this item: "))
    except ValueError:
        shopping_list.append(item)
    else:
        shopping_list.insert(position - 1, item)
        print(f"Item '{item}' added at {position}."
              f"Now list have {len(shopping_list)} items")


def exit_program():
    exit_sign = input("Type any key for exit: ")
    if exit_sign:
        sys.exit()


# Clearing all off from the list
def clear_list():
    del shopping_list[:]


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
        exit_program()

    # Process "HELP" request
    elif new_item.lower() == "help":
        show_help()
        continue

    # Process "SHOW" request
    elif new_item.lower() == "show":
        show_list()
        continue

    # Process "CLEAR" request
    elif new_item.lower() == "clear":
        clear_list()
        continue

    add_to_list(new_item)
