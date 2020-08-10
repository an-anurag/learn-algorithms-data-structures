"""
Find all the permutation of given string. ignore duplicates
eg - abc --> abc, acb, bac, bca, cba, cab
"""


def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i + 1:]):
                # Add it to output
                out += [let + perm]

    return out


print(permute('ABC'))