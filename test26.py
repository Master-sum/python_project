L = ['Hello', 'World', 18, 'Apple', None]

for i in L:
    if isinstance(i, int)==True:
        L.remove(i)
print(L)