"""
Implement binary serach
"""


# iterative version
def binary_search(arr, ele):

    start = 0
    end = len(arr) - 1
    found = False

    while start <= end and not found:
        mid = (start + end) // 2
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return found


# res = binary_search([1, 2, 3, 4, 5, 6, 78, 85, 101, 123], 102)
# print(res)


# recursive version

def binary_search_recur(arr, ele):

    # base case to mark where to stop
    if len(arr) == 0:
        return False

    else:
        mid = len(arr) // 2

        if arr[mid] == ele:
            return True

        # recursive calls
        if ele < arr[mid]:
            return binary_search_recur(arr[: mid], ele)
        return binary_search_recur(arr[mid + 1:], ele)


print(binary_search_recur([1, 2, 3, 4, 5, 6, 78, 85, 101, 123], 8))
