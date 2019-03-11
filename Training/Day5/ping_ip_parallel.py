import os
import re
import time
import sys

from threading import Thread, Lock

pat = re.compile(r'(\d) received')
report = ("No response", 'Partial Response', "Alive")

class IpPing(Thread):
    def __init__(self, ip, name, lock):
        Thread.__init__(self)
        self.ip = ip
        self.name = name
        self.lock = lock

    def run(self):
        start = time.time()
        ip = self.ip
        channel = os.popen('ping -q -c2 ' + ip, 'r')
        self.lock.acquire()
        print self.name, 'Testing .... ' + ip
        self.lock.release()
        sys.stdout.flush()
        while True:
            line = channel.readline()
            if not line:
                break
            result = re.findall(pat, line)
            if result:
                print self.name, report[int(result[0])]
        self.lock.acquire()
        print '{0} took {1} threads to ping {2} ip'.format(self.name, time.time() - start, self.ip)
        self.lock.release()

i = 0
name = 't'
thds = []
lock = Lock()
for host in range(60, 70):
    ip = '192.168.200.' + str(host)
    p = IpPing(ip, name + str(i), lock)
    thds.append(p)
    i = i + 1

for th in thds:
  th.start()

for th in thds:
  th.join()

print 'main thread waiting for other threads'
