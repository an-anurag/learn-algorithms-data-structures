"""
counts digits in number
"""


def total_sum(number: int):

    # edge_case
    if number == 0:
        return number
    return 1 + total_sum(number // 10)


print(total_sum(997654))