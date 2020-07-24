"""
Is second array rotated version of first?
"""


arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [5, 6, 7, 8, 1, 2, 3, 4]


def is_rotation(arr1, arr2):
    arr1_first = arr1[0]
    arr2_first = None

    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr2)):
        if arr2[i] == arr1_first:
            arr2_first = i

    if arr2_first is None:
        return False

    i = 0
    j = arr2_first
    while i < len(arr1):
        if not arr1[i] == arr2[j]:
            return False
        if j == len(arr2) - 1:
            j = -1
        i += 1
        j += 1

    return True


print(is_rotation(arr1, arr2))