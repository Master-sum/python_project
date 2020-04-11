def am(y,b):
   for i in range(1,y+1):
       b1=b*0.05
       b=b1+b
       b2=str(b)
       y1=str(y)
   print('year'+''+y1+':'+b2)
print(am(7,100))