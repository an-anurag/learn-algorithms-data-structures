"""
Find missing element from first arr, given second array
"""

arr1 = [1, 2, 4, 6, 8, 0]
arr2 = [1, 4, 8, 6, 0]

# method 1 by diff

# missing = sum(arr1) - sum(arr2)
# print(missing)


# method 2 by sorting two arrays

def finder(ent1, ent2):
    ent1.sort()
    ent2.sort()
    for i, j in zip(ent1, ent2):
        if i != j:
            return i


print(finder(arr1, arr2))


#  method 3 with dicts/hash storing counter
