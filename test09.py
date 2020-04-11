import  math
def a():
    for i in range(6):
        if i%2 != 0:
            print("zzzz")
        elif i == 2:
            print("z   ")
        elif i==4:
            print("z  z")
        elif i==6:
            break
b=a()
if __name__=='__main__':
    print(b)

