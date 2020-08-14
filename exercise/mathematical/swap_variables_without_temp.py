
# method 1

x = 10
y = 5

# Code to swap 'x' and 'y'

# x now becomes 15
x = x + y

# y becomes 10
y = x - y

# x becomes 5
x = x - y
print("After Swapping: x =", x, " y =", y)


# method 2

# Python3 program to
# swap two numbers
# without using
# temporary variable
x = 10
y = 5

# code to swap
# 'x' and 'y'

# x now becomes 50
x = x * y

# y becomes 10
y = x // y

# x becomes 5
x = x // y

print("After Swapping: x =",
      x, " y =", y)

# method 3 - bitwise XOR

# Python 3 code to swap using XOR

x = 10
y = 5

# Code to swap 'x' and 'y'
x = x ^ y  # x now becomes 15 (1111)
y = x ^ y  # y becomes 10 (1010)
x = x ^ y  # x becomes 5 (0101)

print("After Swapping: x = ", x, " y =", y)
