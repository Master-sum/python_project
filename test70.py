import  time
from functools import wraps
def timethis(func):

    def wrapper(*args):




        start = time.time()
        result = func(*args)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper
@timethis
def co(n):
    while n>0:
        n -=1
c = co(1000000)