my_arr = [-2, -3, 4, -1, -2, 1, 5, -3]


def kadanes_algo(arr):

    if not len(arr) > 0:
        return False

    i = 1
    max_sum = current_sum = arr[0]

    while i < len(my_arr):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(max_sum, current_sum)

        # this also works
        # if current_sum > max_sum:
        #     max_sum = current_sum

        i += 1
    print(max_sum)


kadanes_algo(my_arr)


