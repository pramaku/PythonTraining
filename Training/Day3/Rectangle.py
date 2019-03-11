"""
Attributes
    Data Attributes
        instance level - length, breadth
        class level - count
    Operational Attributes
        instance level - area, scale...
        class level - getCount

    name     ==> public attributes.
    __name   ==> private attributes.
    __name__ ==> python attributes.
"""

class Rectangle:
    count = 0
    def __init__(self, x, y):
        self.length = x
        self.breadth = y
        Rectangle.count = Rectangle.count + 1

    def __str__(self):
        return 'Rectangle - [{0} * {1}]'.format(self.length, self.breadth)

    def __add__(self, rhs):
        return Rectangle(self.length + rhs.length, self.breadth + rhs.breadth)

    def __eq__(self, rhs):
        return ((self.length == self.length) and (self.breadth == self.breadth))

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def isSquare(self):
        return self.length == self.breadth

    def scale(self, length = 0, breadth = 0):
        if self.length + length <= 0:
            return self
        else:
            self.length = self.length + length
            return self

        if self.breadth + breadth <= 0:
            return self
        else:
            self.breadth = self.breadth + breadth
            return self

    @classmethod
    def getCount(cls):
        return cls.count

r1 = Rectangle(10, 10)

print 'Area -> ', r1.area()
print 'Perimeter -> ', r1.perimeter()
print 'isSquare -> ', r1.isSquare()
# print 'scale up length to 10' , r.scale(length=10)
# print 'scale down length to 5' , r.scale(length=-5)
# print 'scale up breadth to 10' , r.scale(breadth=10)
# print 'scale down breadth to 5' , r.scale(breadth=-5)
# print 'scale up length and breadth to 10, 10' , r.scale(length=10, breadth=10)
# print 'scale down length and breadth to 10, 10' , r.scale(length=-10, breadth=-10)
# print 'scale down length and breadth to 20, 20' , r.scale(length=-20, breadth=-20)

r2 = Rectangle(20, 20)

r3 = r1 + r2   # r3 = r1.__add__(r2)
print r3

if r1 == r2:
    print 'equal'
else:
    print 'not equal'

print 'count ', Rectangle.getCount()
