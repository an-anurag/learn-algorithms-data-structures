"""
Find the element pair having sum equal to specified value
a = [1, 2, 3, 4, 2]
b = 4
find all pairs having sum = 4
O(n)
"""


def pair_sum(arr, num):
    seen = set()
    pairs = []
    for j in arr:
        no_to_find = num - j
        if no_to_find not in seen:
            seen.add(no_to_find)
        else:
            pairs.append((j, no_to_find))
    return pairs


print(pair_sum([1, 2, 3, 4, 2, 6, 3], 4))




