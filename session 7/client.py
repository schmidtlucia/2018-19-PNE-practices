# We are programing our first client

import socket

# Create a socket for communicating to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket creating')

PORT = 8080
IP = '212.128.253.64'

s.connect((IP, PORT))

s.send(str.encode('Hola'))

msg = s.recv(2048).decode('utf-8')  #The number is the amount of bytes
print('Message from the server-LSS')
print(msg)

s.close()

print('The end')
