import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8001))
server.listen()
def mang(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"))
        re = input()
        sock.send(re.encode("utf8"))
while True:
    sock, addr = server.accept()
    a = threading.Thread(target=mang,args=(sock,addr))
    a.start()
