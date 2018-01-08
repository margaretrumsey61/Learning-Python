def multiply_by_3_and_5(number: int) -> int:
    """Solution for Project Euler Problem 1
    Sum of all numbers below N which multiply by 3 or 5 could be calculated as:
    sum(by 3) + sum(by 5) - sum(by 15) cause every number which divides by 15 is already counted
    as multiplied by 3 or by 5

    Every sum is arithmetic progression:
    S(n) = ((2*a1 + d(n-1)) * n )/2
    S(n) - sum of all numbers
    a1 - first element of progression (3, 5 or 15)
    d - delta (3, 5 or 15)
    n - index of last element
    """


user_input = int(input("Enter natural number below 1000 \n"))
print(multiply_by_3_and_5(user_input))
