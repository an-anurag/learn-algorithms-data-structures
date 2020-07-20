# Recursive Python program to count
# number of digits in a number

def countDigit(n):
    if n == 0:
        return 0
    return 1 + countDigit(n // 10)


# Driver Code
n = 345289467
print("Number of digits : % d" % (countDigit(n)))




# Iterative Python program to count
# number of digits in a number

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


# Driver Code
n = 345289467
print("Number of digits : % d" % (countDigit(n)))




# Log based Python program to count number of
# digits in a number

# function to import ceil and log
import math


def countDigit(n):
    return math.floor(math.log(n, 10) + 1)


# Driver Code
n = 345289467
print("Number of digits : % d" % (countDigit(n)))


# by converting int to str
# Python3 implementation of the approach
def count_digits(n):
    n = str(n)
    return len(n)


# Driver code
n = 456533457776
print(count_digits(n))