"""
Prints the smallest integer of all the given three numbers.
"""

msg = "enter your numbers (3 values): "
x, y, z = int(raw_input(msg)), int(raw_input(msg)), int(raw_input(msg))

result = 0
if x < y:
    if x < z:
        result  = x
    else:
        result = z
else:
    if z < y:
        result  = z
    else:
        result = y

print 'Smallest of {0} ,{1}, {2} is {3}'.format(x, y, z, result)
