"""
Reverse a given string with recursion
"""


def reverse_string(my_string):
    if len(my_string) == 0:
        return ""
    return reverse_string(my_string[1:]) + my_string[0]


print(reverse_string("Anurag"))