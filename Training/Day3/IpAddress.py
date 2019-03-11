"""
"""
class IpAddress:
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.__a, self.__b, self.__c, self.__d = ipaddr.split('.')

    def __str__(self):
        return self.ipaddr

    def isValid(self):
        items = self.ipaddr.split('.')
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

    def getClass(self):
        if not self.isValid():
            return ""
        if self.__is_class_a():
            return "classA"
        if self.__is_class_b():
            return "classB"
        if self.__is_class_c():
            return "classC"
        if self.__is_class_d():
            return "classD"

    def __is_class_a(self):
        a, b, c, d = [int(x) for x in self.ipaddr.split('.')]
        if a <= 126 and b <= 255 and c <= 255 and d <=254:
            return True
        return False

    def __is_class_b(self):
        a, b, c, d = [int(x) for x in self.ipaddr.split('.')]
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

    def __is_class_c(self):
        a, b, c, d = [int(x) for x in self.ipaddr.split('.')]
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

    def __is_class_d(self):
        a, b, c, d = [int(x) for x in  self.ipaddr.split('.')]
        if a >= 224 and a <=239:
            return True
        else:
            return False

    def __eq__(self, rhs):
        return self.ipaddr == rhs.ipaddr

    def nextIp(self):
        if self.isValid():
            d = int(self.__d)
            c = int(self.__c)
            b = int(self.__b)
            a = int(self.__a)
            if d < 255:
                d = d + 1
                new_ip = '.'.join([self.__a, self.__b, self.__c])
                new_ip = new_ip + '.' + str(d)
                return IpAddress(new_ip)
            elif c < 255:
                # d is 255
                c = int(self.__c)
                d = 0
                c = c + 1
                new_ip = '.'.join([self.__a, self.__b])
                new_ip = new_ip + '.' + str(c) + '.' + str(d)
                return IpAddress(new_ip)
            elif b < 255:
                d = 0
                c = 0
                b = int(self.__b)
                b = b + 1
                new_ip = '.'.join([self.__a])
                new_ip = new_ip + '.' + str(b) + '.' + str(c) + '.' + str(d)
                return IpAddress(new_ip)
            elif a < 255:
                b, c, d = (0, 0, 0)
                a = int(self.__a)
                a = a + 1
                new_ip = '.'.join([str(a), str(b), str(c), str(d)])
                return IpAddress(new_ip)
            else:
                return 'Current ip {0} is the max ip '.format(self)
        else:
            print 'cannot create new IP, current {0} is not valid'.format(self)

ip1 = IpAddress("10.2.3.4")
print "{0} is Valid -> {1}".format(ip1, ip1.isValid())
print "{0} class    -> {1}".format(ip1, ip1.getClass())

ip2 = IpAddress("10.2.3.4")
print '{0} == {1} -> {2}'.format(ip1, ip2, ip1 == ip2)

ip2 = IpAddress("10.2.3.5")
print '{0} == {1} -> {2}'.format(ip1, ip2, ip1 == ip2)

print 'next ip of {0} -> {1}'.format(ip1, ip1.nextIp())

test_ip_str = '10.2.3.255'
print 'next ip of {0} -> {1}'.format(IpAddress(test_ip_str), IpAddress(test_ip_str).nextIp())

test_ip_str = '10.2.255.255'
print 'next ip of {0} -> {1}'.format(IpAddress(test_ip_str), IpAddress(test_ip_str).nextIp())

test_ip_str = '10.255.255.255'
print 'next ip of {0} -> {1}'.format(IpAddress(test_ip_str), IpAddress(test_ip_str).nextIp())

test_ip_str = '255.255.255.255'
print 'next ip of {0} -> {1}'.format(IpAddress(test_ip_str), IpAddress(test_ip_str).nextIp())
