import sys

if sys.argv < 3:
    print 'Usage {0} <input_file1> <input_file2>.... <outppt_file>'
    sys.exit(1)

ip_files = sys.argv[1:-1]
op_file = sys.argv[-1]

f2 = open(op_file, 'w')
for file in ip_files:
    f1 = open(file)
    line = f1.readline()
    while line:
        f2.write(line)
        line = f1.readline()
    f1.close()
f2.close()
