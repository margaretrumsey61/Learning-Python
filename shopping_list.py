import os
import sys


# Function to clear screen
def clear_screen():
    # If our system is Widows, then we utilize command /cls
    if os.name == "nt":
        os.system("cls")
    # Else our system is MacOS or Unix, than command /clear
    else:
        os.system("clear")


# Function to show help for user
def show_help():
    print("Please, add everything for your shopping cart to the list!\n"
          "Type DONE to finish\n"
          "Type SHOW to show current list\n"
          "Type CLEAR to clear whole list\n"
          "Type DELETE to delete certain position\n"
          "Type HELP to display this help\n")


# Printing out all items on the list
def show_list():
    clear_screen()
    print("Here is the full list:")
    for product in shopping_list:
        print(f"{shopping_list.index(product) + 1} {product}")


def delete_from_list():
    clear_screen()
    try:
        delete_position = int(input("Position you would like to delete: "))
    except ValueError:
        print("Error! You need to type position!")
        delete_from_list()
    else:
        del shopping_list[delete_position - 1]


# Adding item to the list
def add_to_list(item):
    clear_screen()
    # Handing error on picking position where to put item
    try:
        position = int(input("Where (position) add this item: "))

    # Value Error - item will go to the end of the list
    except ValueError:
        shopping_list.append(item)

    # Else - we add item on requested index in our list
    else:
        shopping_list.insert(position - 1, item)
        print(f"Item '{item}' added at {position}."
              f"Now list have {len(shopping_list)} items")


# Exiting program properly
def exit_program():
    exit_sign = input("Type any key for exit: ")
    if exit_sign:
        sys.exit()


# Clearing all off from the list
def clear_list():
    shopping_list.clear()


# Creating empty shopping list
shopping_list = []

# Show initial HELP message
show_help()

# Entering new items
while True:
    new_item = input("What you would like to add? > ")  # Ask for new items

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

    # Process "DELETE" request
    elif new_item.lower() == "delete":
        delete_from_list()
        continue

    add_to_list(new_item)
