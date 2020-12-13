"""
eg: for first_duplicate(a) where a = [2, 3, 3, 1, 5, 2] the output should be 3.
There are 2 duplicated number 2 and 3. the second occurrence of 3 has a smaller index than second occurrence of 2 does.
so the answer is 3. for first_duplicate(a) where a = [2, 4, 3, 5, 1], the output should be -1
"""


def first_duplicate(arr):
    seen = []
    dup = []
    for i in range(len(arr)):
        ele = arr[i]
        if ele not in seen:
            seen.append(ele)
        else:
            dup.append(ele)

    if not dup:
        return -1
    else:
        return dup[0]


a = [2, 3, 3, 1, 5, 2]
a = [2, 4, 3, 5, 1]
print(first_duplicate(a))

