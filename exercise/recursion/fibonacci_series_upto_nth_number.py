"""
Fibonacci series
"""

# approach 1: with recursion


def fib(nth_num):

    if nth_num == 0:
        return nth_num

    if nth_num == 1:
        return nth_num

    return fib(nth_num - 2) + fib(nth_num - 1)

print(fib(10))

for i in range(10):
    num = fib(i)
    print(num, end="|")
print()


# approach 2: with iteration
print("---------------------------")


def fib_iter(nth_num):
    a, b = 0, 1
    for i in range(nth_num):
        # print(a, end="|")
        a, b = b, a + b

    # for series only
    # print(a, end="|")
    # for nth number only
    print(a)


fib_iter(10)


# approach 3: with dynamic programming
print("------------------------------------")
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):

    # base case
    if n == 0 or n == 1:
        return n

    # check cache
    if cache[n] is not None:
        return cache[n]

    # keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


print(fib_dyn(10))

for i in range(10):
    print(fib_dyn(i), end='|')