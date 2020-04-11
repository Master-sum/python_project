import socket
from ftplib import FTP
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8001))

while True:
    re = input()
    client.send(re.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf-8"))

