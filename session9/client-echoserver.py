import socket
import termcolor


# SERVER IP, PORT
IP = "212.128.253.88"
PORT = 8080

while True:
    # To not block the server, first write and then connect
    msg = input('> ')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: ")
    termcolor.cprint(response, 'red')

    s.close()
