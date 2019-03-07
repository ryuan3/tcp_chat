#client.py
import socket

#host = socket.gethostname()
host = '127.0.0.1'
print('host = %s' %host)
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode())
s.send('Lisa'.encode())
print(s.recv(1024).decode())
s.send('exit'.encode())
s.close()
