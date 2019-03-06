import socket
import termcolor

# Change this IP to yours!!!!!
IP = "212.128.253.111"
PORT = 8088
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print("\nRequest message: ")
    termcolor.cprint(msg, 'blue')

    # We have to split the message sent by the client into the first line to analyze the request

    req_line = msg.split('\n', 1)[0]  # this is the first line of the message, i.e. the request line
    request = req_line.split(' ')[1]

    print(request)

    if request == '/':
        file = open('index.html', 'r')
        content = file.read()
        file.close()
    elif request == '/pink':
        file = open('pink.html', 'r')
        content = file.read()
        file.close()
    elif request == '/blue':
        file = open('blue.html', 'r')
        content = file.read()
        file.close()
    else:
        file = open('error.html', 'r')
        content = file.read()
        file.close()

    status_line = 'HTTP/1.1 200 OK\r\n'
    header = '  Content-Type: text/html\r\n'
    header += ' Content-Length: {}\r\n'.format(len(str.encode(content)))

    # We have to summ it up into one message: response
    response = status_line + header + '\r\n' + content

    # We send the response
    cs.send(str.encode(response))

    # We close the socket
    cs.close()

# ----------------------------------------------------------------------------------------
# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)