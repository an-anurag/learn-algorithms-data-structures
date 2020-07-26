"""
Multiply all numbers upto nth
"""


def get_mul(nth_num):

    if nth_num == 0:
        return nth_num

    if nth_num == 1:
        return nth_num

    return nth_num * get_mul(nth_num - 1)


print(get_mul(6))
