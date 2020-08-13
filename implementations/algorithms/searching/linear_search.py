"""
Implement linear/sequential search
"""


# array is ordered

def unorder_linear_search(arr, ele):
    pos = 0
    found = False

    while pos < len(arr) and not found:

        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found


a = [2, 5, 12, 43, 65, 78, 23, 8]
print(unorder_linear_search(a, 3))


# array is ordered

def order_linear_search(arr, ele):
    pos = 0
    found = False
    stopped = False

    # edge case
    if arr[0] > ele:
        return False

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


a = [2, 5, 12, 43, 65, 78]
print(order_linear_search(a, 43))