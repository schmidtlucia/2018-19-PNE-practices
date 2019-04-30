# This is a local client for sending a sequence to a server
# Practice 2 -session 8

import socket

# SERVER IP, PORT

PORT = 8080
IP = "212.128.253.105"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

msg = "ACTGATCAT\nlen\ncomplement"
if msg == "":
    msg = "hey"


# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode()

# Print the server's response
print(response)

s.close()