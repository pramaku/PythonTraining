"""
Checks if the given input ip address isvalid or invalid.
"""

import sys

ip_addr = raw_input("Enter the ip address : ")
items = ip_addr.split('.')

def invalid():
    print '{0} in invalid'.format(ip_addr)
    sys.exit()

if len(items) < 4:
    invalid()
else:
    a, b, c, d = items
    if not a.isdigit() and not b.isdigit() and not c.isdigit() and not d.isdigit():
        print('digits in ip')
        invalid()
    a, b, c, d = int(a), int(b), int(c), int(d)
    valid = False
    if a >= 1 and a <= 255:
        if b >=0 and b <= 255:
            if c >=0 and c <= 255:
                if d >=0 and d <= 255:
                    valid = True
    if not valid:
        invalid()

print '{0} in valid'.format(ip_addr)
