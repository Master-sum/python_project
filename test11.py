import re
f=open('E:\\1.txt','rb')
k=f.read()

result = re.match(p,k)
result.groups()
