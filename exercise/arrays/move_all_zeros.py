
#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
#the non-zero elements.


def move_zeros(arr):

    for i in range(len(arr)):
        current = arr[i]
        if current == 0:
            temp = current
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            arr[len(arr) - 1] = temp

    return arr


a = [1, 4, 0, 0, 6, 0, 8, 0, 9]
print(move_zeros(a))