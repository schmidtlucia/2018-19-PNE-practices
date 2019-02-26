# We are programing a client

import socket

# Create a socket for communicating to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket creating')

PORT = 8085
IP = '212.128.253.89'

s.connect((IP, PORT))

s.send(str.encode('Soy una pesada'))

msg = s.recv(2048).decode('utf-8')  #The number is the amount of bytes
print(msg)
