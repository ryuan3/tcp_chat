#client.py
import socket

#host = socket.gethostname()
host = '127.0.0.1'
print('host = %s' %host)
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Linked! Please input your name:")
name = input()
s.send(("%s,0" %name).encode())
info = ""
while info != "exit":
    print("From Others: "+info)
    send_mes = input()
    print("send_mes = %s" %send_mes)
    s.send(send_mes.encode())
    if send_mes == "exit":
        print("exit")
        break
    info = s.recv(1024).decode()
s.close()

