"""
Transpose a given matrix
"""


mat = [
    [13, 53, 82, 92, 7, 40, 12, 96],
    [55, 91, 15, 40, 77, 57, 47, 1],
    [15, 7, 5, 13, 10, 19, 11, 2],
    [8, 0, 4, 5, 4, 9, 7, 3],
    [99, 99, 35, 14, 18, 47, 14, 42],
]

row = len(mat)
col = len(mat[0])

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

# approach 2: with list comprehension

print()
Y = [[mat[j][i] for j in range(row)] for i in range(col)]

for i in Y:
    r = " ".join(list(map(lambda x: str(x), i)))
    print(r)
