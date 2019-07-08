import math

res = math.sqrt(45)
print(res)

"""
“Newton’s Method of approximating square roots
"""

# equation
# new_guess = 1/2 * (old_guess + n/old_guess)


def squareroot(num):
    root = 1/2 * num   # initial guess will be 1/2 of num
    for i in range(10):
        root = (1/2) * (root + (num / root))
    return root


ans = squareroot(25)
print(ans)