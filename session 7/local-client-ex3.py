#This is a local client for chatting with the server

import socket

#creating a socket or communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
#same behaviour as a file
PORT = 8086
IP = '212.128.253.88'

#connect to the server
s.connect((IP,PORT))

condition = True

while condition:
#send a message to the server
    msg2 = input('Message: ')
    msg2.lower()
    s.send(str.encode(msg2))  # encode is to translate the string into bytes
    if msg2 == 'exit':
        condition = False
        s.close()
    else:  # receive a message from the server
        msg = s.recv(2048).decode('utf-8')
        print('Message from the server: ')
        print(msg)

print('The end')