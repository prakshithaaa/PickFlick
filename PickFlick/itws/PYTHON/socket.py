import socket
ss = socket.socket()
ss.bind('localhost', 9999)
ss.listen(5)
print("waiting for client")

while True:
    cs, addr=ss.accept()
    name=cs.recv(1024).decode()
    print("Connected to", addr, name)
    cs.send(bytes("Hello",'utf-8'))
    cs.close()