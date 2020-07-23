"""
Find whether string contains all unique characters
"""

st = "abcdef"  # unique
st2 = "aabcedeef"  # non-unique


def check_unique(arr):
    uni_set = set(arr)
    if len(uni_set) != len(arr):
        return False

    for c in arr:
        if c not in uni_set:
            return False
        else:
            return True


print(check_unique(st))