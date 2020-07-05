def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr, element):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if element == arr[mid]:
            return mid
        else:
            if element < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1


print(binary_search(sorted([2, 7, 89, 34, 9, 78, 23, 12]), 23))