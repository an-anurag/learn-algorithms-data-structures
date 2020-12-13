"""
Input 1 string , count no. of duplicates in that string.  'abcadfhberc',
there are 3 duplicate alphabets so output : no. of duplicates = 3

"""


def check_duplicates(string):
    letters = [x for x in string]
    seen = []
    dup = []
    for ch in letters:
        if ch not in seen:
            seen.append(ch)
        else:
            dup.append(ch)
    return dup, len(dup)


s1 = 'abcadfhberc'
print(check_duplicates(s1))