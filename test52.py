import multiprocessing
import threading
from time import ctime
import time
def t1():
    for i in range(1000):
        print("{}start:{}".format(i,ctime()))

def t2():
    for i in range(1000):
        print("{}start1:{}".format(i, ctime()))
def t3():
    for i in range(1000):
        print("{}start1:{}".format(i, ctime()))
'''a = threading.Thread(target=t1)
     b = threading.Thread(target=t2)
     a.start()
     b.start()
     a.join()
     b.join()'''
'''a = multiprocessing.Process(target=t1)
     b = multiprocessing.Process(target=t2)'''
if __name__ == '__main__':
     T = time.time()
     print("------------------")
     a = threading.Thread(target=t1)
     b = threading.Thread(target=t2)
     c = threading.Thread(target=t3)
     a.start()
     b.start()
     c.start()
     a.join()
     b.join()
     c.join()
     te = time.time()
     print("using time: " + str(te - T) + "s")
#1.0.5365631580352783s不使用线程、进程
#2.0.015622854232788086s使用线程
#3.0.6405787467956543s使用进程