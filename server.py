#server.py

import socket
import time
import threading

#save all the clients' connetions
connections_list = []
#save all pairs of clients and their connections
name_dic = {}

def serverInit():
    #host = socket.gethostname()
    host = '127.0.0.1'
    print('host= %s'% host)
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

def newConnection(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send('Welcome!'.encode())
    while True:
        raw_data = sock.recv(1024).decode()
        time.sleep(1)
        if raw_data == 'exit' or not raw_data:
            del name_dic[sock]
            connections_list.remove(sock)
            sock.close()
            print('Connection from %s:%s closed.' %addr)
            break
        data = raw_data.split(',')
        if data[0] == '0':
            client_name = data[1]
            sock.send(('Hello, %s!' % data[1]).encode())
            connections_list.append(sock)
            name_dic[sock] = client_name
            newOneJoined(sock)
        if data[0] == '1':
            sock.send(('%s: %s' %data[1] %data[2]).encode())
#    sock.close()
#    print('Connection from %s:%s closed.' %addr)

def newOneJoined(newSock):
    for client in name_dic.keys():
        if client != newSock and client != s:
            client.send(name_dic[newSock] + " joined the chatroom")

def someoneLeft(name):
    for client in name_dic.keys():
        if client != s:
            client.send(name + " left the chatroom")

serverInit()
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=newConnection, args=(sock, addr))
    t.start()

