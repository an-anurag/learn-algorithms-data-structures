"""Reversing a list"""

name_list = "A N I K E T".split(' ')
length = len(name_list)
i = length - 1

while i >= 0:
    ch = name_list[i]
    print(ch)
    i -= 1
