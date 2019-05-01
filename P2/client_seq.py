# This is a local client for sending a sequence to a server
# Practice 2 -session 8

import socket
from Seq import Seq


# Creating a socket or communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Same behaviour as a file

PORT = 8080
IP = '212.128.253.88'

# Connect to the server

s.connect((IP, PORT))

condition = True

while condition:

    # Send a message to the server
    msg2 = Seq(input('Write a DNA-sequence: ').upper())
    msg_rev = str(msg2.reverse().strbases)  # I need to write '.strbases' so the program reads it out of the Seq class and converts it into a str
    s.send(str.encode(msg_rev))  # encode is to translate the string into bytes
    if msg2 == 'exit':
        condition = False
        s.close()
    else:  # receive a message from the server
        msg = s.recv(2048).decode('utf-8')
        print('Message from the server: ')
        print(msg)
