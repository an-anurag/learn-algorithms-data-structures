"""
Input 2 strings , 'abcdefgh' and 'wxyz', Output shud be 'awbxcydzefgh'

"""


def string_merger(s1, s2):

    s1_lt = len(s1)
    s2_lt = len(s2)
    result = ""

    if s2_lt < s1_lt:
        i = 0
        while i < s2_lt:
            result += s1[i] + s2[i]
            i += 1
        result += 1

    print(result)

# string_merger('abcdefgh', 'wxyz')


def fizzBuzz(n):
    # Write your code here
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and not i % 5 == 0:
            print("Fizz")
        elif i % 5 == 0 and not i % 3 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(15)