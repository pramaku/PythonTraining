"""
Caluculates the sum of the products of the alternate items in the List.
"""

L = [1,2,3,4,5,6,7,8,9,10]
L1 = L[::2]
L2 = L[1::2]
print(L1)
print(L2)
mul = lambda x,y: x * y
add = lambda x, y: x + y
L3 = map(mul, L1, L2)
final_sum = reduce(add, L3)
print (final_sum)
