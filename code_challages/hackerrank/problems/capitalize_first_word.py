"""
Capitalize first word in given string
"""


def solve(s):
    result = ""

    result += s[0].upper()
    for i in range(1, len(s)):
        # check that there is space before character
        if s[i - 1] == ' ':
            result += s[i].upper()
        else:
            result += s[i]

    return result


print(solve("anuarg gundappa pandit"))