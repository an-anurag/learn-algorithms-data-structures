def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]


# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)


def sel_sort(arr):
    for i in range(len(arr)):
        min_index = i
        # unsorted arr
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
sel_sort(random_list_of_nums)
print(random_list_of_nums)

