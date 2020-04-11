import time
from functools import wraps


def wrapper():
    start = time.time()
    print(start)
    n = 100000

    if n != 0:

        while n > 0:
            n -= 1

    end = time.time()
    print(end)
    print( end - start)








c = wrapper()
