"""
Find common elements in two sorted array
"""

# Approach 1 with linear search
arr1 = [2, 3, 5, 10, 11, 12]
arr2 = [2, 4, 6, 8, 10, 12]

common_arr = []

for i in arr1:
    for j in arr2:
        if i == j:
            common_arr.append(i)

print(common_arr)


# Approach 2 with binary search

arr1 = [2, 3, 5, 10, 11, 12]
arr2 = [2, 4, 6, 8, 10, 12]

common_arr = []


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


for i in arr1:
    res = BinarySearch(arr2, i)
    if res != -1:
        common_arr.append(i)

print(common_arr)