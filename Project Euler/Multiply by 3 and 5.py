def multiply_by_3_and_5(number: int) -> int:
    """Solution for Project Euler Problem 1"""
    total = 0
    for index in [0, number + 1]:
        if index % 3 == 0 and index % 5 == 0:
            continue
        if index % 3 == 0:
            total = total + index
        if index % 5 == 0:
            total = total + index
    return total


user_input = int(input("Enter natural number below 1000 \n"))
print(multiply_by_3_and_5(user_input))
