import pickle

L = [10, 20, [30, 40], 'hello', {1:2}, 50]

fout = open('mydataserialized', 'w')
pickle.dump(L, fout)
fout.close()

fin = open('mydataserialized')
L2 = pickle.load(fin)
print L2
fin.close()
