"""
generator demo
"there should not be any return statement in generator functions"
"""

import time
def sequence():
    i = 0
    while True:
        i = i + 1
        yield i  # entry and exit for the function.


seq = sequence()
print type(seq)


for i in range(10):
    print next(seq)
    time.sleep(1)


# generate the even sequence.
def even_sequence(seed = 0):
    i = 0
    a = 1
    if seed == 1:
        i = -1
        a = 2
    if seed == 2:
        a = 2
    while True:
        i = i + a
        yield i  # entry and exit for the function

even_seq = even_sequence(2)

for i in range(10):
    print next(even_seq)
    time.sleep(1)
