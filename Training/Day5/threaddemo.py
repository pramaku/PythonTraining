"""
create multi threads
"""
from threading import Thread, Lock

class Account:
    def __init__(self):
        self.count = 0

    def deposite(self):
        self.count += 1

    def balance(self):
        return self.count

class Player(Thread):
    def __init__(self, lock, account):
        Thread.__init__(self)
        self.account = account
        self.lock = lock

    def run(self):
        lock = self.lock
        account = self.account
        i = 0
        while i < 1000:
            lock.acquire()
            cur = account.balance()
            account.deposite()
            lock.release()
            i = i + 1

acc = Account()
lock = Lock()

p1 = Player(lock, acc)
p2 = Player(lock, acc)
p3 = Player(lock, acc)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print 'Final account balance = ', acc.balance()
