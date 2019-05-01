# This is a local client for sending a sequence to a server
# Practice 2 EXTRA -session 8

import socket

# Creating a socket or communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Same behaviour as a file

PORT = 8090
IP = '212.128.253.88'

# Connect to the server

s.connect((IP, PORT))

# Sending a message to the server

msg = input('Enter the sequence to analyze: ').upper()
s.send(str.encode(str(msg)))

# Receiving a message

msg_s = s.recv(2048).decode("UTF-8")
print('Server:\n', msg_s)

s.close()