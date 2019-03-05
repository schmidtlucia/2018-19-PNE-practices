#  This server will perform operations on a sequence

import socket
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.253.106"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the message
        msg_c = Seq(msg)  # We have to convert the message sent from the client into the Seq object
        msg_s = 'This is the LENGTH of the sequence given: {}\n, this is the # of A\'s: {}, C\'s: {}, G\'s: {} and T\'s: {} of it; and this itś percentage respectively: {}, {}, {} and{}.: {}'.format(msg_c.len().strbases, msg_c.count('A').strbases, msg_c.count('C').strbases, msg_c.count('G').strbases, msg_c.count('T').strbases, msg_c.perc('A').strbases, msg_c.perc('C').strbases, msg_c.perc('G').strbases, msg_c.perc('T').strbases)
        send_bytes = str.encode(msg_s)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()