# This is an echo server
import socket
import termcolor


PORT = 8080
IP = '212.128.253.88'
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode('utf-8')  # max length of bytes (2048) we want to recieve

    print('Message from the client: ')
    termcolor.cprint(msg, 'red')

    # Sending the message back to the client
    # (bc we are an echo server
    answer = input('Answer from server: ')
    cs.send(str.encode(answer))

    cs.close()


# Create a socket for connecting with the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))  # bc there are two parameters and it only accepts one we need to make a double parenthesis

serversocket.listen(MAX_OPEN_REQUEST)  # server should only listen to a maximum of 5 clients and no more

print('Socket ready: {}'.format(serversocket))

while True:
    print('Waiting for connections at: {}, {}'.format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    # -- Process the client request
    print('Attending client: {}'.format(adress))

    process_client(clientsocket)
