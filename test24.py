x=input('请输入一个数字：')
x_list = list(x)
if len(x_list)>=5:
    a="".join(x_list[0:1])
    a1=int(a)
    b="".join(x_list[1:2])
    b1=int(b)
    c="".join(x_list[2:3])
    c1=int(c)
    d="".join(x_list[3:4])
    d1=int(d)
    e="".join(x_list[4:5])
    e1=int(e)
    if a1==e1 and b1==d1:
        print(a,b,c,d,e)
    else:
        print('123')

