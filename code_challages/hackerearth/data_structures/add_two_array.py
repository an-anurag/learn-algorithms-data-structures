'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
lt = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

index = 0
add_list = []

while lt > index:
    res = arr1[index] + arr2[index]
    add_list.append(res)
    index += 1

print(" ".join([str(x) for x in add_list]))