a=int(input('请输入：'))
print('%d='%a,end='')
num=2
while num<=a:
    if a%num ==0:
        a/=num
        print('%d*'%num,end="")
    else:
        num+=1