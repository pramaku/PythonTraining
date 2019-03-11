import socket
import os, sys

def testprime(m):
    if m < 2 :
        return str(False)
    i = 2
    while i < m:
        if m % i == 0:
            return str(False)
        i = i + 1
    return str(True)

def nextprime(m):
    while True:
        m = m + 1
        if testprime(m): return str(m)

def downloaded_file(file_name):
    send_buf = ''
    try:
        f = open(file_name)
        for line in f.readlines():
            send_buf = send_buf + line
        f.close()
        return send_buf
    except IOError:
        return 'file {0} dont exist on server'.format(file_name)

lookup = {'1': testprime, '2': nextprime, '3': downloaded_file}

HOST = ''
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
os.system("clear")
print 'server is up and running'
sys.stdout.flush()

while True:
    conn, addr = s.accept()
    print "\n connection established from ", addr[0],
    sys.stdout.flush()
    child = os.fork()
    if child == 0:
        while True:
            data = conn.recv(1024)
            if data == '4':
                break
            li = data.split(':')
            result = lookup[li[0]](li[1])
            conn.sendall(result)
        conn.close()
        print '\n connection closed by ', addr[0],
        sys.stdout.flush()
        os._exit(0)

    conn.close()

