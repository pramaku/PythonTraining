import socket
import os, sys

HOST = '127.0.0.1'
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    print '      MENU       \n'
    print '1. testprime'
    print '2. nextprime'
    print '3. download file'
    print '4. exit\n'
    ch = raw_input('Enter your choice : ')
    if ch == '4':
        s.sendall(ch)
        print 'bye'
        break
    if int(ch) < 1 or int(ch) > 4:
        os.system('clear')
        print 'Improper choice.... choose right service'
        continue
    if int(ch) == 1 or int(ch) == 2:
        n = raw_input('Enter one number : ')
        data = ch + ':' + n
        s.sendall(data)
        result = s.recv(1024)
        os.system('clear')
        print 'result from server : ', result
    elif int(ch) == 3:
        file_name = raw_input('Enter file name : ')
        data = ch + ':' + file_name
        s.sendall(data)
        new_file_name = 'downloaded_file.txt'
        recv_buf = ''
        recv_data = s.recv(1024)
        print 'received data from server ', recv_data
        if recv_data != '400':
           while recv_data:
             recv_buf = recv_buf + recv_data
             recv_data = s.recv(1024)
           f = open(new_file_name, 'w')
           f.write(recv_buf)
           f.close()
           print '\n Downloaded file ', file_name,
        else:
           print 'file {0} dont exists'.format(file_name)
s.close()

