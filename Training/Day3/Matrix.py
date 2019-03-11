"""
"""
class Matrix:
    def __init__(self, file_name="", matrix=[]):
        self.row = 0
        self.col = 0
        self.matrix = []
        if file_name:
            f = open(file_name)
            line = f.readline()
            while line:
                self.matrix.append([int(x) for x in line.split()])
                line = f.readline()
            f.close()
        elif matrix:
            self.matrix = matrix
        self.row = len(self.matrix)
        if self.row > 0:
            self.col = len(self.matrix[0])

    def size(self):
        return '[{0} * {1}]'.format(self.row, self.col)

    def __str__(self):
        return str(self.matrix)

    def __add__(self, rhs):
        i = 0
        matrix = []
        while i < self.row:
            col = []
            c1 = self.matrix[i]
            c2 = rhs.matrix[i]
            j = 0
            while j < self.col:
                col.append(c1[j] + c2[j])
                j = j + 1
            matrix.append(col)
            i = i + 1
        return Matrix(matrix=matrix)

    def write(self, file_name):
        f = open(file_name, 'w')
        for row in self.matrix:
            [f.write(str(x) + ' ') for x in row]
            f.write('\n')
        f.close()

m1 = Matrix(file_name=r"temp\m1.txt")
m2 = Matrix(r"temp\m2.txt")

m3 = m1 + m2
print m3.size()
print m3
m3.write(r'temp\m3.txt')
