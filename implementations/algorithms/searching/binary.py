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


def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return True
        return -1


print(BinarySearch(sorted([2, 7, 89, 34, 9, 78, 23, 12]), 23))