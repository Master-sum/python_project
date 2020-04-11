import time
def test():
    for i in range(2000000):
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("你是煞笔")
a = test()