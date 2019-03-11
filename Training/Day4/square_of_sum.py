import sys
if len(sys.argv) < 2:
    print 'usage {0} <list of integers>'.format(sys.argv[0])
    sys.exit()

l = [int(x) for x in sys.argv[1:]]
l1 = l[:-1]
l2 = l[1:]

add = lambda x, y: x + y
sq = lambda x : x * x

l3 = map(add, l1, l2)
l4 = map(sq, l3)
res = reduce(add, l4)
print res
