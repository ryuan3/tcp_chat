#server.py

import socket
import time
import threading

def newConnection(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send('Welcome!'.encode())
    while True:
        raw_data = sock.recv(1024).decode()
        time.sleep(1)
        if raw_data == 'exit' or not raw_data:
            sock.close()
            print('Connection from %s:%s closed.' %addr)
            break
        data = raw_data.split(',')
        if data[0] == '0':
            sock.send(('Hello, %s!' % data[1]).encode())
        if data[0] == '1':
            sock.send(('%s: %s' %data[1] %data[2]).encode())
#    sock.close()
#    print('Connection from %s:%s closed.' %addr)

def serverInit():
    #host = socket.gethostname()
    host = '127.0.0.1'
    print('host= %s'% host)
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)



while True:
    sock, addr = s.accept()
    t = threading.Thread(target=newConnection, args=(sock, addr))
    t.start()

