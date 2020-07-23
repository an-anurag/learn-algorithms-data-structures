""" Check whether string_array is anagram or not"""


def anagram_check1(s1, s2):
    s1 = s1.casefold()
    s2 = s2.casefold()

    char_set = set()

    for c in s1:
        if c != " ":
            char_set.add(c)

    for c in s2:
        if c != " ":
            if c not in char_set:
                return False
    return True


s1 = "Astronomer"
s2 = "Moon starer"
# listen, silent, Astronomer Moon starer

ans = anagram_check1(s1, s2)
print(ans)


def anagram_check2(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for c in s1:
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] += 1

    for c in s2:
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] -= 1

    for k in count.values():
        if k != 0:
            return False
        return True


s1 = "Clint eastwood"
s2 = "Old west action"
print(anagram_check2(s1, s2))
