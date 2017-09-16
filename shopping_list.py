# Function to show help for user
def show_help():
    print("Type DONE to finish")
    print("Type SHOW to show current list")
    print("Type HELP to display help")


# Printing out all items on the list
def show_list():
    print("Here is the full list:")
    for item in shopping_list:
        print(item)


def add_to_list():
    # Add new items to the list
    shopping_list.append(new_item)
    print("Item '{}' added. Now list have {} items".format(new_item, len(shopping_list)))


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

    add_to_list()
