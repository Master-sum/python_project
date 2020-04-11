import socket
s=socket.socket()
host = socket.gethostbyname()
port = 1234
s.bind((host,port))
s.listen(6)
while True:
    c,addr = s.accept()
    print('接受请求')
    c.send('请求成功')
    c.close()

