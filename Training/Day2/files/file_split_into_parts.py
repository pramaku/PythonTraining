import sys

if len(sys.argv) < 3:
    print 'Usage {0} <input_file1> <num_partitions>'.format(sys.argv[0])
    sys.exit(1)

f1 = open(sys.argv[1])
all_lines = f1.readlines()
f1.close()
total_line_count = len(all_lines)

nparts = int(sys.argv[2])
total_lines_per_file = total_line_count / nparts
output_files = [sys.argv[1] + '_part_' + str(x) + '.txt' for x in range(1, nparts + 1)]
current_index = 0
i = 0
while True:
    if i == len(output_files):
        i = 0
    lines_to_write = all_lines[current_index:total_lines_per_file + current_index]
    print len(lines_to_write)
    if len(lines_to_write) < total_lines_per_file:
        f_last = open(output_files[-1], 'a')
        f_last.writelines(lines_to_write)
        f_last.close()
        break

    if not lines_to_write:
        break

    file = open(output_files[i], 'a')
    file.writelines(lines_to_write)
    file.close()
    current_index = current_index + total_lines_per_file
    i = i + 1
