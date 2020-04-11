import _thread
from time import sleep,ctime

def loop0():
    print('start loop 0 at:%s'%ctime())
    sleep(4)
    print('end loop0 at:%s'%ctime())
def loop1():
    print('start loop 1 at:%s'%ctime())
    sleep(2)
    print('end loop  1 at:%s'%ctime())
def main():
    print('starting at:%s'%ctime())#1
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('end all')
if __name__ == '__main__':
    main()
