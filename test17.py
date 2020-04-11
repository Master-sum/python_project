import socket
s = socket.socket()
host = socket.gethostbyname()
port = 1234
s.connect((host.port))
print(s.recv(1024))