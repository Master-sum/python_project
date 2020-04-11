import time
import threading
def test():
    for i in range(20000):
        print (f"started at {time.strftime('%X')}")
        print("你是煞笔")
a = threading.Thread(test())
a.start()