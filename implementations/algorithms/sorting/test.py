def quick_sort(arr):

    def _quick_sort(arr, low, high):

        if low < high:

            split_index = partition(arr, low, high)
            _quick_sort(arr, low, split_index)
            _quick_sort(arr, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)


def partition(arr, first, last):

    pivot = arr[first]
    leftmark = first + 1
    rightmark = last

    while leftmark <= pivot:
        leftmark += 1

    while rightmark >= pivot:
        rightmark += 1

    if leftmark > rightmark:
        leftmark, pivot = pivot, leftmark

    return rightmark


print(quick_sort([10, 2, 45, 9, 34, 6]))