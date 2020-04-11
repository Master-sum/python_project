import time
s = time.time()
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
        print(s)
    while s[-1:] == ' ':
        s = s[:-1]
        print(s)
    return s
trim(s)