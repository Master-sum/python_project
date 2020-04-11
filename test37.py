import time
import threading
b = threading.Lock()
def test():
    for i in range(10000000):
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("你是煞笔")
        c = b.acquire()
        if c:
            print(i)
        b.release()
a = threading.Thread(test())
a.start()