"""

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""


def target_sum(arr, k):

    for i in range(len(arr) - 1):
        current_num = arr[i]
        for j in range(i + 1, len(arr)):
            current_sum = current_num + arr[j]
            if current_sum == k:
                return True


my_list = [10, 15, 3, 7]
k = 17

print(target_sum(my_list, k))

