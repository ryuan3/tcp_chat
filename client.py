#client.py
import socket
import threading
from tkinter import *

def receiveMessages(s,text):
    while True:    
        info = s.recv(1024).decode()
        if info and info != "close":
            print(info)
            text.insert(END, info+"\n")
        if info == "close":
            break

class Chat:
    def __init__(self):
        window = Tk()
        window.title("Chat_Client")
        self.text = Text(window)
        self.text.pack()
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1, text= "Enter your Message: ")
        self.Message = StringVar()
        entryMessage = Entry(frame1, textvariable=self.Message)
        sendButton = Button(frame1, text = "Send", command = self.sendButtonPressed)
        connectButton = Button(frame1, text = "Connect", command = self.connectButtonPressed)

        label.grid(row=1,column=1)
        entryMessage.grid(row=1,column=2)
        sendButton.grid(row=1,column=4)
        connectButton.grid(row=1,column=5)
        self.text.insert(END, "\t\t\t-------------Chat Room------------\n\nEnter your name and click the connect button :)\n\n\n")
        window.mainloop()

    def sendButtonPressed(self):
        mes = self.Message.get()
        if mes == "exit":
            self.s.send(mes.encode())
            self.text.insert(END, "You left the chatroom.\n")
            print("exit")
            self.s.close()
        else:
            self.s.send(("1,%s,%s" %(self.name, mes)).encode())

#def sendMessage(s):
#    while True:
#        mes = input()
#        if mes == "exit":
#            s.send(mes.encode())
#            print("exit")
#            s.close()
#            break
#        else:
#            s.send(("1,%s,%s" %(self.name, mes)).encode())


    def connectButtonPressed(self):
        #host = socket.gethostname()
        host = '127.0.0.1'
        print('host = %s' %host)
        port = 12345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        t1 = threading.Thread(target=receiveMessages, args=(self.s,self.text))
        t1.start()
        self.text.insert(END, "Linked!\n")
        self.name = self.Message.get()
        # 0 means initial info, which is the user's name
        self.s.send(("0,%s" %self.name).encode())

Chat()


