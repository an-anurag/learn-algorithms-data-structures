"""
You are given a string S of length N which encodes a non-negative number V in a bin form.
Two types of operations may be performed on it to modify its value

if V is odd, substract 1 from it
If V is even, divide it by 2
These operations are performed until the value of V becomes 0. returns the number of operations after which its value
become zero
"""


def operations(bin_str):

    num = int(bin_str, 2)

    steps = 0

    while not num <= 0:

        if num % 2 == 0:
            num = num // 2
            steps += 1

        else:
            num = num -1
            steps += 1

    return steps


print(operations('00011000'))
