"""
"""
import time

def testprime(m):
    m =m
    if m < 2 :
        return False
    i = 2
    print 'input ', m
    while i < m:
        if m % i == 0:
            return False
        i = i + 1
    return False

def prime_sequence():
    i = 2
    while True:
        i = i + 1
        print 'testing ', i, ' is prime'
        while not testprime(i):
            i = i + 1
        print 'next is ', i
        yield i

seq = prime_sequence()
print seq
for i in range(10):
    print next(seq)
    time.sleep(1)
