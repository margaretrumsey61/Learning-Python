# Function to show help for user
def show_help():
    print("Type DONE to finish")
    print("Type SHOW to show current list")
    print("Type CLEAR to clear whole list")
    print("Type HELP to display help")


# Printing out all items on the list
def show_list():
    print("Here is the full list:")
    for product in shopping_list:
        print(product)


def add_to_list():
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
    if new_item == "DONE":
        break

    # Process "HELP" request
    elif new_item == "HELP":
        show_help()
        continue

    # Process "SHOW" request
    elif new_item == "SHOW":
        show_list()
        continue

    add_to_list()
