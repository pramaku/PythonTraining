import random
import sys
import time
import os


if len(sys.argv) < 2:
    #print 'please give matrix order'
    sys.exit(1)

n = int(sys.argv[1])

def get_matrix(r, c):
    matrix = []
    for i in range(r):
        col = []
        for j in range(c):
            x = 0
            col.append(x)
        matrix.append(col)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for x in row:
            pass
            #print '%3d' % x,
        #print

def write_to_matrix(m, file_name):
    f1 = open(file_name, 'w')
    for row in m:
        for col in row:
            f1.write(str(col))
            f1.write(' ')
        f1.write('\n')
    f1.close()

m = get_matrix(n, n)
hits = {}
total_filled = 0
start_time = time.time()
while total_filled < (n * n):
    r = random.choice(range(0,n))
    c = random.choice(range(0,n))
    if not m[r][c]:
        cell = random.choice(range(0, 1000))
        m[r][c] = cell
        total_filled = total_filled + 1
    else:
        continue

elapsed = time.time() - start_time

#print_matrix(m)

#print 'time elapsed to fill [{0} * {1}] matrix - {2} seconds'.format(n, n, elapsed)
write_to_matrix(m, str(os.getpid()) + ".txt")
os._exit(0)
