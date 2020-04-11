import socket
from time import ctime
import threading
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',8001))
s.listen()
def many(conn,addr):
    while True:
        m = conn.recv(1024)
        txt = m.decode("utf8")
        print("time:{}\ntxt:{}".format(ctime(), txt))
        a = input(ctime() + ">")
        conn.send(a.encode("utf8"))

while True:
    conn, addr = s.accept()
    c = threading.Thread(target=many,args=(conn, addr))
    c.start()