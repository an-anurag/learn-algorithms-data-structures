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


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# uncomment to take input from the user
# num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


n = 7
mul = 1
i = 1
while i <= n:
    mul *= i
    i += 1
print(mul)


def f(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return f(num - 1) * num

print(f(7))
