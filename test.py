'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
row, col = [int(x) for x in input().split()]

mat = [[int(x) for x in input().split()] for j in range(row)][:row]

# approach 1 by creating another array with rectangular matrix

# create result matrix to store values
Y = [[0 for x in range(row)] for y in range(col)]

# iterate over row
for i in range(row):

    # iterate over col
    for j in range(col):
        # transpose
        Y[j][i] = mat[i][j]

# display
for i in Y:
    r = " ".join(list(map(lambda x: str(x), i)))
    print(r)

