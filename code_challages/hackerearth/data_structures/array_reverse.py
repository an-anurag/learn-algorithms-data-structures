'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

size = int(input())
arr = []
for i in range(size):
    arr.append(int(input()))

counter = len(arr) - 1
while counter >= 0:
    print(arr[counter])
    counter -= 1

