"""
Demo file for creating multiple processes.
"""

import sys, os
if len(sys.argv) != 2:
    print 'usage {0} <input>'.format(sys.argv[0])
    sys.exit(1)

c1 = os.fork()
if c1 == 0:
    # child 1 process
    print 'child 1 started with pid : ', os.getpid()
    os.execvp('python', ['python', 'time_lapse_fill_matrix.py', sys.argv[1]])

c2 = os.fork()
if c2 == 0:
    # child 1 process
    print 'child 2 started with pid : ', os.getpid()
    os.execvp('python', ['python', 'time_lapse_fill_matrix.py', sys.argv[1]])

c3 = os.fork()
if c3 == 0:
    # child 1 process
    print 'child 3 started with pid : ', os.getpid()
    os.execvp('python', ['python', 'time_lapse_fill_matrix.py', sys.argv[1]])

r = 1
while True:
    try:
        p = os.wait()
        print p[0], ' completed ', r
        c_1 = os.fork()
        if c_1 == 0:
            f = open(str(p[0]) + ".txt")
            data = f.read()
            data_nums = []
            for x in data:
                if x.isdigit():
                    data_nums.append(int(x))

            actual_len = len(data_nums)
            unique_len = len(list(set(data_nums)))
            duplicates = actual_len - unique_len
            print p[0], ' duplicates ', duplicates
    except OSError:
        print 'Game is over'
        os._exit(0)
    r = r + 1
