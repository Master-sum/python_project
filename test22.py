for a in range(100,999):
    b=int(a/100)
    c=a-(b*100)
    d=int(c/10)
    e=a-(b*100+d*10)
    if a==b**3+d**3+e**3 :
        print(a)

