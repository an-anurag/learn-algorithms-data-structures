"""
Find all the permutation of given string. ignore duplicates
eg - abc --> abc, acb, bac, bca, cba, cab
"""


def permute(my_string):

    final_result = []

    temp_permute = []
    # base case
    i = 0

    while i < len(my_string):
        ch = my_string[i]
        combination = my_string[:i] + my_string[i + 1:]
        temp_permute.append(combination)
        final_result.append(ch + combination)
        i += 1

    # for ch in my_string:
    #     for item in temp_permute:
    #         final_result.append(ch + item)

    return final_result


print(permute("ABC"))


