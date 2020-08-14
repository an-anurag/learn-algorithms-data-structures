
def rotate_string(s, direction, step):

    if direction == 'right':
        first = s[:len(s) - step]
        second = s[len(s) - step:]
        return second + first
    else:
        first = s[:step]
        second = s[step:]
        return second + first


print(rotate_string("ANURAG", 'left', 0))
