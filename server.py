#server.py

import socket
import time
import threading

#save all the clients' connetions
connections_list = []
#save all pairs of clients and their connections
name_dic = {}

#GUI using Tkinter
#class ChatRoom:
#    def __init__(self):
#        window = Tk()
#        window.title("ChatRoom")
#        self.text = Text(window)
#        self.text.pack()
#        frame1 = Frame(window)
#        frame1.pack()
#        label = Label(frame1, text = "En")

def serverInit():
    #host = socket.gethostname()
    host = '127.0.0.1'
    print('host= %s'% host)
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    return s

def newConnection(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send('Welcome!'.encode())
    while True:
        raw_data = sock.recv(1024).decode()
        time.sleep(1)
        if not raw_data:
            break
        if raw_data == 'exit':
            someoneLeft(name_dic[sock])
            del name_dic[sock]
            connections_list.remove(sock)
            sock.close()
            print('Connection from %s:%s closed.' %addr)
            break
        data = raw_data.split(',')
#        print(data)
        if data[0] == '0':
            client_name = data[1]
            sock.send(('Hello, %s!' % data[1]).encode())
            connections_list.append(sock)
            name_dic[sock] = client_name
            newOneJoined(sock)
        if data[0] == '1':
            print("%s: %s" %(data[1],data[2]))
            for client in name_dic.keys():
                if client != s:
                    client.send(('%s: %s' %(data[1],data[2])).encode())

def newOneJoined(newSock):
    for client in name_dic.keys():
        if client != newSock and client != s:
            client.send(("%s joined the chatroom" %name_dic[newSock]).encode())

def someoneLeft(name):
    for client in name_dic.keys():
        if client != s:
            client.send(("%s left the chatroom" %name).encode())

s = serverInit()
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=newConnection, args=(sock, addr))
    t.start()

