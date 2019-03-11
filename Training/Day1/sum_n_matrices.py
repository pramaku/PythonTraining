"""
Adds all the given input matricesand prints the resultant matrix
"""

count = int(raw_input('Enter number of matrices to be added'))

print('enter row and col data for matrix sum, this applies to all matrices')
r, c = int(raw_input('enter row count')), int(raw_input('enter col count'))

def get_matrix(r, c):
    print('enter matrix for data for {0} x {1}'.format(r, c))
    matrix = []

    for i in range(r):
        col = []
        for j in range(c):
            x = int(raw_input())
            col.append(x)
        matrix.append(col)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print x,
        print

def sum_matrix(m1, m2):
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
    return res

m_list = []
for x in range(count):
    m_list.append(get_matrix(r, c))

first_m = m_list[0]
total_sum = first_m[:]
i = 1
while i < len(m_list):
    total_sum = sum_matrix(total_sum, m_list[i])
    i = i + 1

print_matrix(total_sum)
