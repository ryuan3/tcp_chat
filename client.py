#client.py
import socket
import threading

def receiveMessages(s):
    while True:    
        info = s.recv(1024).decode()
        if info and info != "close":
            print(info)
        if info == "close":
            break

def sendMessage(s):
    while True:
        mes = input()
        if mes == "exit":
            s.send(mes.encode())
            print("exit")
            s.close()
            break
        else:
            s.send(("1,%s,%s" %(name, mes)).encode())

#host = socket.gethostname()
host = '127.0.0.1'
print('host = %s' %host)
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
t1 = threading.Thread(target=receiveMessages, args=(s,))
t1.start()
print("Linked! Please input your name:")
name = input()
# 0 means initial info, which is the user's name
s.send(("0,%s" %name).encode())
t2 = threading.Thread(target=sendMessage, args=(s,))
t2.start()




