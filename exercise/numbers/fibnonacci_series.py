# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

def fib_series2():
    # change this value for a different result
    nterms = 10

    # uncomment to take input from the user
    # nterms = int(input("How many terms? "))

    # first two terms
    n1 = 0
    n2 = 1
    count = 0

    # # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence upto", nterms, ":")
        while count < nterms:
            print(n1, end=' , ')
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


def fib_series(num):
    n1 = 0
    n2 = 1
    counter = 0
    while counter < num:
        if num < 0:
            return -1
        elif num == 1:
            return 0
        else:
            print(n1, end="")
            next_num = n1 + n2
            n1 = n2
            n2 = next_num
            counter += 1


# fib_series(5)


def fib_recur(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_recur(num - 1) + fib_recur(num - 2)

print(fib_recur(5))


print("--------------------------")
