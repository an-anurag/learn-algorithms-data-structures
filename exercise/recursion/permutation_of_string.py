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
        perm = my_string[i + 1:]
        perm2 = my_string[:i]
        temp_permute.append(perm)
        temp_permute.append(perm2)

        for item in temp_permute:
            final_result.append(ch + item)

        i += 1

    return final_result


print(permute("ABC"))


