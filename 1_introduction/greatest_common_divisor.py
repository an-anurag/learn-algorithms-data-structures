# The best-known algorithm for finding a greatest common divisor is Euclid’s Algorithm


def gcd(m, n):
    """
    Euclid’s Algorithm states that the greatest common divisor of two integers m and n is n if n divides m evenly.
    However, if n does not divide m evenly, then the answer is the greatest common divisor of n and the
    remainder of m divided by  n
    :return:
    """

    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


print(gcd(8, 6))


# recursive version

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(8, 6))
