"""
A string called balamced when every letter occurring in the string. appears both in upper and lowercase.
eg: the 'CATattac' is balanced('a', 'c', and 't' occur in both cases), but 'Madam' is not ('d' and 'a' appear only in low)
Note that number of occurrences does not matter.
if string 'S' do not have balanced fragments, the function should return -1
"""


s = 'azABaabza'
s2 = 'TacoCat'
s3 = 'AcZCbaBz'


def check_balance(S):

    start = 0
    for i in range(len(S)):
        ch = S[i]

        for j in range(i + 1, len(S)):
            this_char = S[j]
            if ch.lower() == this_char.lower():
                if S[j].isupper():
                    start = j
                elif S[j].lower():
                    pass

        print('---------------------')

    return start


print(check_balance(s2))


