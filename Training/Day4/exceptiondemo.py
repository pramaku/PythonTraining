"""
demo file for exception handling.
"""

print 'demo'

L = [10, 20, 30]

try:
    #import python
    x = int(raw_input('integer first number:'))
    y = int(raw_input('integer second number:'))
    z = x / y
    print z
    print L[10]
except ValueError:
    print 'Value error on conversion of input'
    print x
except IndexError:
    print 'index error on list'
except ZeroDivisionError:
    print 'divide by zero error because ', z, ' is zero'
except ImportError as e:
    print 'error: ', e
except Exception as e:
    print 'Exception on processing code : ', type(e)
else:
    print 'No exception'
finally:
    print 'finally block'
