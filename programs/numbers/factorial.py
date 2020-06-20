# recursive
def fact(num: int):
    if (num == 1) or (num == 0):
        return 1
    else:
        num * fact(num - 1)


# ternary operator
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
