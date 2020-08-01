"""
sum_of_digits in given number
"""


def sum_of_digits(number: int):

    # base case
    if len(str(number)) == 1:
        return number
    return sum_of_digits(number // 10) + number % 10


print(sum_of_digits(4525))




