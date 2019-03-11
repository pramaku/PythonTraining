"""
Clasify the given ip address values as:
'valid', 'invalid' and difference classes.(classA, classB .. etc..)
"""

total_int = raw_input('enter the count of ip address : ')
ip_addrs = []
for x in range(int(total_int)):
    ip_addrs.append(raw_input('enter ip addresses ({0} values): '.format(total_int)))

def is_ip_valid(ip_addr):
    items = ip_addr.split('.')

    if len(items) < 4:
        return False
    else:
        a, b, c, d = items
        if not a.isdigit() or not b.isdigit() or not c.isdigit() or not d.isdigit():
            print('digits in ip')
            return False
        a, b, c, d = int(a), int(b), int(c), int(d)
        valid = False
        if a >= 1 and a <= 255:
            if b >=0 and b <= 255:
                if c >=0 and c <= 255:
                    if d >=0 and d <= 255:
                        valid = True
        return valid

def is_class_a(ip_addr):
    a, b, c, d = [int(x) for x in ip_addr.split('.')]
    if a <= 126 and b <= 255 and c <= 255 and d <=254:
        return True
    return False

def is_class_b(ip_addr):
    a, b, c, d = [int(x) for x in ip_addr.split('.')]
    if a >= 128 and a <= 191:
        if a == 128:
            if b >= 1 and d >= 1:
                return True
            else:
                return False
        else:
            return True
        if d <= 255:
            return True
    return False

def is_class_c(ip_addr):
    a, b, c, d = [int(x) for x in ip_addr.split('.')]
    if a >= 192 and a <= 223:
        if a == 192:
            if c >=1 and d >= 1:
                return True
            else:
                return False
        if a == 223:
            if c <= 254 and d <=254:
                return True
            else:
                return False
    return False

def is_class_d(ip_addr):
    a, b, c, d = [int(x) for x in ip_addr.split('.')]
    if a >= 224 and a <=239:
        return True
    else:
        return False

result = {}
result['valid'] = []
result['invalid'] = []
result['classA'] = []
result['classB'] = []
result['classC'] = []
result['classD'] = []

for ip in ip_addrs:
    if is_ip_valid(ip):
        result['valid'].append(ip)
        if is_class_a(ip):
            result['classA'].append(ip)
        elif is_class_b(ip):
            result['classB'].append(ip)
        elif is_class_c(ip):
            result['classC'].append(ip)
        elif is_class_d(ip):
            result['classD'].append(ip)
    else:
        result['invalid'].append(ip)

class_list = ['valid', 'classA','classB', 'classC',  'classD', 'invalid']
for class_type in class_list:
    print class_type, ' : '
    for value in result[class_type]:
        print '-- ', value
    print '-' * 60
