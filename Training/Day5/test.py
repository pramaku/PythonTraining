from __future__ import division
import sys, os, time
import pickle

if len(sys.argv) != 2:
    print 'usage {0} <input>'.format(sys.argv[0])
    sys.exit(1)

c1 = os.fork()
file_map = [] 
if c1 == 0:
    # child 1 process
    print 'child 1 started with pid : ', os.getpid()
    os.execvp('python', ['python', 'time_lapse_fill_matrix.py', sys.argv[1]])
else:
    file_map.append(str(c1) + '.txt')

c2 = os.fork()
if c2 == 0:
    # child 1 process
    print 'child 2 started with pid : ', os.getpid()
    os.execvp('python', ['python', 'time_lapse_fill_matrix.py', sys.argv[1]])
else:
    file_map.append(str(c2) + '.txt')

c3 = os.fork()
if c3 == 0:
    # child 1 process
    print 'child 3 started with pid : ', os.getpid()
    os.execvp('python', ['python', 'time_lapse_fill_matrix.py', sys.argv[1]])
else:
    file_map.append(str(c3) + '.txt')

f_pic = open('file.txt', 'w')
pickle.dump(file_map, f_pic)
f_pic.close()

r = 1
while True:
    try:
        p = os.wait()
        print p[0], ' completed ', r
    except OSError:
        print 'Game is over'
        c_1 = os.fork()
        #c_1 = 0
        if c_1 == 0:
            f = open('file.txt')
            file_map = pickle.load(f)
            #print file_map
            f.close()
            for file_name in file_map:
              f1 = open(file_name)
              data_nums = []
              for x in f1.readlines():
                x = x[:-1]
                for y in x.split():
                  data_nums.append(int(y))
              f1.close()
              #print file_name, ' -> ', data_nums
              actual_len = len(data_nums)
              unique_len = len(list(set(data_nums)))
              duplicates = actual_len - unique_len
              print file_name.split('.')[0], ' duplicates ', (float(duplicates) / actual_len) * 100, ' % '
            os._exit(0)
        try:
            time.sleep(10)
            q = os.wait()
            print q[0], ' completed '
            os._exit(0)
        except OSError:
            print 'parent exiting'
            os._exit(0)
    r = r + 1

