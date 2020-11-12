"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?

"""


def target_mul(arr):

    result = []
    # iterate over array
    for i, item in enumerate(arr):
        # creating array without current element in it
        other_els = arr[:i] + arr[i + 1:]
        mul = 1
        # iterating over new array
        for j in other_els:
            # multiply each element
            mul *= j
        # add to final result
        result.append(mul)
    return result


print(target_mul([3, 2, 1]))