import sys
f=open(r'E:\a.txt')

for i in range(3):
    print(str(i)+': '+f.readline(),end=' ')