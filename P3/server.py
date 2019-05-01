#  This server will perform operations on a sequence

import socket
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.253.105"
MAX_OPEN_REQUESTS = 5


def operations(cli):

    # Reading the message from the client
    message = cli.recv(2048).decode("utf-8")
    message = message.split('\n')

    sequence = Seq(message[0])
    nucleicbases = "ACTG"

    for i in message[1:]:
        if i != "len" and i != "complement" and i != "reverse" and i != "countA" and i != "countC" and i != "countG" \
                and i != "countT" and i != "percA" and i != "percC" and i != "percG" and i != "percT":
            final = "Error"
            cli.send(str.encode(final))
            return

    if message[0] == "hey":
        final = "ALIVE"
        cli.send(str.encode(final))
        return

    counter = 0
    for n in message[0].upper():
        if n in nucleicbases:
            counter += 1
            if counter == len(message[0]):
                final = "OK!\n"
            elif counter != len(message[0]):
                final = "Error"
        cli.send(str.encode(final))
        return

    for oper in message[1:]:
        print("Message from the client: {}".format(oper))
        if oper == "len":
            final = str(sequence.len()) + '\n'
        elif oper == "complement":
            final = str(sequence.complement().strbases) + "\n"
        elif oper == "reverse":
            final = str(sequence.reverse().strbases) + "\n"
        elif oper == "countA":
            final = str(sequence.count("A")) + "\n"
        elif oper == "countC":
            final = str(sequence.count("C")) + "\n"
        elif oper == "countG":
            final = str(sequence.count("G")) + "\n"
        elif oper == "countT":
            final = str(sequence.count("T")) + "\n"
        elif oper == "percA":
            final = str(sequence.perc("A")) + "%\n"
        elif oper == "percC":
            final = str(sequence.perc("C")) + "%\n"
        elif oper == "percG":
            final = str(sequence.perc("G")) + "%\n"
        elif oper == "percT":
            final = str(sequence.perc("T")) + "%\n"


# Sending the message back to the client
        # (because we are an echo server)
    cli.send(str.encode(final))


# Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting or connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Attending client: {}".format(address))

    operations(clientsocket)

    # -- Process the client request
    clientsocket.close()
