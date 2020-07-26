"""
Add numbers upto n
"""


def get_sum(nth_digit):

    if nth_digit == 1:
        return nth_digit
    val = nth_digit + get_sum(nth_digit - 1)
    print(val)
    return val


get_sum(5)