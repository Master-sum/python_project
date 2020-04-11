import socket
from time import ctime
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8001))

while True:
    t = input(ctime()+">")
    s.send(t.encode("utf8"))
    m = s.recv(1024)
    if m is not None:
        txt = m.decode("utf8")
        print("time:{}\ntxt:{}".format(ctime(),txt))