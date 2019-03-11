import sys

def get_matrix_from_file(file_name):
    m = []
    f1 = open(file_name)
    line = f1.readline()
    while line:
        m.append([int(x) for x in line.split()])
        line = f1.readline()
    f1.close()
    return m

def sum_matrix(m1, m2):
    res = []
    i = 0
    while i < len(m1):
        col = []
        c1_m1 = m1[i]
        c1_m2 = m2[i]
        j = 0
        while j < len(m1[0]):
            col.append(c1_m1[j] + c1_m2[j])
            j = j + 1
        res.append(col)
        i = i + 1
    return res

if sys.argv < 4:
    print 'usage {0} <matrix 1 file> <matrix 2 file>  <matrix output file> '.format(sys.argv[0])
    sys.exit(0)

m1 = get_matrix_from_file(sys.argv[1])
m2 = get_matrix_from_file(sys.argv[2])
m3 = sum_matrix(m1, m2)

f1 = open(sys.argv[3], 'w')
for row in m3:
    for col in row:
        f1.write(str(col))
        f1.write(' ')
    f1.write('\n')
f1.close()
