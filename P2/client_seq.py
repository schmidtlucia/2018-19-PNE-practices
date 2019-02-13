# This is a local client for sending a sequence to a server
# Practice 2 -session 8

import socket

# CREATING CLASS Seq
class Seq:
    """A class for representing sequences"""
    def __init__(self, str_bases):
        self.str_bases = str_bases
    def len(self):
        return len(self.str_bases)
    def reverse(self):



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

