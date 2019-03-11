"""
Adds the given two matrixes as input and prints the result matrix
"""

def get_matrix(r, c):
    print('enter matrix for data for {0} x {1}'.format(r, c))
    matrix = []

    for i in range(r):
        col = []
        for j in range(c):
            x = int(raw_input())
            col.append(x)
        matrix.append(col)

    #for row in matrix:
    #    for x in row:
    #        print x,
    #    print
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print x,
        print

print('enter row and col data for matrix sum')
r, c = int(raw_input('enter row count')), int(raw_input('enter col count'))

m1 = get_matrix(r, c)
m2 = get_matrix(r, c)

res = []
i = 0
while i < r:
    col = []
    c1_m1 = m1[i]
    c1_m2 = m2[i]
    j = 0
    while j < c:
        col.append(c1_m1[j] + c1_m2[j])
        j = j + 1
    res.append(col)
    i = i + 1

print_matrix(res)
