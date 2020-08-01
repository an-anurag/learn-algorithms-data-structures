
# Given an array containing None values fill in the None values with most recent
# non None value in the array


def fill_none(arr):

    for i in range(1, len(arr)):
        if arr[i] is None:
            arr[i] = arr[i - 1]

    return arr


a = [1, 4, None, 2, None, 0, 9, None]
print(fill_none(a))
