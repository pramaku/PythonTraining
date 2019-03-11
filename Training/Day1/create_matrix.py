"""
creates a m*n matrix with the size given by the user.
"""
r, c = int(raw_input('enter row size : ')), int(raw_input('enter col size : '))

print 'enter data ({0} values) : '.format(r * c)
matrix = []

for i in range(r):
    col = []
    for j in range(c):
        x = int(raw_input())
        col.append(x)
    matrix.append(col)

for row in matrix:
    for x in row:
        print x,
    print
