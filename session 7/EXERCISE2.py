# We are programing a clint, who should enter a string to sent to the server

import socket

# Create a socket for communicating to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket creating')

PORT = 8080
IP = '212.128.253.64'

while True:
    file = input('Please enter a message: ')
    s.connect((IP, PORT))

    s.send(str.encode(file))

    msg = s.recv(2048).decode('utf-8')  #The number is the amount of bytes
    print('Message from the server-LSS')
    print(msg)

    s.close()
