# Creating empty shopping list
shopping_list = []

# Print instructions for user
print("What should i pick from store?")
print("Type DONE to finish")

# Entering new items
while True:
    new_item = input("> ")  # Ask for new items

    if new_item == "DONE":
        break

    # Add new items to the list
    shopping_list.append(new_item)

# Printing out all items on the list
print("Here is the full list:")
for item in shopping_list:
    print(item)

