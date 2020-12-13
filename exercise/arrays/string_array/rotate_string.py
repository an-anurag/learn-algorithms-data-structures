"""
Rotate the string by given direction
"""


def rotate_string(s, direction, step):

    if direction == 'right':

        if step == 0:
            return s

        counter = 1
        string = None
        while counter <= step:
            string = s[-counter:] + s[:-counter]
            counter += 1
        return string


print(rotate_string("ANURAG", 'right', 3))

