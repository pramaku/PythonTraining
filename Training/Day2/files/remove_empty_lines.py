import sys

if sys.argv < 2:
    print 'Usage {0} <input_file1>'.format(sys.argv[0])
    sys.exit(1)

f1 = open(sys.argv[1])
all_lines = []
line = f1.readline()
while line:
    if line == '\n' or line == '\t':
        line = f1.readline()
        continue
    else:
        all_lines.append(line)
        line = f1.readline()
f1.close()

print(all_lines)
f2 =  open(sys.argv[1], 'w')
[f2.write(line) for line in all_lines]

f2.close()
