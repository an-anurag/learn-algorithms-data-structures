"""
Fibonacci series
"""


def fib(nth_num):

    if nth_num == 0:
        return nth_num

    if nth_num == 1:
        return nth_num

    print(fib(nth_num) - 1)
    return fib(nth_num - 2) + fib(nth_num - 1)

print(fib(3))

for i in range(10):
    num = fib(i)
    print(num, end="")