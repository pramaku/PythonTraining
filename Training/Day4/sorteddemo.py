L = ['hello', 'hi', 'apple', 'ok', 'fine']
L = sorted(L, key=lambda x:len(x))
# print L

L = [(10, 20), (20, 5), (1, 30), (6, 7)]
L = sorted(L, key=lambda t: t[1])

print L
